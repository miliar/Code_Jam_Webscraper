#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;
int main()
{
	int t;
	cin>>t;
	int k=1;
	while(t--)
	{
		int d,ans=0;
		cin>>d;
		vector<int> a;
		a.push_back(0);
		for(int i=0;i<d;i++)
		{
			int tmp;
			cin>>tmp;
			ans=max(ans,tmp);
			a.push_back(tmp);
		}
		int res=ans,mx2,total_time;
		/*
		while(1)
		{
			sort(a.begin(),a.end(),greater<int>());
			int mx2=a[0],total_time;
			total_time=res+mx2;
			ans=min(ans,total_time);
			if(mx2==1 || mx2==0)
			{
				break;
			}
			if(mx2%2==0)
			{
				a[0]/=2;
				a.push_back(a[0]);
			}
			else
			{
				a[0]=(a[0]/2)+1;
				a.push_back(mx2/2);
			}
			res++;
		}*/
		for(int i=1;i<=ans;i++)
		{
			mx2=0,total_time=0;
			for(int j=1;j<=d;j++)
			{
				if(a[j]>i)
				{
					mx2+=(a[j]/i);
					if(a[j]%i!=0)
					{
						mx2+=1;
					}
					mx2-=1;
					total_time=max(total_time,i);
				}
				else
				{
					total_time=max(total_time,a[j]);
				}
			}
			mx2+=total_time;
			if(mx2<res)
			{
				res=mx2;
			}
		}
		cout<<"Case #"<<k<<": "<<res<<"\n";
		k++;
	}
	return 0;
}