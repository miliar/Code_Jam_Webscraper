#include<iostream>
#include<cmath>
#include<cstdio>

using namespace std;
bool isPalin(int num)
{
int len=0,i,j;
j=num;
while(j>0)
{
  len++;
  j/=10;
}
if(len==1)
  return true;
else if(len==2 &&((int)(num/10)) == (num%10))
             return true;
else if(len==3 && ((int)(num/100)) == (num%10))
             return true;
return false;
}
 
int main()
{
 
 int i,j,k,l,t,a,b,count=0;
 cin>>t;
 for(i=1;i<=t;i++)
 {
    cin>>a>>b;
    count =0;
    for(j=1;j<=32 && j*j <=b; j++)
    {
       //cout<<"\n a b"<<a<<" b="<<b<<" 
       if(j*j>=a && isPalin(j*j) &&isPalin(j))
       {//cout<<"\n a b"<<a<<" b="<<b<<" num "<<j*j;
               count++;
       }
    }
    cout<<"Case #"<<i<<": "<<count<<"\n";
 }
    
    return 0;
}