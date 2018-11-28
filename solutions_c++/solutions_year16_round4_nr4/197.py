#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#include <vector>
#include <queue>

using namespace std;
const int inf = 1000000007;
const int N = 30;
int n, b[N], c[N];
char str[N][N] , can[N][N];
vector<pair<int , int> > p;

bool dfs(int idx , int people, int machine) {
	if (idx == n) return true;
	for (int i = 0 ; i < n ; i ++) {
		if ((1 << i) & people) continue;
		bool ok = false;
		for (int j = 0 ; j < n ; j ++) {
			if ((1 << j) & machine) continue;
			if(can[i][j] == '1') {
				ok = true;
				if (!dfs (idx + 1, people + (1 << i), machine + (1 << j))) {
					return false;
				}
			}
		}
		if (!ok) return false;
	}
	return true;
}
int main () {
	// freopen ("input.txt", "r" , stdin);
	// freopen ("output.txt", "w", stdout);
	int t, cas = 0;scanf ("%d" , &t);	
	while (t --) {
		scanf ("%d" , &n);
		for (int i = 0 ; i < n ; i ++) {
			scanf ("%s" , str[i]);
		}
		p.clear ();
		for(int i = 0 ; i < 1 << (n * n) ; i ++) {
			int ret = 0;
			for(int j = 0 ; j < n * n ; j ++) {
				if ((1 << j) & i) {
					ret ++;
				}
			}
			p.push_back(make_pair(ret, i));
		}
		sort(p.begin(), p.end());
		for(int ii = 0 ; ii < 1 << (n * n) ; ii ++) {
			int i = p[ii].second;
			int ret = 0;
			for(int j = 0 ; j < n * n ; j ++) {
				if ((1 << j) & i) {
					can[j / n][j % n] = '1';
					ret ++;
				}
				else can[j / n][j % n] = str[j / n][j % n];
			}
			for(int j = 0 ; j < n ; j ++) {
				b[j] = j;
			}
			bool find = true;

			if (dfs(0, 0, 0)) {
				printf ("Case #%d: %d\n" , ++ cas, ret);
				break;
			}
		}



	}
	return 0;
}