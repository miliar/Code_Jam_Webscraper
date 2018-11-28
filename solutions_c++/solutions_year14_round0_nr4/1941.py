#pragma  comment(linker, "/STACK:36777216")
#include <map>
#include <set>
#include <queue>
#include <cmath>
#include <vector>
#include <string>
#include <cstdio>
#include <iomanip>
#include <cstring>
#include <cassert>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#define  lc(x) (x<<1)
#define  rc(x) (lc(x)+1)
#define  PI    (acos(-1))
#define  EPS   1e-8
#define  MAXN  111
#define  MAXM  8888
#define  LL    long long
#define  ULL   unsigned long long
#define  INF   0x7fffffff
#define  pb    push_back
#define  mp    make_pair
#define  lowbit(x) (x&(-x))
#define  mod   1000000007

using namespace std;

int t, n, cas;

double a[1111], b[1111];

int gao1(){
    int ll = 1, res = 0;
    for(int i = 1; i <= n; i ++)
        if(a[i] >= b[ll]) res ++, ll ++;
    return res;
}

int gao2(){
    int now = 1, res = 0;
    for(int i = 1; i <= n; i ++)
        if(b[i] >= a[now]) res ++, now ++;
    return n - res;
}

int main(){
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    cin >> t;
    while(t --){
        scanf("%d", &n);
        for(int i = 1; i <= n; i ++) scanf("%lf", &a[i]);
        for(int i = 1; i <= n; i ++) scanf("%lf", &b[i]);
        sort(a + 1, a + 1 + n), sort(b + 1, b + 1 + n);
        /*for(int i = 1; i <= n; i ++) cout << a[i] << endl;
        cout << endl;
        for(int i = 1; i <= n; i ++) cout << b[i] << endl;
        */
        printf("Case #%d: %d %d\n", ++ cas, gao1(), gao2());
    }
}
