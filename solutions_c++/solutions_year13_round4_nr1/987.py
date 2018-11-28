#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <iostream>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>
using namespace std;

typedef long long LL;
typedef pair<int,int> PII;
typedef vector<int> VI;

#define PB push_back
#define MP make_pair
#define clr(a,b)    (memset(a,b,sizeof(a)))
#define rep(i,a)    for(int i=0; i<(int)a.size(); i++)

const int INF = 0x3f3f3f3f;
const double eps = 1E-8;

map<int, int> hash;
int T;
int n, m;
struct st
{
	int st, ed, c;
	int hst, hed;
}p[1010];

int arr[2010];
int cnt,tot;

int seg[2010];

int main()
{
	freopen("C:\\A-small-attempt0.in","r",stdin);
	freopen("C:\\out.txt","w",stdout);

	scanf("%d",&T);
	int cas = 1;
	while(T--)
	{
		scanf("%d%d",&n,&m);
		cnt = 0;
		hash.clear();
		LL origin = 0, cur = 0;

		for(int i=1; i<=m; i++)
		{
			scanf("%d%d%d",&p[i].st, &p[i].ed, &p[i].c);
			LL k = p[i].ed - p[i].st;
			origin += 1ll * p[i].c * (2ll*n + 1ll - k) * k / 2ll;

			arr[++cnt] = p[i].st;
			arr[++cnt] = p[i].ed;
		}
		sort(arr+1, arr+1+cnt);
		tot = unique(arr+1, arr+1+cnt) - (arr + 1);
		for(int i=1; i<=tot; i++)
			hash.insert(MP(arr[i], i ));

		for(int i=1; i<=m; i++)
		{
			p[i].hst = hash[p[i].st ];
			p[i].hed = hash[p[i].ed ];
		}

		clr(seg, 0);
		for(int i=1; i<=m; i++)
			for(int j=p[i].hst; j<=p[i].hed - 1; j++)
				seg[j]+=p[i].c;

		int end = tot - 1;
		for(int i=1; i<=end; i++)
		{
			if(seg[i] == 0)	continue;

			while(seg[i] > 0)
			{
				int s = i, e = i;
				while(seg[e] > 0) e++;
				e--;

				int st = arr[s], ed = arr[e + 1];
				int k = ed - st;
				cur += (2ll*n + 1ll - k) * k / 2ll;

				for(int j=s; j<=e; j++)
					seg[j]--;
			}
		}
		printf("Case #%d: %I64d\n",cas++,origin - cur);
	}
	return 0;
}
