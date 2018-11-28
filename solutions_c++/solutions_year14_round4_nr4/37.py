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
    cout.precision(10);
    cout << fixed;
    int t = 1;
    cin >> t;
	
	precalc();
	for(int i = 1; i <= t; ++i) {
		cout << "Case #" << i << ": ";
		solve();
	}
#ifdef DEBUG
    cerr<<"\n\n"<<(clock() - start) / 1.0 / CLOCKS_PER_SEC<<"\n\n\n";
#endif
    return 0;
}

/*

int res = 0, cnt;

vector<int> cur;
vector<string> s;

int n, m;

void go() {
	vector<set<string>> x(n);
	for(int i = 0; i < m; ++i) {
		for(int j = 0; j <= s[i].size(); ++j)
			x[cur[i]].insert(s[i].substr(0, j));
	}
	
	int ana = 0;
	for(int i = 0; i < x.size(); ++i) {
		ana += x[i].size();
	}
	
	if(ana > res) {
		res = ana;
		cnt = 1;
	}
	else if(ana == res) {
		++cnt;
	}
}
void rec(int index) {
	
	if(index == m) {
		return go();
	}
	
	
	for(int i = 0; i < n; ++i) {
		cur.push_back(i);
		rec(index + 1);
		cur.pop_back();
	}
}



void solve() {
	cin >> m >> n;
	
	res = 0;
	cnt = 0;
	s = vector<string>(m);
	for(auto& x: s)
		cin >> x;
	
	
	rec(0);
	
	//cout << res << ' '<< cnt << "\n";
	cout << res << "\n";
}*/

#define int li



int cnk[1010][1010];


const int mod = 1000000007;
void precalc() {
	for(int i = 0; i <= 1000; ++i) {
		cnk[i][0] = cnk[i][i] = 1;
		for(int j = 1; j <= i; ++j) {
			cnk[i][j] = (cnk[i - 1][j] + cnk[i - 1][j - 1]) % mod;
		}
	}
}

int m, n;

li rec(map<string, int>& cnt, string s) {
	
	int groups = min(n, cnt[s]);
	li mult = 1;
	
	vector<int> cnts;
	
	int mxChSize = 0;
	
	int ends = cnt[s];
	
	for(char c = 'A'; c <= 'Z'; ++c) {
		if(cnt.find(s + c) != cnt.end()) {
			mult *= rec(cnt, s + c);
			mult %= mod;
			cnts.push_back(min(n, cnt[s + c]));
			mxChSize = max(mxChSize, cnts.back());
			ends -= cnt[s + c];
		}
	}
	if(s == "") {
		cout << "";
	}
	if(ends) {
		cnts.push_back(ends);
		mxChSize = max(mxChSize, ends);
	}
	li ans = 0;
	for(int i = groups; i >= mxChSize; --i) {
		int g = ((groups - i) % 2) ? -1 : 1;
		li add = 1;
		for(int z: cnts) {
			add *= cnk[i][z];
			add %= mod;
		}
		
		add *= cnk[groups][i];
		add %= mod;
		ans += (g * add);
	}
	
	ans %= mod;
	ans += mod;
	ans %= mod;
	
	
	return ans * mult % mod;
}


void solve() {
	cin >> m >> n;
	
	
	map<string, int> cnt;
	
	for(int i = 0; i < m; ++i) {
		string s;
		cin >> s;
		for(int j = 0; j <= s.size(); ++j)
			cnt[s.substr(0, j)]++;
	}
	
	int res = 0;
	for(auto& x: cnt) {
		res += min(x.second, n);
	}
	cout << res << ' ' << rec(cnt, "") << "\n";
}