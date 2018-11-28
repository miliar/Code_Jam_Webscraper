#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <map>
#include <set>
#include <vector>
using namespace std;

#define mp(x, y) make_pair((x), (y))

typedef long long ll;

int t;

int n;
ll d;
vector<vector<int> > next;
vector<ll> s;

int ans;
int cur;

ll l, r;

void dfs(int v)
{
	if(s[v]<l || s[v]>r) return;
	cur++;
	for(int i=0; i<next[v].size(); i++) {
		int s=next[v][i];
		dfs(s);
	}
}

ll s0, as, cs, rs;
ll m0, am, cm, rm;


int main()
{
	scanf("%d", &t);

for(int q=1; q<=t; q++) {
	scanf("%d%lld", &n, &d);
	scanf("%lld%lld%lld%lld", &s0, &as, &cs, &rs);
	scanf("%lld%lld%lld%lld", &m0, &am, &cm, &rm);

	next.clear();
	next.resize(n);
	s.clear();
	s.resize(n);
	s[0]=s0;
	for(int i=1; i<n; i++) s[i]=(s[i-1]*as+cs)%rs;

	for(int i=1; i<n; i++) {
		m0=(m0*am+cm)%rm;
		next[m0%i].push_back(i);
	}

	ans=0;
	for(l=max(s[0]-d, 0LL); l<=s[0]; l++) {
		r=l+d;
		cur=0;
		dfs(0);
		ans=max(ans, cur);
	}

	printf("Case #%d: %d\n", q, ans);
}

	return 0;
}
