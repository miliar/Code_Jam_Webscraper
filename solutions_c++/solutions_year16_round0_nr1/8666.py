#include<iostream>
#include<math.h>
using namespace std;
void generate_stepvalues(int n,int x,int *a)
{
	for(int i=0;i<x;i++)
	{
		int temp = pow(10,i+1);
		a[i] = n%temp;
	}
	for(int i=x-1;i>=0;i--)
	{
		int temp = pow(10,i);
		a[i] = (a[i] - a[i-1])/temp;
	}
}
void generate_eachvalues(int x,int *a,int*b)
{
	for(int i=0;i<x;i++)
	{
		for(int j=0;j<10;j++)
		{
			if(a[i]==j)
			{
				b[j]++;
				break;
			}
		}
	}
}
int calculatex(int n)
{
	int x = 1;
	int power = pow(10,x);
	while(n%power!=n)
	{
		x++;
		power = pow(10,x);
	}
	return x;
}
bool check(int *b)
{
	for(int j=0;j<10;j++)
	{
		if(b[j]==0)
		{
			return false;
		}
	}
		return true;
}
int main()
{
	int t;
	cin>>t;
	for(int k=0;k<t;k++)
	{
		int n,i=1,m;
		cin>>n;
		if(n==0)
		{
			cout<<"Case #"<<k+1<<":"<<" INSOMNIA"<<"\n";
			continue;
		}
		int b[10];
		for(int j=0;j<10;j++)
		{
			b[j]=0;
		}	
		while(!check(b))
		{
			m=i*n;
			int x = calculatex(m);
			int a[x];
			generate_stepvalues(m,x,a);
			generate_eachvalues(x,a,b);
			i++;
		}
		cout<<"Case #"<<k+1<<":"<<" "<<m<<"\n";
	}
}