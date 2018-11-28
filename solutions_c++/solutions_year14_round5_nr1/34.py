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


void solve() {
	li n, p, q, R , s;
	cin >>  n >>p >> q >> R >> s;
	vector<li> a(n);
	for(int i = 0; i < n; ++i) {
		a[i] = ((i * p + q) % R + s);
	}
	
	vector<li> pref(n + 1);
	for(int i = 0; i < n; ++i) {
		pref[i + 1] = pref[i] + a[i];
	}
	
	int r = 0;
	
	li bset = 1e18;
	for(int l = 0; l < n; ++l) {
		li left = pref[l];
		--r;
		if(r < l) {
			r = l;
		}
		
		li cur = max(left, max(pref[r] - pref[l], pref[n] - pref[r]));
		bset = min(bset, cur);
		while(r <= n && pref[r] - pref[l] < pref[n] - pref[r]) {
			++r;
			cur = max(left, max(pref[r] - pref[l], pref[n] - pref[r]));
			bset = min(bset, cur);
			
		}
	}
	
	
	//cout << bset << endl;
	
	cout << (pref[n] - bset) * ld(1.0) / pref[n] << "\n";
}