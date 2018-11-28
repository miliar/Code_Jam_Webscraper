#include <iostream>
#include <string>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <string.h>
#include <utility>
#include <queue>
#include <stack>
#include <iomanip>
#include <ctype.h>
#include <sstream>
#include <map>
#include <set>
#include <stdio.h>
#include <assert.h>
#include <ctype.h>

using namespace std;

#define FOR(i,n) for(int i = 0;i < n;i++)
#define FORR(i,n) for(int i = n-1;i >= 0;i--)
#define REP(i,a,b) for(int i = (a);i<(b);++i)
#define MP make_pair
#define ALL(a) (a).begin(),(a).end()
#define PB push_back
#define PII pair<int,int>
#define sz(a) (int)(a).size()
#define CLEAR(a) memset(a, 0, sizeof(a))
#define INF 2000000000


typedef long long LL;

int m,n;
string s;
vector<string> a;
vector<string> e[4];

int wc = -1;
int cnt = 0;

int serv(int idx) {
	set<string> q;
	FOR(i, e[idx].size()) {
		//cerr << "S " << e[idx][i] << endl;
		FOR(l, e[idx][i].length() + 1) {
			q.insert(e[idx][i].substr(0, l));
		}
	}

	return q.size();
}

void eval() {
	int mywc = 0;
	FOR(i, n) {
		mywc += serv(i);
	}

	if (mywc > wc) {
		wc = mywc;
		cnt = 1;
	} else if (mywc == wc) {
		cnt++;
	}
}

void go(int idx) {
	if (idx == m) {
		eval();
		return;
	}
	FOR(i, n) {
		e[i].push_back(a[idx]);
		go(idx + 1);
		e[i].pop_back();
	}
}

void solve() {
	cin >> m >> n;
	FOR(i,m) {
		cin >> s;
		a.push_back(s);
	}

	go(0);

	cout << wc << ' ' << cnt << endl;
}

int main() {
  ios_base::sync_with_stdio(0);
  int tt;
  cin >> tt;

  FOR(tn,tt) {
  	a.clear();
  	wc = -1;
  	cnt = 0;
    cout << "Case #" << tn + 1 << ": ";
    solve();
  }



  return 0;
}
