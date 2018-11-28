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

double dp[205][205];

double get(vector<double> P){
	int n = P.size();
	forn(i, n + 1){
		forn(j, n + 1){
			dp[i][j] = 0;
		}
	}
	dp[0][0] = 1;
	fornn(i, 1, n + 1){
		forn(j, n + 1){
			dp[i][j] = dp[i - 1][j] * (1 - P[i - 1]);
			if(j > 0){
				dp[i][j] += dp[i - 1][j - 1] * P[i - 1];
			}
		}
	}
	return dp[n][n / 2];
}

int main(){
	int tt;
	cin >> tt;
	forn(ii, tt){
		int n, k;
		cin >> n >> k;
		vector<double> P(n);
		forn(i, n){
			cin >> P[i];
		}
		sort(P.begin(), P.end());
		double e = 0;
		forn(i, k + 1){
			vector<double> Z;
			forn(j, i){
				Z.push_back(P[j]);
			}
			forn(j, k - i){
				Z.push_back(P[P.size() - 1 - j]);
			}
			e = max(e, get(Z));
		}
		/*double e = 0;
		forn(i, 1 << n){
			vector<double> G;
			forn(j, n){
				if(i & (1 << j)){
					G.push_back(P[j]);
				}
			}
			if(G.size() == k){
				e = max(e, get(G));
			}
		}*/
		printf("Case #%d: ", ii + 1);
		printf("%0.10f\n", e);
	}
}