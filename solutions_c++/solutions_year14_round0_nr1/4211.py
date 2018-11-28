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

float s2f(string input)
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
    float dec = (float)(s2n(b));
    for (int i=0;i<b.length();i++)
    {
        dec/=10;
    }
    return (float)num + dec;
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
        string* out = new string;
        *out = "0";
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

int main(void)
{
	ifstream ifile;
	ifile.open("Msmall.txt");
	string input="";
	getline(ifile,input);
    int sets = s2n(input);
    for (int set=0;set<sets;set++)
    {
        cout<<"Case #"<<set+1<<": ";
        string* rel = new string[2];
        for (int j=0;j<2;j++)
        {
            rel[j]="";
            getline(ifile,input);
            int opt = s2n(input);
            for (int i=0;i<4;i++)
            {
                getline(ifile,input);
                if (i+1==opt)
                {
                    rel[j]+=input;
                }
            }
        }
        int* r1 = new int[4];
        int* r2 = new int[4];
        string* s1 = parse(rel[0],' ');
        string* s2 = parse(rel[1],' ');
        for (int i=0;i<4;i++)
        {
            r1[i]=s2n(s1[i+1]);
            r2[i]=s2n(s2[i+1]);
        }
        int* sol = new int[5];
        sol[0]=0;
        for (int i=0;i<4 && sol[0]<2;i++)
        {
            for (int j=0;j<4 && sol[0]<2;j++)
            {
                if (r1[i]==r2[j])
                {
                    sol[0]++;
                    sol[sol[0]]=r1[i];
                }
            }
        }
        if (sol[0]==0)
        {
            cout<<"Volunteer cheated!\n";
        }
        else if (sol[0]==1)
        {
            cout<<sol[1]<<endl;
        }
        else
        {
            cout<<"Bad magician!\n";
        }
    }
    return 0;
}















