#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<ctime>
#include<cmath>
#include<iostream>
#include<sstream>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<bitset>
#include<string>
#include<queue>
#include<iomanip>
#include<limits>
#include<typeinfo>
#include<functional>
#include<numeric>
#include<unordered_set>
#include<unordered_map>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef double ld;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef pair<ld,ld> pdd;

#define X first
#define Y second

int m,n;
string s[10];
int u[10],a[10];

int getsize(vector<string>& F)
{
	int ans=0;
	for (int i=0;i<F.size();++i)
	{
		ans+=F[i].size();
		int t=0;
		for (int j=0;j<i;++j)
		{
			int p=0;
			while (F[i][p]==F[j][p])
			{
				++p;
				if (F[i].size()==p||F[j].size()==p) break;
			}
			t=max(t,p);
		}
		ans-=t;
	}
	return ans;
}

int main()
{
	freopen("try.in","r",stdin);
	freopen("try.out","w",stdout);
	int Test;
	cin>>Test;
	for (int T=1;T<=Test;++T)
	{
		printf("Case #%d: ",T);
		cin>>m>>n;
		for (int i=1;i<=m;++i)
			cin>>s[i];
		int p=1;
		for (int i=1;i<=m;++i)
			p*=n;
		int ans=0,cnt=0;
		for (int s=0;s<p;++s)
		{
			int t=s;
			for (int i=1;i<=n;++i)
				u[i]=0;
			for (int i=1;i<=m;++i)
			{
				a[i]=t%n+1;
				u[a[i]]=1;
				t/=n;
			}
			t=0;
			for (int i=1;i<=n;++i)
				if (!u[i]) t=1;
			if (t) continue;
			vector<string> F[5];
			for (int i=1;i<=m;++i)
				F[a[i]].push_back(::s[i]);
			int get=0;
			for (int i=1;i<=n;++i)
				get+=getsize(F[i]);
			if (get>ans)
			{
				ans=get;
				cnt=1;
			}
			else if (get==ans)
			{
				cnt++;
			}
		}
		printf("%d %d\n",ans+n,cnt);
	}
	return 0;
}
