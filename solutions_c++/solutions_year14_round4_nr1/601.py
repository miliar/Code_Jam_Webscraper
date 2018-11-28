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

int n,s;
int a[10010];


int main()
{
	freopen("try.in","r",stdin);
	freopen("try.out","w",stdout);
	int Test;
	cin>>Test;
	for (int T=1;T<=Test;++T)
	{
		printf("Case #%d: ",T);
		cin>>n>>s;
		for (int i=1;i<=n;++i)
		{
			cin>>a[i];
		}
		sort(a+1,a+n+1);
		int i=1,j=n,t=0,ans=0;
		while (i<=j)
		{
			if (a[i]+a[j]<=s)
			{
				++ans;
				i++;
				j--;
				continue;
			}
			j--;
			++ans;
		}
		printf("%d\n",ans);
	}
	return 0;
}
