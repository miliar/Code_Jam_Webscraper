#define _CRT_SECURE_NO_WARNINGS
#include<sstream>
#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<climits>
#include<cmath>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<numeric>
#include<functional>
#include<algorithm>
#include<bitset>
#include<tuple>
#include<unordered_set>
#include<random>
using namespace std;
#define INF (1<<29)
#define rep(i,n) for(int i=0;i<(int)(n);i++)
#define all(v) v.begin(),v.end()
#define uniq(v) v.erase(unique(all(v)),v.end())



int popcount32(unsigned int x) {
#if defined(_MSC_VER) //Cf
	return __popcnt(x);
#elif defined(__GNUC__)
	return __builtin_popcount(x);
#else 
	x = x - ((x >> 1) & 0x55555555);
	x = (x & 0x33333333) + ((x >> 2) & 0x33333333);
	x = (x + (x >> 4)) & 0x0F0F0F0F;
	x = x + (x >> 8);
	x = x + (x >> 16);
	return x & 0x0000003F;
#endif
}



int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int T;
	cin >> T;
	string fir[1000], sec[1000];
	rep(icase, T) {
		int n;
		cin >> n;
		rep(i, n)cin >> fir[i] >> sec[i];
		int ans = 0;
		rep(i,1<<n) {
			if (ans >= popcount32(i))continue;
			set<string> f, s;
			rep(j,n) {
				if ((i >> j & 1) == 0) {
					f.insert(fir[j]);
					s.insert(sec[j]);
				}
			}
			bool ok = true;
			rep(j, n) {
				if ((i >> j & 1) == 1) {
					if (f.find(fir[j]) == f.end() || s.find(sec[j]) == s.end())ok = false;
				}
			}
			if (ok)ans = popcount32(i);
		}

		cout << "Case #" << icase + 1 << ": " << ans << endl;
	}


	return 0;
}