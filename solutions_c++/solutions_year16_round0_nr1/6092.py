#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#define LL long long

using namespace std;


int main(void){
    int T, kase = 0;
    scanf("%d", &T);
    while(T--){
        int N, M, cnt = 0;
        bool vis[10];
        memset(vis, 0, sizeof(vis));
        scanf("%d", &N);
        for(int i = 1; i <= 10000; i++){
            M = i * N;
            for(int tmp = M; tmp; tmp /= 10){
                 if(!vis[tmp % 10]){
                     vis[tmp % 10] = true;
                     cnt++;
                 }
                 if(cnt == 10) goto ans;
            }
        }
ans:
        printf("Case #%d: ", ++kase);
        if(cnt != 10) puts("INSOMNIA");
        else printf("%d\n", M);
    }

    return 0;
}

