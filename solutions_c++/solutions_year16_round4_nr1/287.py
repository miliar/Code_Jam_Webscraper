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

string dfs(int n, int t){
	if(n == 0){
		if(t == 0){
			return "P";
		}
		
		if(t == 1){
			return "R";
		}

		return "S";
	}
	if(t == 0){
		string a = dfs(n - 1, t);
		string b = dfs(n - 1, 1);
		return min(a + b, b + a);
	}
	if(t == 1){
		string a = dfs(n - 1, t);
		string b = dfs(n - 1, 2);
		return min(a + b, b + a);
	}
	
	if(t == 2){
		string a = dfs(n - 1, t);
		string b = dfs(n - 1, 0);
		return min(a + b, b + a);
	}
}

int main(){
	int tt;
	cin >> tt;
	forn(ii, tt){
		int n, r, p, s;
		cin >> n >> r >> p >> s;
		string res = "IMPOSSIBLE";
		forn(g, 3){
			string ss = dfs(n, g);
			int q, w, e;
			q = w = e = 0;
			forn(i, ss.size()){
				if(ss[i] == 'R'){
					q++;
				}
				if(ss[i] == 'P'){
					w++;
				}
				if(ss[i] == 'S'){
					e++;
				}
			}
			if(r == q && p == w && e == s){
				if(res[0] == 'I'){
					res = ss;
				}
				res = min(res, ss);
			}
		}
		cout << "Case #" << ii + 1 << ": " << res << '\n';
	}
}