#include<stdio.h>
#include<fstream>
#include<string.h>
using namespace std;
int main()
{
int t,i=1;
ifstream in("input.txt");
ofstream out("output.txt");
in>>t;
for(i=1;i<=t;i++)
{
    int j;
    char s[1000],cc;
    in>>s;
int n=strlen(s),change=0;
for(j=0;j<n-1;j++)
{
if(s[j]!=s[j+1])
    change++;
}
if(s[n-1]=='-')
    change=change+1;
out<<"Case #"<<i<<": "<<change<<endl;
}
return 0;
}
