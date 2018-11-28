#include<iostream>
#include<string.h>
using namespace std;
int main()
{
int t;
cin>>t;
int r=t;
while(t>0)
{
char A[2000],B[2000],C[2000];
cin>>A;
int n=strlen(A);
B[1000]=A[0];
int a=999;
int b=1001;
char s=A[0];
for(int i=1;i<n;i++)
{
//cout<<"s="<<s<<endl;
if((int)A[i]>=(int)s)
{
B[a]=A[i];
//cout<<"a="<<a<<endl;
a--;
s=A[i];
}
else
{
B[b]=A[i];
//cout<<"b="<<b<<endl;
b++;
}
}
int g=0;
for(int i=a+1;i<=b-1;i++)
{
    //cout<<B[i];
C[g]=B[i];
g++;
//cout<<"g="<<g<<endl;
}
C[g]='\0';
cout<<"Case #"<<r-t+1<<": "<<C<<endl;
t--;
}
return 0;
}


