#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <cmath>
#include <algorithm>
#include <assert.h>
#include <memory.h>
#include <string.h>
#include <complex>
#include <queue>

using namespace std;

#pragma comment(linker, "/STACK:100000000")

#define ll long long
#define pb push_back
#define mp make_pair
#define sz(x) (int)(x).size()
#define fr(i,a,b) for(int i = (a);i <= (b);i++)
#define fd(i,a,b) for(int i = (a);i >= (b);i--)

#define div fpfasjsaijd

int ri(){int x;scanf("%d",&x);return x;}

__int128 min(__int128 a, __int128 b) {
	if(a < b) return a;
	return b;
}

int main() {
	//freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++) {
		printf("Case #%d:\n", t);
		int N, J;
		scanf("%d %d", &N, &J);
		for(__int128 mask = 0, maxmask = ((__int128)1 << (N - 2)); mask < maxmask; mask++) {
			if(J == 0) break;
			ll cur = mask * (__int128)2 + (__int128)1;
			cur += ((__int128)1 << (N - 1));
			vector<__int128> divs;
			for(int deg = 2; deg <= 10; deg++) {
				__int128 val = 0;
				for(int i = N - 1; i >= 0; i--) {
					val *= (__int128)deg;
					if(cur & ((__int128)1 << i)) val++;
				}
				for(__int128 div = 2, maxdiv = min((__int128)1000000, val - (__int128)1); div <= maxdiv; div++) {
					if(val % div == 0) {
						divs.pb(div);
						break;
					}
				}
			}
			if(sz(divs) == 9) {
				J--;
				for(int i = N - 1; i >= 0; i--) {
					if(cur & ((__int128)1 << i)) printf("1");
					else printf("0");
				}
				for(int i = 0; i < sz(divs); i++) {
					cout << " " << (ll)divs[i];
				}
				cout << endl;
			}
		}

	}


	return 0;
}
