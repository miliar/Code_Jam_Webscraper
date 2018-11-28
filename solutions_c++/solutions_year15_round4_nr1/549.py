#include <iostream>
#include <fstream>
#include <cstdio>
#include <iomanip>
#include <sstream>
#include <cstring>
#include <string>
#include <cmath>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <numeric>
#include <utility>
#include <functional>
#include <limits>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int ui;
typedef pair<int,int> pii;
typedef vector<vector<int> > graph;

const double pi = acos(-1.0);

#define oned(a, x1, x2) { cout << #a << ":"; for(int _i = (x1); _i < (x2); _i++){ cout << " " << a[_i]; } cout << endl; }
#define twod(a, x1, x2, y1, y2) { cout << #a << ":" << endl; for(int _i = (x1); _i < (x2); _i++){ for(int _j = (y1); _j < (y2); _j++){ cout << (_j > y1 ? " " : "") << a[_i][_j]; } cout << endl; } }

#define mp make_pair
#define pb push_back
#define fst first
#define snd second

const int MAXN = 105;

int n, m;
char a[MAXN][MAXN];
int dx[128], dy[128];
char p[] = {'>','<','^','v'};

void solve() {
	dx['<'] = dx['>'] = 0;
	dx['v'] = +1;
	dx['^'] = -1;
	dy['v'] = dy['^'] = 0;
	dy['>'] = +1;
	dy['<'] = -1;
	int ans = 0;
	for(int i = 0; i < n; i++) {
		for(int j = 0; j < m; j++) {
			int c = a[i][j];
			if(c!='.') {
				bool ok = false;
				int x = i, y = j;
				while(true) {
					x += dx[c];
					y += dy[c];
					if(!(x>=0 && x<n && y>=0 && y<m)) {
						break;
					}
					if(a[x][y]!='.') {
						ok = true;
						break;
					}
				}
				if(!ok) {
					ans++;
					for(int k = 0; k < 4 && !ok; k++) {
						c = p[k];
						int x = i, y = j;
						while(true) {
							x += dx[c];
							y += dy[c];
							if(!(x>=0 && x<n && y>=0 && y<m)) {
								break;
							}
							if(a[x][y]!='.') {
								ok = true;
								break;
							}
						}
					}
				}
				if(!ok) {
					printf("IMPOSSIBLE\n");
					return;
				}
			}
		}
	}
	printf("%d\n", ans);
}

int main() {
	freopen("A-input.in", "r", stdin);
	freopen("A-output.out", "w", stdout);
	int t; scanf("%d", &t);
	for(int c = 1; c <= t; c++) {
		scanf("%d %d", &n, &m);
		for(int i = 0; i < n; i++) {
			scanf("%s", a[i]);
		}
		printf("Case #%d: ", c);
		solve();
	}
}
