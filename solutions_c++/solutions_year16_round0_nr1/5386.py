#include<iostream>
#include<stdio.h>

using namespace std;

int main()
{
	int t,i;
	cin>>t;
	for(i=1;i<=t;i++)
	{
		int a[10]={0};
		int n;
		cin>>n;
		if(n==0)
		{
			cout<<"Case #"<<i<<": INSOMNIA\n";
			continue;
		}
		else{
		int flag=0,x=1;
		while(flag==0)
		{	
			long long y,w;
			w=y=n*x;
			while(y!=0)
			{
				int z=y%10;
				y/=10;
				a[z]=1;	
			}
			int sum=a[0]+a[1]+a[2]+a[3]+a[4]+a[5]+a[6]+a[7]+a[8]+a[9];
			//cout<<sum<<"\n";
			if(sum==10)
			{
				cout<<"Case #"<<i<<": "<<w<<"\n";
				break;
			}
			x++;
		}}
		
	}
}

