#include<iostream>
#include<cstdlib>
#include<cmath>
using namespace std;
int a[50];
long long prime_check(long long a)
{
	long long i;
	long long lim=sqrt(a);
	for(i=2;i<lim;i++)
	{
		if(a%i==0)
			return i;
	}
	return 1;
}
int jam_check(int n,int c,int o)
{
	int i,flag=1,j;
	long long arr[9],t;
	for(i=0;i<9;i++)
	{
		t=a[n-1];
		for(j=n-2;j>=0;j--)
			t=t+pow((i+2),n-j-1)*a[j];
		arr[i]=prime_check(t);
		if(arr[i]==1)
		{
			flag=0;
			break;
		}
	}
	if(flag==0)
		return 0;
	if(o==0)
		cout<<"Case #"<<c<<":"<<endl;
	for(i=0;i<n;i++)
		cout<<a[i];
	for(i=0;i<9;i++)
		cout<<" "<<arr[i];
	cout<<endl;
	return 1;
}
void bitStringGen(int n)
{
	static int num=0;
	int i,j=0;
	for(i=1;i<n-1;i++,j++)
	{
		a[i]=num&(int)(pow(2,j));
		if(a[i]!=0)
			a[i]=1;
	}
	num=num+1;
}
int main()
{
	int t;
	int c=0,o;
	cin>>t;
	while(t--)
	{
		o=0;	
		c++;
		int n,j,i;
		cin>>n;
		cin>>j;
		a[0]=1;
		a[n-1]=1;
		while(j!=0)
		{
			bitStringGen(n);
			if(jam_check(n,c,o)==1)
			{
				o=1;
				j--;
			}
		}
		o=0;
	}
	return 0;
}
