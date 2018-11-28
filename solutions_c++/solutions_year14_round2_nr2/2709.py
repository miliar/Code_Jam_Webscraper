#include<iostream>
using namespace std;

int main()
{
freopen("B-small-attempt0.in", "r", stdin);
freopen("output.txt", "w", stdout);
int test;
cin>>test;
for(int l=1;l<=test;l++)
{
cout<<"Case #"<<l<<": ";
int a,b,k;
cin>>a>>b>>k;
unsigned long int cnt=a+b-1;
int i,j;
for(i=1;i<a;i++)
{
 for(j=1;j<b;j++)
 {
  if((i&j)<k)
  {
  //cout<<i<< " "<<j<<endl;
  cnt++;
  }
  }
}
cout<<cnt<<endl; 
}
return 0;
}