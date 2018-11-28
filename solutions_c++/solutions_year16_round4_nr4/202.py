#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cassert>
using namespace std;
typedef long long ll;
typedef double R;
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define FOR(i, s, t) for(i = (s); i < (t); i++)
#define RFOR(i, s, t) for(i = (s)-1; i >= (t); i--)

const int MAXN = 52;

vector<int> e[MAXN];
vector<int> q;
vector<pair<int, int> > v;
bool vis[MAXN];

pair<int, int> operator+(const pair<int, int> &a, const pair<int, int> &b) {
	return mp(a.fi + b.fi, a.se + b.se);
}

void bfs(int i){
	int h, t;
	h = t = 0;
	q.clear();
	vis[i] = true;
	q.pb(i);
	t++;
	while(h < t){
		i = q[h++];
		for(int j = 0; j < e[i].size(); j++){
			int k = e[i][j];
			if(!vis[k]){
				vis[k] = true;
				q.pb(k);
				t++;
			}
		}
	}
}

int dfs(const vector<pair<int, int> > &v){
	int m = v.size();
	int n = 0;
	int ret;
	int i, j, k;
	for(i = 0; i < m; i++)
		n += v[i].fi;
	ret = n*n;
	for(i = 0; i < 1<<(m-1); i++){
		pair<int, int> x = v[0];
		for(j = 0; j < m-1; j++)
			if(1<<j&i)
				x = x + v[j+1];
		if(x.fi == x.se){
			vector<pair<int, int> > t;
			for(j = 0; j < m-1; j++)
				if(!(1<<j&i))
					t.pb(v[j+1]);
			ret = min(ret, x.fi*x.fi + dfs(t));
		}
	}
	return ret;
}

int main(){
#ifdef LOCAL
	//freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);
#endif
	int T, i0;
	scanf("%d", &T);
	for(i0 = 1; i0 <= T; i0++){
		int n, m;
		int i, j, k;
		scanf("%d", &n);
		m = 0;
		for(i = 0; i < n; i++){
			for(j = n; j < 2*n; j++){
				char s[2];
				scanf("%1s", s);
				if(s[0] == '1'){
					e[i].pb(j);
					e[j].pb(i);
					m++;
				}
			}
		}
		memset(vis, 0, sizeof vis);
		for(i = 0; i < 2*n; i++)
			if(!vis[i]){
				bfs(i);
				pair<int, int> a(0, 0);
				for(j = 0; j < q.size(); j++)
					if(q[j] < n)
						a.fi++;
					else
						a.se++;
				//printf("%d %d\n", a.fi, a.se);
				v.pb(a);
			}
		int ans = dfs(v) - m;
		printf("Case #%d: %d\n", i0, ans);
		for(i = 0; i < n*2; i++)
			e[i].clear();
		v.clear();
	}
	return 0;
}
