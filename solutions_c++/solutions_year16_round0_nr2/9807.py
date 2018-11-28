#include<cstdio>
#include<iostream>
#include<algorithm>
#include <fstream>
#include<cstring>
#include<algorithm>
using namespace std;
int ans;
void reverse_check(string &, string &);
int main()
{
ifstream input; //Creating object for input stream
ofstream output; //Creating object for output stream
input.open("B-large.in");    //open a file to read input
output.open("outlg.txt"); //open a file to write output
int test,loop,ans1,ans2;
string str,cp,str2;
input>>test;
for(loop=1;loop<=test;loop++)
{
input>>str;
str2=str;
cp="+";
ans=0;
reverse_check(str,cp);
ans1=ans;
cp="-";
ans=1;
reverse_check(str2,cp);
ans2=ans;
output<<"Case #"<<loop<<": "<<min(ans1,ans2)<<endl;
}
input.close();             //closing the input file
output.close();            //closing the output file
return 0;
}
void reverse_check(string &str, string &flag)
{
int len,i;
len=str.length();
if(len==0)
return;
for(i=len-2;i>=0&&(str[i]==str[i+1]);i--);
if(str[i+1]!=flag[0])
{
ans++;
flag=(flag=="+"?"-":"+");
}
str=str.substr(0,i+1);
reverse_check(str,flag);
return;
}
