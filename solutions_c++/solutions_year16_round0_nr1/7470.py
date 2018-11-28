#include<bits/stdc++.h>
#define rep(i,a,b) for(i=a;i<b;++i)
#define m 1000000007
#define rev(i,a,b) for(i=a;i>b;--i)
#define ll long long int
using namespace std;
int main()
{
	ll time,temp,x,t,n,i,flag[10],count;
	cin>>t;
	time=1;
	while(t--)
	{
		cin>>n;
		if(n==0)
		{
			cout<<"Case #"<<time<<": "<<"INSOMNIA"<<endl;
			time++;
		}
		else
		{
			rep(i,0,10)
				flag[i]=0;
			count=0;
			i=1;
			while(count!=10)
			{
				temp=n*i;	
				while(temp)
				{
					x=temp%10;
					temp=temp/10;
					if(flag[x]==0)
					{
						flag[x]=1;
						count++;
					}
				}
				i++;
			}
			cout<<"Case #"<<time<<": "<<n*(i-1)<<endl;
			time++;
		}
	}
	return 0;
}
