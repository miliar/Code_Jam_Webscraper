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

const int MAXN = 205;
const int MAXW = 1005;

int n, cnt[MAXN];
string s[MAXN][MAXW];
int x[MAXN][MAXW];

set<string> all;
map<string,int> id;

set<int> as, bs, aw, bw, rest;

int intersection(set<int> &a, set<int> &b) {
	int num = 0;
	for(set<int>::iterator it = a.begin(); it != a.end(); it++) {
		if(b.find(*it)!=b.end()) {
			num++;
		}
	}
	return num;
}

set<int> rem;

int done[10000];

set<int> tmp;

void solve() {
	all.clear();
	for(int i = 0; i < n; i++) {
		for(int j = 0; j < cnt[i]; j++) {
			all.insert(s[i][j]);
		}
	}
	int num = 0;
	for(set<string>::iterator it = all.begin(); it != all.end(); it++) {
		id[*it] = num++;
	}
	for(int i = 0; i < n; i++) {
		for(int j = 0; j < cnt[i]; j++) {
			x[i][j] = id[s[i][j]];
		}
	}
	
	as.clear();
	for(int j = 0; j < cnt[0]; j++) {
		as.insert(x[0][j]);
	}
	bs.clear();
	for(int j = 0; j < cnt[1]; j++) {
		bs.insert(x[1][j]);
	}
	
	memset(done,0,sizeof(done));
	int tot = 0;
	for(set<int>::iterator it = as.begin(); it != as.end(); it++) {
		if(bs.find(*it)!=bs.end()) {
			tot++;
			done[*it] = true;
		}
	}

	int add = (n==2 ? 0 : 1e9);
	for(int msk = 4; msk < (1<<n); msk += 4) {
		aw.clear();
		bw.clear();
		tmp.clear();
		for(int i = 2; i < n; i++) {
			if(msk&(1<<i)) {
				for(int j = 0; j < cnt[i]; j++) {
					aw.insert(x[i][j]);
				}
			} else {
				for(int j = 0; j < cnt[i]; j++) {
					bw.insert(x[i][j]);
				}
			}
		}
		int num = 0;
		for(set<int>::iterator it = aw.begin(); it != aw.end(); it++) {
			if(!done[*it] && (bs.find(*it)!=bs.end() || bw.find(*it)!=bw.end())) {
				tmp.insert(*it);
				num++;
			}
		}
		for(set<int>::iterator it = bw.begin(); it != bw.end(); it++) {
			if(!done[*it] && (as.find(*it)!=as.end() && tmp.find(*it)==tmp.end())) {
				num++;
			}
		}
		if(num < add) {
			add = num;
		}
	}
	printf("%d\n", tot+add);
}

int main() {
	freopen("C-input.in", "r", stdin);
	freopen("C-output.out", "w", stdout);
	int t; scanf("%d", &t);
	for(int c = 1; c <= t; c++) {
		cin >> n;
		cin.ignore();
		for(int i = 0; i < n; i++) {
			string txt;
			getline(cin,txt);
			stringstream ss(txt);
			cnt[i] = 0;
			while(ss >> s[i][cnt[i]]) {
				cnt[i]++;
			}
		}
		printf("Case #%d: ", c);
		solve();
	}
}
