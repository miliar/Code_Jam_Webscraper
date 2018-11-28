#include<iostream>
#include<cmath>
#include<cstring>
#include<cstdio>
using namespace std ;
int main()
{
int t,t1=1;
FILE *p ;
p=fopen("output.txt","w") ;
cin>>t ;
while(t1<=t)
{
int a,b,k,ct=0,i,j ;
cin>>a>>b>>k ;
//cout<<(a&b) ;
for(i=0;i<a;i++)
{
for(j=0;j<b;j++)
{
int temp=i&j ;
    if(temp<k)
    {
    //cout<<i<<" "<<j<<"\n" ;
    ct++ ;
    }
}
}
fprintf(p,"Case #%d: %d\n",t1,ct) ;
//cout<<"Case #"<<t1<<": "<<ct<<"\n";
t1++ ;
}
return 0 ;
}
