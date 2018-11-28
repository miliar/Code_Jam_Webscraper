#include<iostream>
#include<math.h>
using namespace std;
int isPali(int n)
{
	int t=n,d,r=0;
	while(n!=0)
	{
		d=n%10;
		r=r*10+d;
		n/=10;
	}
	if(t==r)
		return 1;
	else
		return 0;
}
int main()
{
	int n,a,b,j,i,p,s,c[100];
	float r;
	cin>>n;
	for(i=0;i<n;i++)
		c[i]=0;
	for(i=0;i<n;i++)
	{
		cin>>a>>b;
		for(j=a;j<=b;j++)
		{
			p=isPali(j);
			r=sqrt(j);
			if((r-(int)r)!=0)
				s=0;
			else
			s=isPali(sqrt(j));
			if(p==1&&s==1)
			{
				c[i]++;
			}
		}
	}
	for(i=0;i<n;i++)
		cout<<"Case #"<<i+1<<": "<<c[i]<<"\n";
	return 0;
}
			
		
