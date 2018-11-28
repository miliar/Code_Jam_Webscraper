#include <bits/stdc++.h>
using namespace std;
int main()
{
	freopen("B.inp","r",stdin);
	freopen("B.out","w",stdout);
	int test,cur,ans;
	string cake;
	cin>>test;
	for(int testcase=1;testcase<=test;testcase++)
	{
		cin>>cake;
		cur=1;
		ans=0;
		for(int j=cake.length()-1;j>=0;j--)
		{
			if(cur==1&&cake[j]=='+') continue;
			if(cur==0&&cake[j]=='-') continue;
			cur=1-cur;
			ans++;
		}
		cout<<"Case #"<<testcase<<": "<<ans<<'\n';
	}
}