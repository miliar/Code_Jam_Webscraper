/***************************************
      zzblack                         **
      2016-05-29                      **
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

char mp[10][10];
int a[5];
int n;
int used[5];

bool dfs(int id, int Sta) {
    if(id == n) {
        return 1;
    }
    int ccc = 0;
    for (int i = 0; i < n; i++) {
        if(used[i]) continue;
        int num = n * n - (a[id] * n + i) - 1;
        if ((Sta >> num & 1) == 0) continue;
        ccc++;
        used[i] = 1;
        if (dfs(id+1, Sta) == 0) return 0;
        used[i] = 0;
    }
    return ccc != 0;
}

bool check(int Sta) {
    for (int i = 0; i < n; i++) a[i] = i;
    do {
        CLR(used);
        if (!dfs(0, Sta)) return 0;
    } while (next_permutation(a, a + n));
//    puts("***");

    return 1;
}

int main () {
#ifdef LOCAL
	freopen("C:\\Users\\zzblack\\Desktop\\case1.in","r",stdin);
      freopen("C:\\Users\\zzblack\\Desktop\\case2.out","w",stdout);
#endif

    int T = read(), cas = 1;
    while (T--) {
        n = read();
        for (int i = 0; i < n; i++) scanf("%s", mp[i]);
        int s = n * n;
        int sta = 0, ans = 100;
        for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++){
            sta <<= 1;
            if(mp[i][j] == '1') sta++;
        }
        for (int m = 0; m < 1 << s; m++) {
            if (m & sta) continue;
            if (check(m | sta)) {
                ans = min(ans, __builtin_popcount(m));
//                printf("%d\n", __builtin_popcount(m));
            }
        }
        printf("Case #%d: %d\n", cas++, ans);


    }

	return 0;
}
