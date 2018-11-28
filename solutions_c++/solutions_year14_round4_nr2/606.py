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

int n;
int a[1010],L[1010],R[1010];

int main()
{
	freopen("try.in","r",stdin);
	freopen("try.out","w",stdout);
	int Test;
	cin>>Test;
	for (int T=1;T<=Test;++T)
	{
		printf("Case #%d: ",T);
		cin>>n;
		for (int i=1;i<=n;++i)
		{
			scanf("%d",&a[i]);
			L[i]=R[i]=0;
		}
		for (int i=1;i<=n;++i)
		{
			for (int j=1;j<i;++j)
				if (a[j]>a[i]) ++L[i];
			for (int j=i+1;j<=n;++j)
				if (a[j]>a[i]) ++R[i];
		}
		int ans=0;
		for (int i=1;i<=n;++i)
			ans+=min(L[i],R[i]);
		printf("%d\n",ans);
	}
	return 0;
}
