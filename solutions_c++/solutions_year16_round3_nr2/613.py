#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <string>
#include <cstring>
#include <cmath>
#include <bitset>
#include <stack>
#include <vector>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <ctime>
#include <cstring>
#include <list>
//#include <forward_list>
#include <iomanip>
#include <cassert>
#include <functional>	

const double EPS = 0.00000001;
const long long mod = 1000000000 + 7;
using namespace std;
#define ll long long
#define ull unsigned long long
#define mk make_pair

//----------------------------
//
#define cin fin
//
#define cout fout

//----------------------------


#ifdef cin
ifstream fin("in.in");
#endif
#ifdef cout
ofstream fout("out.out");
#endif

ll myPow(ll a, ll n){
	ll res = 1;
	while (n){
		if (n % 2) res *= a;
		n /= 2;
		a *= a;
	}
	return res;
}

int lg(ll x){
	int ans = 0;
	while (x >= 1){
		x /= 2;
		ans++;
	}
	return ans - 1;
}

int g[100][100];

int main(){

	/*c[1][1] = 1;
	for (int i = 0; i < 60; i++) c[i][0] = 1;
	for (int i = 1; i < 60; i++)
	for (int j = 1; j < 60; j++) c[i][j] = c[i - 1][j - 1] + c[i - 1][j];
	fac[0] = 1;
	for (int i = 1; i < 60; i++) fac[i] = fac[i - 1] * i;*/

	ios::sync_with_stdio(0);
	int t, z = 1;
	cin >> t;
	while (t--){
		memset(g, 0, sizeof(g));
		cout << "Case #" << z++ << ": ";
		//--------------------------------------------------------

		ll b, m;
		cin >> b >> m;
		ll n = b - 2;

		ll p = myPow(2, n);
		if (p < m){
			cout << "IMPOSSIBLE" << endl;
			continue;
		}
		else{
			cout << "POSSIBLE" << endl;

			ll x = 1;
			int idx = 0;
			for (int i = 1; i <= b; i++){
				
				idx = i;
				if (x * 2 > m)
					break;
				x *= 2;
			}
			for (int i = 1; i < b; i++) g[i][i + 1] = 1;
			for (int i = b - idx; i <= b; i++){
				for (int j = i + 1; j <= b; j++) g[i][j] = 1;
			}
			m -= myPow(2, idx - 1);

			while (m){
				int d = lg(m);
				x = myPow(2, d);
				m -= x;
				for (int i = 0;; i++){
					if (myPow(2, i) == x){
						g[1][b - i - 1] = 1;
						break;
					}

				}
			}
		}
		for (int i = 1; i <= b; i++){
			for (int j = 1; j <= b; j++) cout << g[i][j];
			cout << endl;
		}
		
		//--------------------------------------------------------

	}
#undef cin
	int ______________;
	cin >> ______________;
	return 0;
}