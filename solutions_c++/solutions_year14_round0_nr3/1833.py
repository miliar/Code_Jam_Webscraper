/*
 TASK:
 LANG: C++
 */
#include <algorithm>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iterator>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <list>
#include <bitset>
#include <cstring>
#include <string>
#include <climits>
#include <deque>
#include <utility>
#include <complex>
#include <numeric>
#include <functional>
#include <stack>
#include <iomanip>
#include <ctime>
#include <valarray>
//#include "vc.h"
#ifdef _MSC_VER
#include <hash_set>
#include <hash_map>
using namespace stdext;
#define __typeof(x) auto
#else
#if __GNUC__ > 2
#include <ext/hash_set>
#include <ext/hash_map>
using namespace __gnu_cxx;
#else
#include <hash_set>
#include <hash_map>
#endif
#endif

template<class key>
struct hashtemp {

	enum {
		bucket_size = 4, min_buckets = 8
	};
	virtual size_t operator()(const key &p) const=0;
	virtual ~hashtemp() {
	}

};

using namespace std;
#ifndef M_PI
const long double M_PI=acos((long double)-1);
#endif
#define rep(i,n) for(int  i=0;i<(int)(n);++i)
long double ZERO = 0;
const long double INF = 1 / ZERO, EPSILON = 1e-12;
#define all(c) (c).begin(),(c).end()
#define rep2(i,a,b) for(int i=(a);i<=((int)b);++i)
#define foreach(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)

#define sz(v) ((int)((v).size()))
#define let(x,y) __typeof(y) x(y)

#define rrep(i,n) for(int  i=((int)n)-1;i>=0;--i)
#define rall(c) (c).rbegin(),(c).rend()
#define rrep2(i,a,b) for(int i=(a);i>=((int)b);--i)
#define rforeach(it,c) for(__typeof((c).rbegin()) it=(c).rbegin();it!=(c).rend();++it)
#define rep2d(i, j, v) rep(i, sz(v)) rep(j, sz(v[i]))
#define foreach2d(i, j, v) foreach(i,v) foreach(j,*i)

int r, c, m;
char g[11][11];
char tmp[11][11];

int dir8[8][2] = { { 0, -1 }, { -1, -1 }, { -1, 0 }, { -1, 1 }, { 0, 1 },
		{ 1, 1 }, { 1, 0 }, { 1, -1 } };
bool getDir8(int i, int j, int k, int &ni, int &nj, int r, int c) {
	ni = i + dir8[k][0];
	nj = j + dir8[k][1];
	return ni >= 0 && ni < r && nj < c && nj >= 0;
}
int ok(int i, int j) {
	if (tmp[i][j] == '*')
		return 0;
	char old = tmp[i][j];
	tmp[i][j] = '*';
	int res = 1;
	if (old == '0')
		rep(k,8)
		{
			int ni, nj;
			if (getDir8(i, j, k, ni, nj, r, c))
				res += ok(ni, nj);
		}
	return res;
}

char cnt(int i, int j) {
	char res = '0';
	rep(k,8)
	{
		int ni, nj;
		if (getDir8(i, j, k, ni, nj, r, c))
			res += g[ni][nj] == '*';
	}
	return res;
}
bool test() {
	int t = 0;
	rep(i,r)
		rep(j,c)
		{
			if (g[i][j] == '*')
				tmp[i][j] = '*';
			else
				tmp[i][j] = cnt(i, j), t++;
		}

	rep(i,r)
		rep(j,c)
			if (tmp[i][j] == '0' || t==1 &&tmp[i][j] != '*') {
				if (ok(i, j) == t ) {
					g[i][j] = 'c';
					return true;
				}
				else return 0;
			}

	return t == 1;
}

char arr[100];
int main() {
	std::ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
#ifndef ONLINE_JUDGE
	freopen("1.in", "rt", stdin);
	freopen("1.out", "wt", stdout);
#endif
	int T;
	cin >> T;
	rep(t,T)
	{

		cin >> r >> c >> m;
		
		rep(i,r*c)
			arr[i] = i < m ? '*' : '.';
		printf("Case #%d:\n", t + 1);
		do {
			int k = 0;
			rep(i,r)
				rep(j,c)
					g[i][j] = arr[k++];
			if (test()) {
				rep(i,r)
				{
					rep(j,c)
						printf("%c",g[i][j]); 
					printf("\n");
				}
				goto bara;
			}
		} while (next_permutation(arr, arr + r * c));
		printf("Impossible\n");
		bara:


		cerr<<t<<endl;
	}
	return 0;
}
