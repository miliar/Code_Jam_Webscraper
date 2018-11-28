#define _ijps 01
#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker, "/STACK:667772160")
#include <iostream>
#include <cmath>
#include <vector>
#include <time.h>
#include <map>
#include <set>
#include <deque>    
#include <cstdio>
#include <unordered_map>
#include <unordered_set>
#include <bitset>
#include <algorithm>
#include <string>
#include <fstream>    
#include <complex>    
#include <assert.h>
#include <list>
#include <cstring>
using namespace std;

#define name ""
typedef unsigned long long ull;
typedef long long ll;
#define mk make_pair
#define forn(i, n) for(ll i = 0; i < (ll)n; i++)
#define fornn(i, q, n) for(ll i = ( ll)q; i < (ll)n; i++)
#define times clock() * 1.0 / CLOCKS_PER_SEC

struct __isoff{
	__isoff(){
		if (_ijps)
			freopen("input.txt", "r", stdin), freopen("output.txt", "w", stdout);//, freopen("test.txt", "w", stderr);
		//else freopen(name".in", "r", stdin), freopen(name".out", "w", stdout);
		//ios_base::sync_with_stdio(0);
		srand('C' + 'T' + 'A' + 'C' + 'Y' + 'M' + 'B' + 'A');
		//srand(time(0));
	}
	~__isoff(){
		//if(_ijps) cout<<' '<<times<<'\n';
	}
} __osafwf;
const ull p1 = 123123;
const ull p2 = 12321;
const double eps = 1e-6;
const double pi = acos(-1.0);

const ll inf = 1e18 + 7;
const int infi = 1e9 + 7;
const ll dd = 1e6 + 7;
const ll maxN = 1e5 + 7;
const ll sh = 4501;
const ll mod = 1e9 + 7;
const ll mod2 = 100003;

int n, k;
vector < vector<int> > g;
vector<int> mt;
vector<bool> used;

bool dfs(int v) {
	if (used[v]) { 
		return 0;
	}
	used[v] = 1;
	forn(i, g[v].size()){
		int to = g[v][i];
		if (mt[to] == -1 || dfs(mt[to])) {
			mt[to] = v;
			return 1;
		}
	}
	return 0;
}
 
bool ok(vector<vector<bool> > B){
	forn(i, B.size()){
		k = n = B[i].size();
		g.clear();
		g.resize(B.size());
		forn(j, B.size()){
			if(i == j){
				continue;
			}
			forn(k, B.size()){
				if(B[i][k] && B[j][k]){
					g[k].push_back(j);
				}
			}
		}
		mt.assign(k, -1);
		for (int v = 0; v < n; ++v) {
			used.assign(n, false);
			dfs(v);
		}
		int t = 0;
		forn(i, k){
			t += mt[i] != -1;
		}
		forn(j, B[i].size()){
			t -= B[i][j];
		}
		if(t == 0){
			return 0;
		}
	}
	return 1;
}

int main(){
	int tt;
	cin >> tt;
	forn(ii, tt){
		int n;
		cin >> n;
		vector<vector<bool> > G(n, vector<bool>(n));
		forn(i, n){
			string s;
			cin >> s;
			forn(j, n){
				if(s[j] == '1'){
					G[i][j] = 1;
				}
			}
		}
		int res = infi;
		forn(i, (1 << (n * n))){
			int ce = 0;
			vector<vector<bool> > T = G;
			forn(j, n * n){
				if(i & (1 << j)){
					if(!T[j % n][j / n]){
						ce++;
					}
					T[j % n][j / n] = 1;
				}
			}
			if(ok(T)){
				res = min(res, ce);
			}
		}
		cout << "Case #" << ii + 1 << ": " << res << '\n';
		cerr << ii << '\n';

	}
}