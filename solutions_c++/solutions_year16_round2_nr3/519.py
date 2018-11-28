#include <iostream>
#include <vector>
#include <fstream>
#include <queue>
#include <algorithm>
#include <list>
#include <ctime>
#include <cstdio>
#include <stack>
#include <cstring>
#include <climits>
#include <cmath>
#include <string>
#include <functional>
#include <sstream>
#include <map>
#include <set>

#pragma comment(linker, "/STACK:100000000000000")

using namespace std;
#define     For(i,a,b)        for (int i=a; i<b; i++)
#define     Rep(i,a)          for (int i=0; i<a; i++)
#define     ALL(v)            (v).begin(),(v).end()
#define     Set(a,x)          memset((a),(x),sizeof(a))
#define     EXIST(a,b)        find(ALL(a),(b))!=(a).end()
#define     Sort(x)           sort(ALL(x))
#define     UNIQUE(v)         Sort(v); (v).resize(unique(ALL(v)) - (v).begin())
#define     MP                make_pair
#define     SF                scanf
#define     PF                printf
#define     MAXN              1001
#define     MOD               1000000007
#define     Dbug              cout<<"";
#define     EPS               1e-8
#define     timestamp(x)      printf("Time : %.3lf s.\n", clock()*1.0/CLOCKS_PER_SEC)
typedef long long ll;
typedef pair<int, int> pii;
int n;
string s[MAXN], t[MAXN];
int sameF[MAXN], sameS[MAXN], dp[1<<17];

int rec(int msk)
{
	if(msk == (1<<n) - 1) return 0;
	if(~dp[msk]) return dp[msk];
	int ans = 0, fake = 0, tmsk = msk;
	Rep(i, n) if(!(msk & (1<<i)))
	{
		if((sameF[i] & msk) && (sameS[i] & msk)) 
		{
			fake++;
			tmsk |= 1<<i;
		}
	}
	Rep(i, n) if(!(tmsk & (1<<i)))
	{
		int tmp = rec(tmsk | 1<<i);
		ans = max(ans, tmp);
	}
	ans += fake;
	return dp[msk] = ans;
}

int main() {
	//ios_base::sync_with_stdio(false);
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int tc, cas = 1;
	cin>>tc;
	while (tc--)
	{
		PF("Case #%d: ", cas++);
		cin>>n;
		Rep(i, n) cin>>s[i]>>t[i];
		Rep(i, n)
		{
			sameF[i] = sameS[i] = 0;
			Rep(j, n) if(i!=j)
			{
				if(s[i] == s[j]) sameF[i] |= 1<<j;
				if(t[i] == t[j]) sameS[i] |= 1<<j;
			}
		}
		Set(dp, -1);
		int ans = rec(0);
		cout<<ans<<endl;
	}
	return 0;
}