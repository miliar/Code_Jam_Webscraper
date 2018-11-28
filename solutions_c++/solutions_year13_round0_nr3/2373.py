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
#define N 100111

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
int64 a[] = {1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521,400080004,404090404,10000200001,10221412201,12102420121,12345654321,40000800004,1000002000001,1002003002001,1004006004001,1020304030201,1022325232201,1024348434201,1210024200121,1212225222121,1214428244121,1232346432321,1234567654321,4000008000004,4004009004004};
int64 l, r, ans;
//int tt[N];
vector <int64> num;
bool isPalin(int64 x) {
    int c[100], sz = 0, l, r;
    while ( x ) {
        c[sz++] = x % 10LL;
        x /= 10LL;
    }
    l = 0; r = sz - 1;
    while (l <= r) {
        if (c[l] != c[r]) return false;
        l++; r--;
    }
    return true;
}
bool check(int64 x) {
    int64 y = (int64)sqrt(x);
    if ( isPalin(x) && isPalin(y) ) return true;
    return false;
}
int f(int64 x) {
    int k = 0;
    while (k < 39 && a[k] <= x) k++;
    return k;
}
int main() {
	freopen("exam.inp","r", stdin); freopen("exam.out","w", stdout);
	/*num.clear();
	for (int i = 1;i <= 10000000;i++) {
	    int64 so = (int64)i * (int64)i;
        if ( check(so) ) {
            cout<<so<<endl;
            num.pb(so);
        }
	}
    cout<<num.size()<<endl;
    /*printf("{%lld",num[0]);
    for (int i = 1;i < num.size();i++)
        printf(",%lld", num[i]);
    printf("};\n");*/
	int cases, caseno = 0;
	scanf("%d", &cases);
	//fill(tt, 0);
	while (cases--) {
	    scanf("%lld %lld", &l, &r);
	    //tt[f(r) - f(l - 1)]++;
        printf("Case #%d: %d\n", ++caseno, f(r) - f(l - 1));
	}
	/*fr(i, 1, 6)
        if (tt[i] > 0) printf("%d %d\n", i, tt[i]);*/
	return 0;
}
