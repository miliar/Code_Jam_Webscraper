#include<iostream>
using namespace std;

int main()
{

int t,p,q,r,x,y;
cin>>t;

for(int i=0;i<t;i++)
{

q=x=y=r=0;
cin>>p;
string a;
cin>>a;

char b;
for(int j=0;j<p+1;j++)
{
    b=a[j];  
 y=b-'0';

  if(j>q)
    {
     x=j-q;
     r+=x;
     q+=x;
    }   
q=q+y;

}

cout<<"Case #"<<i+1<<": "<<r<<endl;

}
return 0;
}
