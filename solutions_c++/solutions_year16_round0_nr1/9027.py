#pragma comment(linker,"/STACK:64000000")
#include <iostream>
#include <vector>
#include <string>
#include <locale>
#include <set>
#include <cstdio>
#include <map>
#include <algorithm>
#include <ctype.h>
#include <cmath>
#include <cstdlib>
#include <utility>
#include <queue>
#include <iomanip>
#include <stack>
#include <bitset>
#include <functional>
#define _USE_MATH_DEFINES
#define mp make_pair
#define pb push_back      
#define F first
#define S second
#define SS stringstream
#define sqr(x) ((x)*(x))
#define CC(x) cout << (x) << endl
#define pw(x) (1ll<<(x))
#define buli(x) __builtin_popcountll(x)
#define forn(i, n) for(int i = 0 ; (i) < (n) ; ++i)
#define MAX_N 1000000007
#define LL long long
template <class T> T gcd(T a, T b) { return a ? gcd(b % a, a) : b; } 
using namespace std;


int  main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	

	LL t, p, k, res, n, j;
	cin >> t;
	const int POW = (2 << 9) - 1;
	
	for (int i = 1; i <= t; ++i) {
		n;
		cin >> n;
		if (n == 0) {
			cout << "Case #" << i << ": " << "INSOMNIA" << '\n';
		}
		else {
			res = 0;
			k = n;
			for (int v = 1; res != POW; ++v, j = v) {
				n = k*v;
				while (n) {
					p = n % 10;
					if (p == 0) {
						res |= 1;
					}
					else {
						res |= (1 << p);
					}
					n /= 10;
				}
			}
			cout << "Case #" << i << ": " << k *(j-1) << '\n';
		}
	}

}