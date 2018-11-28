//source here#pragma  comment(linker, "/STACK:36777216")
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
#define  MAXN  444
#define  MAXM  44444
#define  LL    long long
#define  ULL   unsigned long long
#define  INF   0x3fffffff
#define  pb    push_back
#define  mp    make_pair
#define  mod   1000000007
#define  lowbit(x) (x&(-x))

using namespace std;

int s[22], n, t, x, cas;

int gao(){
    int pos, cnt = 0 ;
    for(int i = 1; i <= 16; i ++)
        if(s[i] == 2) cnt ++, pos = i;
    if(cnt > 1) return -1;
    if(cnt == 0) return -2;
    return pos;
}

int main(){
    //freopen("read.in", "r", stdin);
    //freopen("ans.txt", "w", stdout);

    cin >> t;
    while(t --){
        scanf("%d", &n);
        memset(s, 0, sizeof(s));
        for(int i = 1; i <= 4; i ++)
            for(int j = 1; j <= 4; j ++){
                scanf("%d", &x);
                if(i == n) s[x] ++;
            }
        scanf("%d", &n);
        for(int i = 1; i <= 4; i ++)
            for(int j = 1; j <= 4; j ++){
                scanf("%d", &x);
                if(i == n) s[x] ++;
            }
        printf("Case #%d: ", ++ cas);
        int k = gao();
        if(k == -1) printf("Bad magician!\n");
        else if(k == -2) printf("Volunteer cheated!\n");
        else printf("%d\n", k);
    }
}
