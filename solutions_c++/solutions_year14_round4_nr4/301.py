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

int TESTS, CASE;

const int MAXN = 10;

int n, m;

string s[MAXN];

int ans, cnt;

int cls[MAXN];
int vis[MAXN];

struct elem {
	int next[26];
} T[MAXN*MAXN];

int calc(vector<int> &ids) {
	int sz = ids.size();
	memset(T[0].next,0,sizeof(T[0].next));
	int size = 1;
	for(int i = 0; i < sz; i++) {
		int id = ids[i];
		int v = 0;
		for(size_t j = 0; j < s[id].size(); j++) {
			int c = s[id][j];
			if(!T[v].next[c]) {
				memset(T[size].next,0,sizeof(T[size].next));
				T[v].next[c] = size++;
			}
			v = T[v].next[c];
		}
	}
	return size;
}

void go(int pos) {
	if(pos<n) {
		for(int k = 0; k < m; k++) {
			cls[pos] = k;
			go(pos+1);
		}
	} else {
		int msk = 0;
		memset(vis,0,sizeof(vis));
		int id = 0;
		for(int i = 0; i < n; i++) {
			if(!vis[i]) {
				for(int j = 0; j < n; j++) {
					if(cls[j]==cls[i]) {
						vis[j] = true;
						msk ^= cls[j]*(1<<(2*j));
					}
				}
				id++;
			}
		}
		int curr = 0;
		memset(vis,0,sizeof(vis));
		for(int i = 0; i < n; i++) {
			if(!vis[i]) {
				vector<int> ids;
				for(int j = 0; j < n; j++) {
					if(cls[j]==cls[i]) {
						ids.pb(j);
						vis[j] = true;
					}
				}
				curr += calc(ids);
			}
		}
		if(curr > ans) {
			ans = curr;
			cnt = 0;
		}
		if(curr == ans) {
			cnt++;
		}
	}
}

void solve() {
	cout << "Case #" << CASE << ": ";
	sort(s,s+n);
	
	for(int i = 0; i < n; i++) {
		for(size_t j = 0; j < s[i].size(); j++) {
			s[i][j] -= 'A';
		}
	}
	
	ans = 0;
	cnt = 0;
	go(0);
	cout << ans << ' ' << cnt << endl;
}

int main() {
	freopen("D-small.in", "r", stdin);
	freopen("D-small.out", "w", stdout);
	ios_base::sync_with_stdio(false);
	cin >> TESTS;
	for(CASE = 1; CASE <= TESTS; CASE++) {
		cin >> n >> m;
		for(int i = 0; i < n; i++) {
			cin >> s[i];
		}
		solve();
	}
}
