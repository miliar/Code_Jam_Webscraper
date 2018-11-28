#include <bits/stdc++.h>
using namespace std;
#define MAXN 1000005
//int ans[MAXN];
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	/*memset(ans,-1,sizeof(ans));
	ans[0]=-1;
	int mx=-1;
	for(int i=1;i<=1000000;i++)
	{
		set<int> s;

		int n1=i;
		while(n1)
		{
			s.insert(n1%10);
			n1/=10;
		}
		int cur=i;
		while((int)s.size()<10)
		{
			cur+=i;
			mx=max(mx,cur);
			n1=cur;
			while(n1)
		{
			s.insert(n1%10);
			n1/=10;
		}

		}
		ans[i]=cur;
		
	}
	cout<<mx<<endl;*/

	int t;
	cin>>t;
	string str="Case #";
	int cnt=1;
	while(t--)
	{
		int n;
		cin>>n;
		int ans=0;
		if(n==0)
		{
			ans=0;
		}
		else
		{
			set<int> s;

		int n1=n;
		while(n1)
		{
			s.insert(n1%10);
			n1/=10;
		}
		int cur=n;
		while((int)s.size()<10)
		{
			cur+=n;
			
			n1=cur;
			while(n1)
		{
			s.insert(n1%10);
			n1/=10;
		}

		}
		ans=cur;
		}
		if(ans==0)
		{
			cout<<str<<cnt<<": "<<"INSOMNIA"<<endl;
		}
		else cout<<str<<cnt<<": "<<ans<<endl;
		cnt++;
	}

	return 0;
}