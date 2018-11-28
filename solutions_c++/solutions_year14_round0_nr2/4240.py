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
    ofstream ofile;
    ofile.open("cookieOUT.txt");
	ifile.open("cookie.in");
	string input="";
	getline(ifile,input);
    int sets = s2n(input);
    for (int set=0;set<sets;set++)
    {
        ofile<<"Case #"<<set+1<<": ";
        getline(ifile,input);
        string* in = parse(input,' ');
        double c = s2f(in[1]);
        double f = s2f(in[2]);
        double x = s2f(in[3]);
        double num = (x/c)-(2/f)-1;
        int n = (int)num;
        if (n<num)
            n++;
        double out = 0;
        double r = 2;
        cout<<c<<":"<<f<<":"<<x<<":"<<n<<endl;
        for (int i=0;i<n;i++)
        {
            out+=(c/r);
            r+=f;
        }
        out+=(x/r);
        ofile<<f2s(out)<<endl;
    }
    ofile.close();
    return 0;
}















