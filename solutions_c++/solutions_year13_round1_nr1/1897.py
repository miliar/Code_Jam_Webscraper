#include<iostream>
#include<math.h>
using namespace std;
int main()
{
int a,b,c[1001],d,i,x;
for(i=1;i<=1001;i++)
	c[i]=0;
cin>>d;
i=1;
while(i<=d)
{
   cin>>a>>b;
   while(1)
   	{
   		x=((a+1)*(a+1))-(a*a);
   		b=b-x;
   		if(b>=0)
   			c[i]++;
   		else
   			break;
   		a=a+2;
   	}
a=0;
b=0;
i++;
}
i=1;
while(i<=d)
{
cout<<"Case #"<<i<<": "<<c[i]<<"\n";
i++;
}
return 1;
}
