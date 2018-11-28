#pragma comment(linker, "/STACK:60000000")
#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <cstdlib>
#include <string>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <iomanip>
#include <queue>
#include <stack>
#include <complex>
#include <list>
#include <deque>
#include <cassert>
#include <ctime>
using namespace std;

#ifdef WIN32
    #define LLD "%I64d"
#else
    #define LLD "%lld"
#endif

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;

const double PI = acos(-1.0); 
const double eps = 1e-12;
const int INF = (1 << 31) - 1;
const ll LLINF = ((ll)1 << 62) - 1;

#define mp make_pair
#define pb push_back
#define sz(x) (int)x.size()
#define X first
#define Y second
#define all(x) x.begin(),x.end()
#define fill(a, x) memset(a, x, sizeof(a));
#define next nexttt
#define prev prevvv
#define y1 y111

const int base = 1000000000;
const int base_digits = 9;

long long p[]={
    1,
    4,
    9,
    121,
    484,
    10201,
    12321,
    14641,
    40804,
    44944,
    1002001,
    1234321,
    4008004,
    100020001,
    102030201,
    104060401,
    121242121,
    123454321,
    125686521,
    400080004,
    404090404,
    10000200001,
    10221412201,
    12102420121,
    12345654321,
    40000800004,
    1000002000001,
    1002003002001,
    1004006004001,
    1020304030201,
    1022325232201,
    1024348434201,
    1210024200121,
    1212225222121,
    1214428244121,
    1232346432321,
    1234567654321,
    4000008000004,
    4004009004004
   };

int main() {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	
	
	//printf("%d\n", sz(s));

	int t, cnt = 0;
	scanf("%d", &t);
	for (int i = 0; i < t; i++) {
		ll k1, k2;
		cnt = 0;
		scanf(LLD LLD, &k1, &k2);
		for (int i = 0; i < 39; i++) {
			if (p[i] >= k1 && p[i] <= k2) 
				cnt++; 
		}
		printf("Case #%d: %d\n", i + 1, cnt);
	}
	return 0;
}