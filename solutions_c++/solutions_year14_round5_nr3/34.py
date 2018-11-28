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
		cerr << "ok" << endl;
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



int ans;

set<int> in, out;

set<int> numbers;

int id = 3000;


vector<pair<char, int>> com;

void rec(int);

void try_enter(int index, int id) {
	if(in.count(id)) {
		return;
	}
	in.insert(id);
	
	
	bool was_out = out.count(id);
	if(was_out)
		out.erase(id);
	
	rec(index + 1);
	
	if(was_out)
		out.insert(id);
	
	in.erase(id);
}

void try_leave(int index, int id) {
	if(out.count(id)) {
		return;
	}
	out.insert(id);
	
	
	bool was_out = in.count(id);
	if(was_out)
		in.erase(id);
	
	rec(index + 1);
	
	if(was_out)
		in.insert(id);
	
	out.erase(id);
}

void rec(int index) {
	
	if(index == com.size()) {
		ans = min(ans, (int)in.size());
		return;
	}
	
	
	auto func = com[index].first == 'E' ? try_enter : try_leave;
	
	if(com[index].second) {
		func(index, com[index].second);
	}
	else {
		for(auto num: numbers) {
			func(index, num);
		}
		numbers.insert(id);
		++id;
		func(index, id - 1);
		--id;
		numbers.erase(id);
	}
	
}

void solve() {
	ans = 20;
	in.clear();
	out.clear();
	
	numbers.clear();
	
	id = 3000;
	com.clear();
	
	int n;
	cin >> n;
	com.resize(n);
	
	for(int i = 0; i < n; ++i) {

		cin >> com[i].first >> com[i].second;
		if(com[i].second)
			numbers.insert(com[i].second);
	}
	
	
	rec(0);
	if(ans == 20)
		cout << "CRIME TIME\n";
	else
		cout << ans << "\n";
	
}