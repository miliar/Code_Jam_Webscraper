#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
	long long t,n,i,ans,c,temp,k;
	freopen("input.in","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>t;
	for(c=1;c<=t;c++)
	{
		long long a[10];
		cin>>n;
		ans=0;
		k=1;
		for(i=0;i<=9;i++)
		a[i]=0;
		if(n==0)
		 cout<<"Case #"<<c<<": INSOMNIA"<<endl;
		else
		{
			while(ans<10)
		    {
			 temp=k*n;
			 while(temp>0)
			 {
				i=temp%10;
				if(a[i]==0)
				{
					a[i]=1;
					ans++;
				}
				temp/=10;
			 } 
			k++;
		    }
		    cout<<"Case #"<<c<<": "<<n*(k-1)<<endl;
		}
	}
}
