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
string adj[10], tmp[10];
vector<int> ord;

bool bt(int p, int msk)
{
	if(msk == ((1<<n) - 1)) return 1;
	int c = ord[p];
	bool in = 0;
	Rep(i, n) if(adj[c][i] == '1' && (msk&(1<<i)) == 0)
	{
		in = 1;
		bool ok = bt(p+1, msk|(1<<i));
		if(ok == 0) return 0;
	}
	if(in == 0) return 0;
	return 1;
}

bool calc()
{
	ord.clear();
	Rep(i, n) ord.push_back(i);
	do
	{
		bool ok = bt(0, 0);
		if(!ok) return 0;
	} while (next_permutation(ALL(ord)));
	return 1;
}
int main() {
	//ios_base::sync_with_stdio(false);
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int tc , cas = 1;
	cin>>tc;
	while (tc--)
	{
		cin>>n;
		Rep(i, n) cin>>adj[i];
		int tot = 0;
		Rep(i, n) Rep(j, n)
		{
			if(adj[i][j] == '1') tot |= 1<<((i*n) + j);
		}
		int ans = 1<<30;
		Rep(i, 10) tmp[i] = adj[i];
		Rep(i, 1<<(n*n))
		{
			if(i & tot) continue;
			Rep(ii, n) Rep(j, n)
			{
				if(i & (1<<((ii*n) + j))) adj[ii][j] = '1';
			}
			bool ok = calc();
			Rep(ii, 10) adj[ii] = tmp[ii];
			if(ok)
			{
				int cnt = 0;
				Rep(ii, n*n) if(i&(1<<ii)) cnt++;
				ans = min(ans, cnt);
			}
		}
		PF("Case #%d: %d\n", cas++, ans);
	}
	return 0;
}