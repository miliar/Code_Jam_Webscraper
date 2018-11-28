#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
using namespace std;

const int T = 25;

int n, m, p;
int u[T], v[T], a[T], b[T];
int path[T];
bool vv[T], ans[T];
int f[T], g[T];
vector< pair<int, int> > e[T], _e[T];

void work()
{
	cin >> n >> m >> p;
	for (int i = 1; i <= m; ++i) 
		cin >> u[i] >> v[i] >> a[i] >> b[i];		
	for (int i = 1; i <= p; ++i)
		cin >> path[i];
	for (int i = 1; i <= m; ++i)
		ans[i] = false;
	for (int mask = 0; mask < (1 << m); ++mask) {
		for (int i = 1; i <= n; ++i) {
			e[i].clear();
			_e[i].clear();
		}
		for (int i = 1; i <= m; ++i) {
			e[u[i]].push_back(make_pair(v[i], ((mask & (1 << (i - 1))) > 0) ? a[i] : b[i]));
			_e[v[i]].push_back(make_pair(u[i], ((mask & (1 << (i - 1))) > 0) ? a[i] : b[i]));
		}
		{
		vector<int> q;		
		for (int i = 1; i <= n; ++i)
			f[i] = -1;
		q.push_back(1);
		f[1] = 0;
		vv[1] = true;
		for (int i = 0; i < q.size(); ++i) {
			int qi = q[i];
			for (int j = 0; j < e[qi].size(); ++j) {
				int t = e[qi][j].first, d = e[qi][j].second;
				if (f[t] == -1 || f[qi] + d < f[t]) {
					f[t] = f[qi] + d;					
					if (!vv[t]) {
						vv[t] = true;
						q.push_back(t);
					}
				}
			}
			vv[qi] = false;
		}
		}
		{
		vector<int> q;		
		for (int i = 1; i <= n; ++i)
			g[i] = -1;
		q.push_back(2);
		g[2] = 0;
		vv[2] = true;
		for (int i = 0; i < q.size(); ++i) {
			int qi = q[i];			
			for (int j = 0; j < _e[qi].size(); ++j) {
				int t = _e[qi][j].first, d = _e[qi][j].second;
				if (g[t] == -1 || g[qi] + d < g[t]) {
					g[t] = g[qi] + d;					
					if (!vv[t]) {
						vv[t] = true;
						q.push_back(t);
					}
				}
			}
			vv[qi] = false;
		}
		}
		/*
		cout << mask << endl;
		for (int i = 1; i <= n; ++i)
			cout << f[i] << " " << g[i] << endl;
		cout << endl;
		*/
		for (int i = 1; i <= m; ++i)
			if (f[u[i]] + (((mask & (1 << (i - 1))) > 0) ? a[i] : b[i]) + g[v[i]] == f[2])
				ans[i] = true;
	}
	int ret = 0;
	for (int i = 1; i <= p; ++i)
		if (!ans[path[i]]) {
			ret = i;
			break;
		}
	if (ret == 0)
		cout << "Looks Good To Me";
	else
		cout << path[ret];
}

int main()
{
    freopen("c1.in", "r", stdin);
    freopen("c1.out", "w", stdout);

    int t2;
    cin >> t2;
    for (int t1 = 1; t1 <= t2; ++t1) {
        printf("Case #%d: ", t1);
        work();
        printf("\n");
    }
    
    return 0;
}
