#ifdef _MSC_VER
#define _CRT_SECURE_NO_WARNINGS
#endif

#include <iostream>
#include <cmath>
#include <iomanip>
#include <string>
#include <cstring>
#include <cstdio>
#include <math.h>
#include <algorithm>
#include <stdio.h>
#include <climits>
#include <stack>
#include <queue>
#include <vector>
#include <set>
#include <sstream>
#include <map>
#include <ctime>
#include <cstdlib>
#include <list>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include<unordered_map>
using namespace std;

typedef unsigned long long ull;
typedef long long ll;
int dx8[] = { 0, 0, 1, -1, 1, -1, 1, -1 };
int dy8[] = { -1, 1, 0, 0, -1, -1, 1, 1 };
int dy[] = { 1, -1, 0, 0 };
int dx[] = { 0, 0, 1, -1 };
int X[6] = { 0, 0, 0, -1, 0, 1 };
int Y[6] = { 0, 0, -1, 0, 1, 0 };
int Z[6] = { 1, -1, 0, 0, 0, 0 };
// start + (end - start) / 2;

#define OO ll(1e17)
#define mod ll(1000000007)
/*
*/
int main() {
	freopen("A-large.in", "r", stdin);
	freopen("TectFile1.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	int cnt = 1;
	while (t--) {
		ll n;
		scanf("%lld", &n);
		if (n == 0)printf("Case #%d: INSOMNIA\n", cnt);
		set<int>st;
		ll N = n;
		while (N) {
			st.insert(N % 10);
			N /= 10; 
		}
		if (st.size() == 10) {
			printf("Case #%d: %lld\n", cnt, n);
			continue;
		}
		for (int i = 2; i <= 1000;i++) {
			ll x = i * n;
			while (x) {
				st.insert(x % 10);
				x /= 10;
			}
			if (st.size() == 10) {
				printf("Case #%d: %lld\n", cnt, i*n);
				break;
			}
		}
		cnt++;
	}
}
/*
*/