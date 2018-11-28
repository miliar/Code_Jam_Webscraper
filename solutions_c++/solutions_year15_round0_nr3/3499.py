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

int t;
int dp[11111][10][4];
int n, k;
char s[nmax];
int mat[4][4] = {{1, 2, 3, 4},
				{2, -1, 4, -3},
				{3, -4, -1, 2},
				{4, 3, -2, -1}};

int mul(int a, int b) {
	int x = 0;
	if(a < 0) a = -a, x = 1 - x;
	if(b < 0) b = -b, x = 1 - x;
	int r = mat[a - 1][b - 1];
	if(x != 0) r = -r;
	return r;
}

int f(char c) {
	if(c == '1') return 1;
	if(c == 'i') return 2;
	if(c == 'j') return 3;
	if(c == 'k') return 4;
	return -1;
}

int g(int x) {
	if(x < 0) {
		return 4 - x;
	}
	return x;
}

int h(int x) {
	if(x <= 4) {
		return x;
	}
	return 4 - x;
}

int main() {
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
	//freopen("distance.in", "r", stdin); freopen("distance.out", "w", stdout);
	//ios :: sync_with_stdio(false);
	cin >> t;
	for(int te = 1; te <= t; ++te) {
		memset(dp, 0, sizeof(dp));
		scanf("%d%d\n", &n, &k);
		gets(s + 1);
		for(int i = n + 1; i <= n * k; ++i) {
			s[i] = s[i - n];
		}
		n *= k;
		dp[1][f(s[1])][0] = 1;
		for(int i = 1; i < n; ++i) {
			for(int j = 1; j <= 8; ++j) {
				for(int k = 0; k < 3; ++k) {
					if(dp[i][j][k] != 0) {
						if(k == 0 && h(j) == 2 || k == 1 && h(j) == 3) {
							dp[i + 1][f(s[i + 1])][k + 1] = 1;
						}
						int nxt = mul(h(j), f(s[i + 1]));
						dp[i + 1][g(nxt)][k] = 1;
					}
				}
			}
		}
		printf("Case #%d: %s\n", te, dp[n][4][2] == 1 ? "YES" : "NO");
	}
	getchar(); getchar();
	return 0;
}