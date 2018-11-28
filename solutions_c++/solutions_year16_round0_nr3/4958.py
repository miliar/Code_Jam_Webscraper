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
int cnt, n, k, add, limit;
vector <int64> ans[55];
bool isPrime(int64 x)
{
    if (x == 1) return false;
    if (x == 2 || x == 3) return true;
    for (int i = 2;(int64)i * (int64)i <= x;i++)
        if (x % i == 0) return false;
    return true;
}
int64 getNumber(int a[], int n)
{
    int64 res = 0;
    for (int i = 0;i < n;i++)
        res = (res * 10 + a[i]);
    return res;
}
int64 getBase(int a[], int n, int base)
{
    int64 res = 0, p = 1;
    for (int i = n - 1;i >= 0;i--)
    {
        res += p * a[i];
        p *= base;
    }
    return res;
}
bool isOk(int64 number) {
    int bit[16], m = 0;
    int baseTwo = number;
    while ( number ) {
        bit[m++] = number % 2;
        number /= 2;
    }
    reverse(bit, bit + m);
    if (bit[0] != 1 || bit[m - 1] != 1) return false;
    if (isPrime(baseTwo)) return false;
    for (int base = 3;base <= 10;base++)
    {
        number = getBase(bit, m, base);
        if (isPrime(number)) return false;
    }
    return true;
}
int64 findDivisor(int64 x)
{
    for (int i = 2;(int64)i * (int64)i <= x;i++)
    {
        if (x % i == 0) return i;
    }
}
void saveResult(int64 number, int cnt)
{
    int bit[16], m = 0;
    int baseTwo = number;
    while ( number ) {
        bit[m++] = number % 2;
        number /= 2;
    }
    reverse(bit, bit + m);
    ans[cnt].push_back(getNumber(bit, m));
    ans[cnt].push_back(findDivisor(baseTwo));
    //ans[cnt].push_back(baseTwo);
    for (int base = 3;base <= 10;base++)
    {
        number = getBase(bit, m, base);
        ans[cnt].push_back(findDivisor(number));
        //ans[cnt].push_back(number);
    }
}
int main() {
    freopen("exam.inp","r",stdin);
    freopen("exam.out","w",stdout);
    scanf("%d", &cases);
    while (cases--){
        scanf("%d %d", &n, &k);
        add = 1 + (1 << (n - 1)); limit = (1 << n);
        cnt = 0;
        for (int i = add;i < limit && cnt < k;i++)
        {
            if ((i & 1) && (i & (1 << (n - 1))))
                if (isOk(i)) {
                    saveResult(i, cnt);
                    cnt++;
                }
        }
        printf("Case #%d:\n", ++caseNo);
        for (int i = 0;i < k;i++)
        {
            printf("%lld", ans[i][0]);
            for (int j = 1;j < 10;j++)
                printf(" %lld", ans[i][j]);
            printf("\n");
        }
    }
    return 0;
}
