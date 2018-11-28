#pragma comment(linker, "/STACK:100000000")
#define _CRT_SECURE_NO_WARNINGS
#include <algorithm>
#include <iostream>
#include <memory.h>
#include <cstdlib>
#include <complex>
#include <sstream>
#include <cstring>
#include <vector>
#include <cstdio>
#include <string>
#include <bitset>
#include <queue>
#include <stack>
#include <ctime>
#include <cmath>
#include <map>
#include <set>
 
using namespace std;
 
typedef unsigned long long ull;
typedef complex < double > cd;
typedef long double ld;
typedef long long ll;
 
#define ppb pop_back
#define pb push_back
#define mp make_pair
#define fs first
#define sd second
 
#define inf 1000000007
#define nmax 100010
#define mmax 100010
#define eps 1e-9

int t, k;
string s;

bool can(int d) {
	int cur = d + s[0] - '0';
	for(int i = 1; i <= k; ++i) {
		if(cur < i) {
			return false;
		}
		cur += s[i] - '0';
	}
	return true;
}

int main() {
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
	//freopen("distance.in", "r", stdin); freopen("distance.out", "w", stdout);
	//ios :: sync_with_stdio(false);
	cin >> t;
	for(int te = 1; te <= t; ++te) {
		cin >> k >> s;
		int l = -1, r = k + 10;
		while(l < r - 1) {
			int m = (l + r) / 2;
			if(can(m))
				r = m;
			else
				l = m;
		}
		printf("Case #%d: %d\n", te, r);
	}
	getchar(); getchar();
	return 0;
}