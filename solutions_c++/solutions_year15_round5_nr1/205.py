#define _USE_MATH_DEFINES
#include<iostream>
#include<cmath>
#include<cstdio>
#include<string>
#include<vector>
#include<queue>
#include<deque>
#include<map>
#include<cctype>
#include<algorithm>
#include<cstring>
#include<set>

using namespace std;

typedef pair<int, int> pii;
typedef map<pii, int> mpii;
#define mp(x, y) make_pair(x, y)

const int MAX = 1e6 + 100;

vector<vector<int> > g;
int S[MAX];

vector<int> t;
int nn;

int sum (int r)
{
	int result = 0;
	for (; r >= 0; r = (r & (r+1)) - 1)
		result += t[r];
	return result;
}

void inc (int i, int delta)
{
	for (; i < nn; i = (i | (i+1)))
		t[i] += delta;
}

int sum (int l, int r)
{
	return sum (r) - sum (l-1);
}

vector<pii> vs;

void dfs(int v, int l, int r)
{
	vs.push_back(mp(min(l, S[v]), max(r, S[v])));
	for (int i=0;i<g[v].size();++i)
		dfs(g[v][i], min(l, S[v]), max(r, S[v]));
}

int solve()
{
	g.clear();
	int N, D, As, Cs, Rs, M, Am, Cm, Rm;
	cin >> N >> D >> S[0] >> As >> Cs >> Rs >> M >> Am >> Cm >> Rm;
	g.resize(N);
	for (int i=1;i<N;++i) {
		S[i] = (1ll * S[i-1] * As + Cs) % Rs;
		M = (1ll * M * Am + Cm) % Rm;
		g[M%i].push_back(i);
	}
	vs.clear();
	dfs(0, S[0], S[0]);
	sort(vs.begin(), vs.end());
	nn = 2000001;
	t.assign (nn, 0);
	for (int i=0;i<vs.size();++i)
		inc(vs[i].second, 1);
	int res = 0;
	for (int i=0;i<vs.size();++i) {
		res = max(res, sum(vs[i].first, vs[i].first+D));
		inc(vs[i].second, -1);
	}
	return res;
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for (int t=1;t<=T;++t)
		printf("Case #%d: %d\n", t, solve());
	return 0;
}
