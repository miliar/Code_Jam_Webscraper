#include<iostream>
#include<cassert>
#include<cstring>
#include<algorithm>
#include<cmath>
#include<cstdio>
#include<string>
#include<vector>
#include<cstdlib>
#include<iterator>
#include<ctime>
#include<map>
#include<sstream>
#include<set>
#include<cctype>
#include<queue>
#include <memory.h>

using namespace std;

#define all(c) (c).begin(), (c).end()

template<typename T> inline string intToString(T x){ostringstream q;q << x;return q.str();}
template<typename T> inline T myPow(T x, T n, T MOD){T res = 1;while (n>0) {if (n & 1) {res = 1ll*res * x % MOD;}x = 1ll*x * x % MOD;n/=2;}return res;}
template<typename T> inline T gcd(T a, T b){a=abs(a);b=abs(b);while ((a>0) && (b>0)) {if (a>b)a%=b;else b%=a;}return a+b;}


typedef unsigned long long LLong;
typedef long double LDb;
int n,x;
int a[11111];
int main()
{
#ifdef m0stik
    freopen("input.txt","r",stdin);
    freopen("output.txt", "w", stdout);
#endif
    int test;
    cin >> test;
    for (int it = 0; it < test; ++it) {
        printf("Case #%d: ", it+1);
        cin >> n >> x;
        for (int i = 0; i < n; ++i) {
            int q;
            scanf("%d", &q);
            ++a[q];
        }
        int res = 0;
        for (int i = x; i>=0; --i) {
            while (i+i<=x && a[i]>1) {
                res++;
                a[i]-=2;
            }
            for (int j = i-1; j>=0; --j) {
                while (i+j<=x && a[i]>0 && a[j]>0) {
                    res++;
                    a[i]--;
                    a[j]--;
                }
            }
        }
        for (int i = 0; i <= x; ++i) {
            res+=a[i];
            a[i] = 0;
        }
        printf("%d\n", res);
    }

    return 0;
} 