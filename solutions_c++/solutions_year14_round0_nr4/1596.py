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

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef double ld;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef pair<ld,ld> pdd;

#define X first
#define Y second

int main()
{
	freopen("try.in","r",stdin);
	freopen("try.out","w",stdout);
	int T;
	cin>>T;
	for (int TT=1;TT<=T;++TT)
	{
		printf("Case #%d: ",TT);
		int n;
		cin>>n;
		set<ld> a,b,c;
		for (int i=1;i<=n;++i)
		{
			ld x;
			cin>>x;
			a.insert(x);
		}
		c=a;
		for (int i=1;i<=n;++i)
		{
			ld x;
			cin>>x;
			b.insert(x);
		}
		int tot=0;
		for (auto p : b)
		{
			auto it=a.upper_bound(p);
			if (it==a.end()) break;
			++tot;
			a.erase(it);
		}
		printf("%d ",tot);
		tot=0;
		a=c;
		for (auto p : a)
		{
			auto it=b.upper_bound(p);
			if (it==b.end())
			{
				b.erase(b.begin());
				++tot;
			}
			else
			{
				b.erase(it);
			}
		}
		printf("%d\n",tot);
	}
	return 0;
}
