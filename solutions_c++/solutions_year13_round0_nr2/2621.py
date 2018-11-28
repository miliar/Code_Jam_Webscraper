/***********************************************
* Author - LUONG VAN DO                        *
* Problem 
* Algorithm
* Time Limit
* *********************************************/
#include <iostream>
#include <stdio.h>
#include <queue>
#include <stack>
#include <vector>
#include <map>
#include <set>
#include <list>
#include <cmath>
#include <math.h>
#include <cstring>
#include <string.h>
#include <stdlib.h>
#include <algorithm>

#define FileIn(file) freopen(file".inp", "r", stdin)
#define FileOut(file) freopen(file".out", "w", stdout)
#define fr(i,a,b) for (int i=a;i<=b;i++)
#define FORD(i,a,b) for (int i=a;i>=b;i--)
#define rep(i, n) for (int i=0; i<n; i++)
#define repr(i, n) for (int i = n - 1;i >= 0;i--)
#define fill(ar, val) memset(ar, val, sizeof(ar))
#define pb push_back
#define ff first
#define ss second
#define PI 3.1415926535897932385
#define uint64 unsigned long long
#define int64 long long
#define INF 500000000
#define N 111

using namespace std;

inline int max(int a, int b) { return a > b ? a : b; }
inline int min(int a, int b) { return a < b ? a : b; }
inline int gcd(int a, int b) { if (a % b) return gcd(b, a % b); else return b; }
inline int lcm(int a, int b) { return (a * (b / gcd(a, b) )); }

inline int And(int mask, int bit) { return mask & (1 << bit); }
inline int Or(int mask, int bit) { return mask | (1 << bit); }
inline int Xor(int mask, int bit) { return mask & (~(1 << bit)); }

typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;
int m, n, c1, c2;
int a[N][N];
bool checkR(int r) {
    rep(i, n)
        if (a[r][i] != 1) return false;
    return true;
}
bool checkC(int c) {
    rep(i, m)
        if (a[i][c] != 1) return false;
    return true;
}
int main() {
	freopen("exam.inp","r", stdin); freopen("exam.out","w", stdout);
	int cases, caseno = 0;
	scanf("%d", &cases);
	while (cases--) {
        scanf("%d %d", &m, &n);
        c1 = c2 = 0;
        printf("Case #%d: ", ++caseno);
        rep(i, m) rep(j, n) {
            scanf("%d", &a[i][j]);
            if (a[i][j] == 1) c1++;
            if (a[i][j] == 2) c2++;
        }
        if (c1 == n * m || c2 == n * m) {
            puts("YES");
            continue;
        }
        rep(i, m) rep(j, n)
            if (a[i][j] == 1)
                if ( checkR(i) || checkC(j) ) c1--;
        if (!c1) puts("YES");
        else puts("NO");
	}
	return 0;
}
