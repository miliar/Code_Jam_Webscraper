#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <deque>
#include <cmath>
#include <ctime>
#include <stack>
#include <set>
#include <map>
#include <cassert>
#include <memory.h>

using namespace std;

#define mp make_pair
#define pb push_back
#define all(a) a.begin(), a.end()

typedef long long li;
typedef long double ld;
typedef vector<int> vi;
typedef pair <int, int> pi;

void solve();

void precalc();

#define FILENAME "souvenir"

int main(){
    string s = FILENAME;
#ifdef RIAD
    freopen("input", "r", stdin);
#ifndef DEBUG
    freopen("output", "w", stdout);
#endif
    //cout<<FILENAME<<endl;
    //assert (s != "change me please");
    clock_t start = clock(); 
#else
    //freopen(FILENAME ".in", "r", stdin);
    //freopen(FILENAME ".out", "w", stdout);
#endif
    cout.sync_with_stdio(0); 
    cout.precision(20);
    cout << fixed;
    int t = 1;
    cin >> t;
	
	//precalc();
	for(int i = 1; i <= t; ++i) {
		cout << "Case #" << i << ": ";
		solve();
		//cerr << "ok" << endl;
	}
#ifdef DEBUG
    cerr<<"\n\n"<<(clock() - start) / 1.0 / CLOCKS_PER_SEC<<"\n\n\n";
#endif
    return 0;
}


struct monster {
	int hits, gold;
	
	bool operator < (const monster& o) const {
		return tie(o.hits, o.gold) < tie(hits, gold); 
	}
};

vector<set<int>> g;
vi c;


int rec(int pos1, int pos2, bool may_finish) {
	int money_was = c[pos1];
	c[pos1] = 0;
	
	int mn = 1e9;
	if(g[pos1].empty()) {
		if(may_finish && !money_was)
			return 0;
		mn = min(mn, rec(pos2, pos1, true));
	}
	else {
		
		int v = pos1;
		vi copy = vi(g[v].begin(), g[v].end());
		for(int to: copy) {
			g[v].erase(to);
			g[to].erase(v);
			mn = min(mn, rec(pos2, to, false));
			g[v].insert(to);
			g[to].insert(v);
		}
	}
	
	c[pos1] = money_was;
	return money_was - mn;
}


void solve() {
	int n;
	cin >> n;
	
	g.clear();
	g.resize(n);
	
	c.resize(n);
	
	for(int i = 0; i < n; ++i)
		cin >> c[i];
	for(int i = 1; i <= n- 1; ++i) {
		int j;
		cin >> j;
		assert(j >= 1 && j <= n);
		g[i - 1].insert(j - 1);
		g[j - 1].insert(i - 1);
	}
	
	
	int best = -1e9;
	for(int i = 0; i < n; ++i) {
		int worst = 1e9;
		for(int j = 0; j < n; ++j) {
			
			worst = min(rec(i, j, false), worst);
		}
		
		best = max(best, worst);
		
	}
	
	cout << best << "\n";
}