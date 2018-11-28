#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cstdio>
#include <string>
using namespace std;

string n2s(int input)
{
    string out = "";
    int neg = 1;
    if (input<0)
    {
        input*=-1;
        int neg = -1;
    }
    if (input==0)
    {
        return "0";
    }
    while (input>0)
    {
        int rel = input-(input/10)*10;
        out+=" ";
        out[out.length()-1]=rel+'0';
        input/=10;
    }
    if (neg==-1)
    {
        out+="-";
    }
    string put = out;
    for (int i=0;i<out.length();i++)
    {
        put[i]=out[out.length()-1-i];
    }
    return put;
}
string f2s(double input)
{
    int num = (int) input;
    int neg = 1;
    if (input<0)
    {
        input*=-1;
        int neg = -1;
    }
    double rem = input-(double)num;
    string out = "";
    for (int i=0;i<8;i++)
    {
        rem*=10;
        int temp = (int)rem;
        rem=rem-(double)temp;
        out = out+" ";
        out[out.length()-1]=temp+'0';
    }
    out = (n2s(num)+"."+out);
    if (neg==-1)
    {
        out = "-"+out;
    }
    return out;
}

int s2n(string input)
{
    int out=0;
    int neg=1;
    if (input.length()>=1)
    {
        if (input[0]=='-')
        {
            neg=-1;
            input=input.substr(1,input.length()-1);
        }
    }
    for (int i=0;i<input.length();i++)
    {
        out*=10;
        out+=input[i]-'0';
    }
    out*=neg;
    return out;
}

double s2f(string input)
{
    int neg=1;
    if (input.length()>=1)
    {
        if (input[0]=='-')
        {
            neg=-1;
            input=input.substr(1,input.length()-1);
        }
    }
    int loc = 0;
    while (input[loc]!='.' && loc<input.length()-1)
    {
        loc++;
    }
    string f = input.substr(0,loc);
    string b = input.substr(loc+1,input.length()-loc-1);
    int num = s2n(f);
    double dec = (double)(s2n(b));
    for (int i=0;i<b.length();i++)
    {
        dec/=10;
    }
    return (double)num + dec;
}

string* parse(string input, char del)
{
    int count=0;
    for (int i=0;i<input.length();i++)
    {
        if (input[i]==del)
            count++;
    }
    if (count==0)
    {
        string* out = new string[2];
        out[0]=1;
        out[1]=input;
        return out;
    }
    string* out = new string[count+2];
    for (int i=0;i<count+2;i++)
    {
        out[i]="";
    }
    out[0]=n2s(count+1);
    for (int i=0;i<count;i++)
    {
        int loc=0;
        while (input[loc]!=del)
        {
            loc++;
        }
        out[i+1]=input.substr(0,loc);
        input=input.substr(loc+1,input.length()-loc-1);
    }
    out[count+1]=input;
    return out;
}

void mergeSort(double* input,int l, int r)
{
    if (l==r)
    {
        return;
    }
    mergeSort(input,l,(l+r)/2);
    mergeSort(input,(l+r)/2+1,r);
    int x=l;
    int y=(l+r)/2+1;
    double* out = new double[r-l+1];
    int i = 0;
    while (x<(l+r)/2+1 && y<r+1)
    {
        if (input[x]<input[y])
        {
            out[i]=input[x];
            x++;
        }
        else
        {
            out[i]=input[y];
            y++;
        }
        i++;
    }
    if (x==(l+r)/2+1)
    {
        while (y<r+1)
        {
            out[i]=input[y];
            y++;
            i++;
        }
    }
    else
    {
        while (x<(l+r)/2+1)
        {
            out[i]=input[x];
            i++;
            x++;
        }
    }
    for (int j=0;j<r-l+1;j++)
    {
        input[l+j]=out[j];
    }
}

int main(void)
{
	ifstream ifile;
    ofstream ofile;
    ofile.open("dwarOUT.txt");
	ifile.open("dwar.txt");
	string input="";
	getline(ifile,input);
    int sets = s2n(input);
    for (int set=0;set<sets;set++)
    {
        ofile<<"Case #"<<set+1<<": ";
        getline(ifile,input);
        int num = s2n(input);
        double* k = new double[num];
        double* n = new double[num];
        getline(ifile,input);
        string* in1 = parse(input,' ');
        getline(ifile,input);
        string* in2=parse(input,' ');
        for (int i=0;i<num;i++)
        {
            k[i]=s2f(in2[i+1]);
            n[i]=s2f(in1[i+1]);
        }
        mergeSort(k,0,num-1);
        mergeSort(n,0,num-1);
        int war = 0;
        int x=num-1;
        int y=num-1;
        while (x>=0)
        {
            if (n[x]>k[y])
            {
                war++;
            }
            else
            {
                y--;
            }
            x--;
        }
        int dwar = 0;
        int x1=0;
        int x2=num-1;
        int y1=0;
        int y2=num-1;
        while (x1<=x2)
        {
            if (n[x1]<k[y1])
            {
                y2--;
                x1++;
            }
            else
            {
                dwar++;
                x1++;
                y1++;
            }
        }
        ofile<<dwar<<" "<<war<<endl;
    }
    ofile.close();
    return 0;
}















