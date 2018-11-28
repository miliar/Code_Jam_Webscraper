#include<iostream>
#include<cstdio>
#include<cmath>
using namespace std;
int a[10000];
int main()
{
	int t,cas=0;
	cin>>t;
	for(cas=0;cas<t;cas++)
	{
		int highest1=0,n;
		cin>>n;
		for(int i=1;i<=n;i++)
		{
			cin>>a[i];
			highest1=max(highest1,a[i]);
		}
		int ans=highest1;
		for(int i=0;i<highest1;i++)
		{
			int now=0,highest2=0;
			for(int j=0;j<n;j++)
			{
				if(a[j+1]>i+1)
				{
					now += (a[j+1] / (i+1))+((a[j+1]%(i+1)==0)?0:1)-1;
					highest2=max(highest2,i+1);
				}
				else highest2=max(highest2,a[j+1]);
			}
			now = now+highest2;
			if(now<ans)
			ans=now;
		}
		cout<<"Case #"<<cas+1<<": "<<ans<<endl;
	}
	return 0;
}
