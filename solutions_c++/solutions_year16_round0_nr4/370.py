#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#include<iostream>
#include<vector>
using namespace std;
typedef long long LL;
int T,K,C,S;
int main()
{
	freopen("D-large.in","r",stdin);
	freopen("D-large.out","w",stdout);
	cin>>T;
	for(int I=1;I<=T;I++)
	{
		cout<<"Case #"<<I<<": ";
		cin>>K>>C>>S;
		if(S*C<K)puts("IMPOSSIBLE");
		else
		{
			vector<LL> ans;
			for(int i=0;i<K;i+=C)
			{
				LL r=0;
				for(int j=i;j<i+C;j++)
					r=r*K+(j<K?j:0);
				ans.push_back(r+1);
			}
			for(int i=0;i<ans.size();i++)
				printf("%lld%c",ans[i]," \n"[i==ans.size()-1]);
		}
	}
	return 0;
}

