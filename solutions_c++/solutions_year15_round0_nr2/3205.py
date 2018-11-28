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
#include<list>
#include<iomanip>
#include<limits>
#include<typeinfo>
#include<functional>
#include<numeric>
#include<complex>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef pair<ld,ld> pdd;

#define X first
#define Y second

int n;
int p[1010];

int main()
{
	freopen("try.in","r",stdin);
	freopen("try.out","w",stdout);
	int Test;
	cin>>Test;
	for (int T=1;T<=Test;++T)
	{
		cin>>n;
		for (int i=1;i<=n;++i)
			scanf("%d",&p[i]);
		int ans=1000;
		for (int i=1;i<=1000;++i)
		{
			int t=0;
			for (int j=1;j<=n;++j)
				if (p[j]>i) t+=(p[j]-1)/i;
			ans=min(ans,t+i);
		}
		printf("Case #%d: %d\n",T,ans);
	}
	return 0;
}
