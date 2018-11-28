#include<iostream>
#include<stdio.h>
using namespace std;
void solve()
{
	long n;
	cin>>n;
	int a[10]={0,0,0,0,0,0,0,0,0,0};
	long i,temp,v,k,count=0;
	for(i=1;i<100;i++)
	{
		temp=i*n;
		v=i*n;
		while(temp)
		{
			k=temp%10;
			if(a[k]!=1)
			{
			a[k]=1;
			count++;	
			}
			temp/=10;
		}
		if(count==10)
		break;
	}
	if(count==10)
	cout<<v<<"\n";
	else
	cout<<"INSOMNIA\n";
}
int main()
{
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	int t,i;
	cin>>t;
	for(i=0;i<t;i++)
	{
		cout<<"Case #"<<(i+1)<<": ";
		solve();
	}
	return 0;
}
