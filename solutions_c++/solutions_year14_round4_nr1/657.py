/*
 * Author:  xioumu
 * Created Time:  2014/5/31 22:07:24
 * File Name: A.cpp
 * solve: A.cpp
 */
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<string>
#include<map>
#include<set>
#include<iostream>
#include<vector>
#include<queue>

using namespace std;
#define sz(v) ((int)(v).size())
#define rep(i, n) for (int i = 0; i < (n); ++i)
#define repf(i, a, b) for (int i = (a); i <= (b); ++i)
#define repd(i, a, b) for (int i = (a); i >= (b); --i)
#define clr(x) memset(x,0,sizeof(x))
#define clrs( x , y ) memset(x,y,sizeof(x))
#define out(x) printf(#x" %d\n", x)
#define sqr(x) ((x) * (x))
typedef long long lint;

const int maxint = -1u>>1;
const double eps = 1e-8;
const int maxn = 10000 + 10;

int sgn(const double &x) {  return (x > eps) - (x < -eps); }

int a[maxn], n, m;

int main() {
    int T, ca;
    freopen("A.out", "w", stdout);
    scanf("%d", &T);
    repf (ca, 1, T) {
        scanf("%d%d", &n, &m);
        rep (i, n)
            scanf("%d", &a[i]);
        sort(a, a + n);
        int ans = 0;
        int i = 0, j = n - 1;
        while (i <= j) {
            if (i == j) {  
                ans++;
                i++;
            }
            else {
                if (a[i] + a[j] <= m) {
                    i++, j--;
                }
                else j--;
                ans++;
            }
        }
        printf("Case #%d: %d\n", ca, ans);
    }
    return 0;
}
