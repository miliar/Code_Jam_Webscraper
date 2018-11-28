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
    int j,k;
    char s[10000],cc;
    in>>s;
    int n=strlen(s);
char a[n];
for(k=0;k<n;k++)
{
    char temp[n];
if(k==0)
    a[k]=s[k];
else if(a[0]<=s[k])
{
strcpy(temp,a);
    a[0]=s[k];
    for(j=1;j<=k;j++)
{
a[j]=temp[j-1];
}
}
else
{
a[k]=s[k];
}
}
for(k=0;k<n;k++)
    s[k]=a[k];
out<<"Case #"<<i<<": "<<s<<endl;
}
return 0;
}
