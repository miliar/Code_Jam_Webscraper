#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
#include <fstream>

using namespace std;

long long ans;

void check(string &, string &);

int main()
{
ifstream in; //Creating object for input stream
ofstream out; //Creating object for output stream

in.open("input.in");    //open a file to read input
out.open("output_pan.txt"); //open a file to write output

    long long t,x,cnt,t_num,i,dg;
    string s,flag;
    in>>t;
    for(x=1;x<=t;x++)
    {
        in>>s;
        flag="+";
        ans=0;
        check(s,flag);
		out<<"Case #"<<x<<": "<<ans<<endl;
	}

in.close();             //closing the input file
out.close();            //closing the output file

    return 0;
}

void check(string &s, string &flg)
{
    long long len,i;
    len=s.length();
    if(len==0)
        return;
    for(i=len-2;i>=0&&(s[i]==s[i+1]);i--);
    if(s[i+1]!=flg[0])
    {
        ans++;
        flg=(flg=="+"?"-":"+");
    }
    s=s.substr(0,i+1);
    check(s,flg);
    return;
}
