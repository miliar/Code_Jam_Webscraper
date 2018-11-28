#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <map>
#include <set>
#include <vector>
#include <iostream>
using namespace std;
typedef long long LL;
map<LL, LL> ma, mb;
map<LL, LL> :: iterator ait, bit;
//const int MAXN = 64;
//int low[MAXN], high[MAXN], cur[2][MAXN], begin[MAXN];
int main() {
	int testnum, n, p;
	LL cnt, cstep, cur, step, l;
	scanf("%d", &testnum);
	for (int test = 1; test <= testnum; test++) {
		scanf("%d%d", &n, &p);
		l =  1LL << n;
		ma.clear(); 
		mb.clear();
		p--;
		ma[0] = mb[0] = 0;
		ma[l - 1] = mb[l - 1] = l - 1;
		ma[l] = mb[l] = l;
		cnt = 0;
		cstep = 1;
		cur = 0;
		step = 1 << (n - 1);
		for (int i = 1; i < n; i++) {
			cstep <<= 1;
			cnt += cstep;
			cur += step;
			mb[cur] = cnt;
			step >>= 1;
		}
		cnt = 0;
		cstep = 1 << (n - 1);
		cur = 0;
		step = 1;
		for (int i = 1; i < n; i++) {
			cnt += cstep;
			cur += step;
			ma[cur] = cnt;
			step <<= 1;
			cstep >>= 1;
		}
		bit = mb.upper_bound(p);
		ait = ma.upper_bound(p);
		bit--; ait--;
		printf("Case #%d: %lld %lld\n", test, bit->second, ait->second);
	}
	return 0;
	/*int n = 6;
	int l = 1 << n;
	for (int i = 0; i < l; i++) {
		begin[i] = i;
		low[i] = l;
		high[i] = -1;
	}
	int cnt = 1000000;
	do {
		int a = 0, x, y;
		memcpy(cur[0], begin, sizeof(int) * l);
		for (int i = 0; i < n; i++) {
			for (int j = 0; (j << 1) < l; j++) {
				x = cur[a][j << 1]; y = cur[a][(j << 1) | 1];
				if (x > y) swap(x, y);
				cur[!a][j] = x; cur[!a][j + (l >> 1)] = y;
			}
			a = !a;
		}
		for (int i = 0; i < l; i++) {
			low[cur[a][i]] = min(low[cur[a][i]], i);
			high[cur[a][i]] = max(high[cur[a][i]], i);
		}
		random_shuffle(begin, begin + l);
	} while (cnt-- > 0);//next_permutation(begin, begin + l));
	for (int i = 0; i < l; i++)
		printf("%d%c", low[i], i + 1 < l ? ' ' : '\n');
	for (int i = 0; i < l; i++)
		printf("%d%c", high[i], i + 1 < l ? ' ' : '\n');
	return 0;*/
}