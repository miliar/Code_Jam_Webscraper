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
		srand(time(0));
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
const int infi = 2e9 + 7;
const ll dd = 1e5 + 7;
const ll sh = 4501;
const ll mod = 1e9 + 7;
const ll mod2 = 175781251;

int main(){
	int fg;
	cin >> fg;
	forn(ii, fg){
		int n, j;
		cin >> n >> j;
		cout << "Case #" << ii + 1 << ": ";
		cout << '\n';
		forn(i, j){
			string g;
			ll t = i * 2 + 1 + (1 << (n / 2 - 1));
			forn(k, n / 2){
				bool ok = t & (1ll << k);
				g.push_back(ok + '0');
			}
			reverse(g.begin(), g.end());
			cout << g << g << ' ';
			reverse(g.begin(), g.end());
			fornn(k, 2, 11){
				ll t = 0, q = 1;
				forn(e, g.size()){
					t += (g[e] - '0') * q;
					q *= k;
				}
				cout << t << ' ';
			}
			cout << '\n';
		}
		cout << '\n';
	}
}