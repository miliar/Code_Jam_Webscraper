/***********************************************
* Author - LUONG VAN DO                        *
*
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
#define FOR(i,a,b) for (int i=a;i<=b;i++)
#define FORD(i,a,b) for (int i=a;i>=b;i--)
#define REP(i, n) for (int i=0; i<n; i++)
#define fill(ar, val) memset(ar, val, sizeof(ar))
#define pb push_back
#define A first
#define B second
#define PI 3.1415926535897932385
#define uint64 unsigned long long
#define int64 long long
#define INF 500000000
#define N 100000

using namespace std;

inline int max(int a, int b) { return a > b ? a : b; }
inline int min(int a, int b) { return a < b ? a : b; }
inline int gcd(int a, int b) { if (a % b) return gcd(b, a % b); else return b; }
inline int lcm(int a, int b) { return (a * (b / gcd(a, b) )); }

inline int And(int mask, int bit) { return mask & (1 << bit); }
inline int Xor(int mask, int bit) { return mask & (~(1 << bit)); }

typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;
int cases, caseNo = 0;
int n;
int flg[10];
int64 ans;
bool isOk(int64 x) {
    while ( x ) {
        flg[x % 10] = 1;
        x /= 10;
    }
    for (int i = 0;i < 10;i++)
        if (flg[i] == 0) return false;
    return true;
}
int main() {
    freopen("exam.inp","r",stdin);
    freopen("exam.out","w",stdout);
    scanf("%d",&cases);
    //for (int i = 0;i <= 1000000;i++) cout<<i<<endl;
    while (cases--)
    {
        scanf("%d", &n);
        if (n == 0) {
            printf("Case #%d: INSOMNIA\n", ++caseNo);
            continue;
        }
        for (int i = 0;i < 10;i++) flg[i] = 0;
        for (int j = 1;;j++)
        if (isOk(j * (int64)n)){
            ans = j * n;
            break;
        }
        printf("Case #%d: %lld\n", ++caseNo, ans);
    }
    return 0;
}
