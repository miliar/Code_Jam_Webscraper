/*
 * temp.cpp
 *
 *  Created on: 2012-7-18
 *      Author: BSBandme
 */
//#pragma comment(linker, "/STACK:1024000000,1024000000")
#include <iostream>
#include <fstream>
#include <string.h>
#include <cstdio>
#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <cassert>
#include <list>
#include <iomanip>
#include <math.h>
#include <deque>
#include <utility>
#include <map>
#include <set>
#include <bitset>
#include <numeric>
#include <climits>
#include <cctype>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <functional>
#include <sstream>

using namespace std;

#define mpr make_pair
typedef unsigned int ui;
typedef unsigned long long ull;
typedef long long ll;
typedef pair <int, int> pii;
typedef pair <ll, ll> pll;
typedef pair <double, double> pdd;
typedef vector <int> vi;
typedef vector <ll> vll;
typedef vector <double> vd;
typedef vector <string> vs;
typedef map <string, int> mpsi;
typedef map <double, int> mpdi;
typedef map <int, int> mpii;

const double pi = acos(0.0) * 2.0;
const double eps = 1e-12;
const int step[8][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}, {1, 1}, {1, -1}, {-1, 1}, {-1, -1}};

template <class T> inline T abs1(T a) {return a < 0 ? -a : a;}

template <class T> inline T max1(T a, T b) { return a > b ? a : b; }
template <class T> inline T max1(T a, T b, T c) { return max1(max1(a, b), c); }
template <class T> inline T max1(T a, T b, T c, T d) { return max1(max1(a, b, c), d); }
template <class T> inline T max1(T a, T b, T c, T d, T e) { return max1(max1(a, b, c, d), e); }
template <class T> inline T min1(T a, T b) { return a < b ? a : b; }
template <class T> inline T min1(T a, T b, T c) { return min1(min1(a, b), c); }
template <class T> inline T min1(T a, T b, T c, T d) { return min1(min1(a, b, c), d); }
template <class T> inline T min1(T a, T b, T c, T d, T e) { return min1(min1(a, b, c, d), e); }

inline int jud(double a, double b){
	if(abs(a) < eps && abs(b) < eps) return 0;
	else if(abs1(a - b) / abs1(a) < eps) return 0;
	if(a < b) return -1;
	return 1;
}
template <typename t> inline int jud(t a, t b){
	if(a < b) return -1;
	if(a == b) return 0;
	return 1;
}

// f_lb == 1��������ͬ��һ������߽磬f_small == 1���������û��Ѱ�ҵ�ֵ����С����
template <typename it, typename t1>
inline int find(t1 val, it a, int na, bool f_small = 1, bool f_lb = 1){
	int be = 0, en = na - 1;
	if(*a <= *(a + na - 1)){
		if(f_lb == 0) while(be < en){
			int mid = (be + en + 1) / 2;
			if(jud(*(a + mid), val) != 1) be = mid;
			else en = mid - 1;
		}else while(be < en){
			int mid = (be + en) / 2;
			if(jud(*(a + mid), val) != -1) en = mid;
			else be = mid + 1;
		}
		if(f_small && jud(*(a + be), val) == 1) be--;
		if(!f_small && jud(*(a + be), val) == -1) be++;
	} else {
		if(f_lb) while(be < en){
			int mid = (be + en + 1) / 2;
			if(jud(*(a + mid), val) != -1) be = mid;
			else en = mid - 1;
		}else while(be < en){
			int mid = (be + en) / 2;
			if(jud(*(a + mid), val) != 1) en = mid;
			else be = mid + 1;
		}
		if(!f_small && jud(*(a + be), val) == -1) be--;
		if(f_small && jud(*(a + be), val) == 1) be++;
	}
	return be;
}

