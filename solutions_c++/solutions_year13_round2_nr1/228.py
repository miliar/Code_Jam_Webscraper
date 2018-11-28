#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;
typedef __int64 int64;
int64 data[200];
int64 ini;
int n;
int main()
{
	int cas=0,cc=0;
	freopen("I:\\ip.in","r",stdin);
	freopen("I:\\output.txt","w",stdout);
	cin>>cas;
	while(cas--)
	{
		cin>>ini>>n;
		for(int i=0;i<n;i++)
		{
			cin>>data[i];
		}
		int ans=n;
		sort(data,data+n);
		int cur=0;
		 cout<<"Case #"<<++cc<<": ";
		 if(ini==1)
		 {
		  cout<<ans<<endl;
		   continue;
		}
		for(int i=0;i<n;i++)
		{
			ans=min(ans,cur+n-i);
			if(ini<=data[i])
			{
				while(ini<=data[i])
				{
					ini*=2;
					ini--;
					cur++;
				}
				ini+=data[i];
			}
			else
			  ini+=data[i];
		}
		ans=min(ans,cur);
		cout<<ans<<endl;
	}
	return 0;
}
