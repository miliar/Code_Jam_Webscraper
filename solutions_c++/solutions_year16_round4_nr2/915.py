/***************************************
      zzblack                         **
      2016-05-28                      **
      Orz                             **
****************************************/
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <cmath>
#include <string>
#include <cctype>
#include <cstdio>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;
#define ls id<<1,l,mid
#define rs id<<1|1,mid+1,r
#define OFF(x) memset(x,-1,sizeof x)
#define CLR(x) memset(x,0,sizeof x)
#define MEM(x) memset(x,0x3f,sizeof x)
typedef long long ll ;
typedef pair<int,int> pii ;
const int maxn = 1e5 + 50 ;
const int maxm = 1e6 + 50;
const double eps = 1e-10;
const int max_index = 62;
const int inf = 0x3f3f3f3f ;
const int MOD = 1e9+7 ;

inline int read(){
    char c = getchar();
    while (!isdigit(c)) c = getchar();
    int x = 0;
    while (isdigit(c)) {
        x = x * 10 + c - '0';
        c = getchar();
    }
    return x;
}

double p[250];

int main () {
#ifdef LOCAL
	freopen("C:\\Users\\zzblack\\Desktop\\case.in","r",stdin);
      freopen("C:\\Users\\zzblack\\Desktop\\case.out","w",stdout);
#endif

    int T = read(), cas = 1;
    while (T--) {
        int n = read(), k = read();
        for (int i = 0; i < n; i++) scanf("%lf", &p[i]);
        double ans = 0;
        for (int i = 0; i < 1 << n; i++) {
            if (__builtin_popcount(i) != k) continue;
            double tmp = 0;
            for (int j = i; j; j = (j-1) & i) {
                double t = 1;
                if(__builtin_popcount(j) != k >> 1) continue;
                for (int m = 0; m < n; m++) {
                    if ((i >> m & 1) == 0) continue;
                    if(j >> m & 1) t *= p[m];
                    else t *= 1-p[m];
                }
                tmp += t;
            }
            ans = max(ans, tmp);
        }
        printf("Case #%d: %.10f\n", cas++, ans);
    }

	return 0;
}