template <class T> inline T lowb(T num) {return num & (-num); }
inline int bitnum(ui nValue) { return __builtin_popcount(nValue); }
inline int bitnum(int nValue) { return __builtin_popcount(nValue); }
inline int bitnum(ull nValue) { return __builtin_popcount(nValue) + __builtin_popcount(nValue >> 32); }
inline int bitnum(ll nValue) { return __builtin_popcount(nValue) + __builtin_popcount(nValue >> 32); }
inline int bitmaxl(ui a) { if(a == 0) return 0; return 32 - __builtin_clz(a); }
inline int bitmaxl(int a) { if(a == 0) return 0; return 32 - __builtin_clz(a); }
inline int bitmaxl(ull a) { int temp = a >> 32; if(temp) return 32 - __builtin_clz(temp) + 32; return bitmaxl(int(a)); }
inline int bitmaxl(ll a) { int temp = a >> 32; if(temp) return 32 - __builtin_clz(temp) + 32; return bitmaxl(int(a)); }

long long pow(long long n, long long m, long long mod = 0){
	if(m < 0) return 0;
	long long ans = 1;
	long long k = n;
	while(m){
		if(m & 1) {
			ans *= k;
			if(mod) ans %= mod;
		}
		k *= k;
		if(mod) k %= mod;
		m >>= 1;
	}
	return ans;
}

#define debug
//.........................mi.......feng......xian.......xia.......jin.......zhi.......hack...............................................

const int maxn = 500;
int n, m, ncase, nm;
char mp[maxn][maxn];

int main(){
    ios_base::sync_with_stdio(0);
	#ifdef debug //......................................................................................................
	freopen("input.txt", "r", stdin);
	#endif //...........................................................................................................
	freopen("output.txt", "w", stdout);
	scanf("%d", &ncase);
	for(int i1 = 0; i1 < ncase; i1++) {
		memset(mp, 0, sizeof(mp));
		scanf("%d%d%d", &n, &m, &nm);
		int rnm = nm;
		printf("Case #%d:\n", i1 + 1);
		if(nm == 0) {
			for(int i = 0; i < n; i++) for(int j = 0; j < m; j++) mp[i][j] = '.';
			mp[0][0] = 'c';
			for(int i = 0; i < n; i++) puts(mp[i]);
			continue;
		}
		if(nm == n * m - 1) {
			for(int i = 0; i < n; i++) for(int j = 0; j < m; j++) mp[i][j] = '*';
			mp[0][0] = 'c';
			for(int i = 0; i < n; i++) puts(mp[i]);
			continue;
		}
		bool flag = 0, can = 1;
		if(n > m) swap(n, m), flag = 1;
		if(n == 1) {
			if(m - 2 >= nm) {
				for(int i = 0; i < n; i++) for(int j = 0; j < m; j++) mp[i][j] = '*';
				for(int i = 0; i < m - nm; i++) mp[0][i] = '.';
				mp[0][0] = 'c';
			} else can = 0;
		} else {
			if(nm <= n * m - 4) {
				for(int i = 0; i < n; i++) for(int j = 0; j < m; j++) mp[i][j] = '*';
				nm = n * m - nm;
				can = 0;
				for(int i = 2; i <= n && i <= nm / 2; i++) if(nm % i != 1 && nm / i + bool(nm % i) <= m) {
					can = 1;
					int cnt = 0;
					for(int j = 0; j < m && cnt < nm; j++) for(int k = 0; k < i && cnt < nm; k++) {
						mp[k][j] = '.';
						cnt++;
					}
					break;
				}
				if(can == 0 && n != 2 && nm != 5 && nm != 7) {
					can = 1;
					int cnt = 0;
					for(int j = 0; j < m && cnt < nm - 2; j++) for(int i = 0; i < n && cnt < nm - 2; i++) {
						mp[i][j] = '.';
						cnt++;
					}
					mp[0][nm / n] = mp[1][nm / n] = '.';
				}
				mp[0][0] = 'c';
			} else can = 0;
		}
		if(can == 0) puts("Impossible");
		else {
			int rcnt = 0;
			for(int i = 0; i < n; i++) for(int j = 0; j < m; j++)
				rcnt += mp[i][j] == '*';
			assert(rcnt == rnm);
			if(flag) {
				for(int j = 0; j < m; j++) {
					for(int i = 0; i < n; i++) printf("%c", mp[i][j]);
					puts("");
				}
			} else for(int i = 0; i < n; i++) puts(mp[i]);
		}
	}

    return 0;
}



