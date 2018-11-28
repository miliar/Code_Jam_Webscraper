#include<iostream>
#include<math.h>
#include<stdlib.h>
#define pi 3.14159
using namespace std;

int main()
{
long double r,t;
int T,count=0,ans[10000];
cin>>T;
for(int i=0;i<T;i++)
{
count=0;
cin>>r;
//cin.ignore(256,' ');
cin>>t;
//cin.ignore(256,'\n');
long double a=r;
long double area=pi*(2*r+1);
while(area<=t*pi)
{	count++;
	a=a+2;
	area+=pi*(2*a+1);
}
ans[i]=count;
}
for(int i=0;i<T;i++)
cout<<"Case #"<<(i+1)<<": "<<ans[i]<<"\n";
return 0;
}
