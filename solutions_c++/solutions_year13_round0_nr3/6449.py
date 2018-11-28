#include<iostream>
#include<string.h>
#include<stdio.h>
#include<math.h>
using namespace std;

main()
{
   unsigned long int n,temp,k,flag,r,count,i,j,t;
cin>>t;
unsigned long int a[t][2];
    for(i=0;i<t;i++)
    cin>>a[i][0]>>a[i][1];

    for(i=0;i<t;i++)
    {
        count=0;
        for(j=a[i][0];j<=a[i][1];j++)
        {


n=j;
temp=n;
k=0;flag=0;
while(n>0)
{
    k=(k*10)+n%10;
    n/=10;


}
if(temp==k)
flag++;
if(flag==1){
r=sqrt(temp);
if(r*r==temp)
{temp=r;
k=0;
while(r>0)
{
    k=(k*10)+r%10;
    r/=10;


}
if(temp==k)
flag++;
}
}
if(flag==2)count++;


}
cout<<"Case #"<<i+1<<": "<<count<<"\n";
    }
}
