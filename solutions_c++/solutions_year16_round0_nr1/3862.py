#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <string>
#include <cstdlib>
#include <queue>
#include <stack>
#include <cmath>
#include <vector>
#include <map>

#define ll long long
#define ull unsigned long long
#define lson l, m, rt<<1
#define rson m+1, r, rt<<1|1

using namespace std;

const int inf = 0x3f3f3f3f;
const int M = 102;

char a[M], ch[M];

int vis[10];

int main(){

    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for(int cas = 1; cas <= t; cas++){
        ll n;
        int isok = 0;
        memset(vis, 0, sizeof(vis));
        scanf("%lld", &n);
        ll tmp = n;
        int f = 0;
        ll i;
        for(i = 1; i <= 1000000; i++){
            tmp = n*i;
            while(tmp){
                int g = tmp%10;
                tmp /= 10;
                if(!vis[g]){
                    vis[g] = 1;
                    isok++;
                    if(isok == 10){
                        f = 1;
                        break;
                    }
                }
            }
            if(f)
                break;
        }
        if(f)
            printf("Case #%d: %lld\n", cas, n*i);
        else
            printf("Case #%d: INSOMNIA\n", cas);
    }


    return 0;
}









