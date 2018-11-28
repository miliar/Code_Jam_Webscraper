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

vector<monster> monsters;


struct state {
	int pos;
	int hitsCurrent;
	int turns;
	
	
	bool operator < (const state& o) const  {
		return make_tuple(pos, hitsCurrent, turns) < make_tuple(o.pos, o.hitsCurrent, o.turns);
	}
};

int p,q;


map<state, int> res;

int solve(const state& s) {
	
	if(res.count(s))
		return res[s];
	
	if(s.pos == monsters.size())
		return res[s] = 0;
	
	int nh = (s.pos + 1 == monsters.size()) ? 10000 : monsters[s.pos + 1].hits;
	
	if(s.hitsCurrent <= 0) {
		return res[s] = solve({s.pos + 1, 
				nh, 
				s.turns
		});
	}
	
	if(s.turns == 0) {
		return res[s] = solve({s.pos, s.hitsCurrent - q, 1});
	}
	
	
	
	int re = 0;
	{
		
		//bad
		
		int turns = (s.hitsCurrent - 1) / q + 1;
		re = max(re, solve({s.pos + 1, nh, s.turns + turns}));
		
		
		int mod = s.hitsCurrent % q;
		if(mod == 0)
			mod = q;
		if(mod <= p && s.hitsCurrent > q && s.turns + turns - 2 >= 0) {
			re = max(re, solve({s.pos + 1, nh, s.turns + turns - 2}) + monsters[s.pos].gold);
		}
	}
	
	{
		int mon = 0;
		if(s.hitsCurrent <= p)
			mon = monsters[s.pos].gold;
		
		re = max(re, mon + solve({s.pos, s.hitsCurrent - p, s.turns - 1}));
	}
	
	return res[s] = re;
}

void solve() {
	res.clear();
	int n;
	cin >>p >> q >> n;
	vector<monster> a(n);
	for(int i = 0; i < n; ++i) {
		cin >> a[i].hits >> a[i].gold;
	}
	
	a.swap(monsters);
	
	
	
	cout << solve({0, monsters[0].hits, 1}) << "\n";
	
}