#include <cstdio>
#include <cstring>
#include <algorithm>
int pancake[1001], pan[1001], panpan[1001], panp[1001];
int main(){
    freopen("output.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int kase = 1; kase <= T; ++kase){
        memset(pancake, 0, sizeof(pancake));
        memset(pan, 0, sizeof(pan));
        memset(panpan, 0, sizeof(panpan));
        memset(panp, 0, sizeof(panp));
        int N;
        scanf("%d", &N);
        for(int i = 0; i < N; ++i){
            int x;
            scanf("%d", &x);
            ++pancake[x], ++pan[x], ++panpan[x], ++panp[x];
        }
        int ans = 9, x = 0;
        for(int i = 9; i >= 1; --i){
            if(!pancake[i]) continue;
            ans = std::min(ans, x+i);
            pancake[i%2 ? i/2+1 : i/2] += pancake[i];
            pancake[i/2] += pancake[i];
            x += pancake[i];
        }
        if(panpan[9]){
            x = panpan[9];
            panpan[4] += panpan[9];
            panpan[5] += panpan[9];
            for(int i = 8; i >= 1; --i){
                if(!panpan[i]) continue;
                ans = std::min(ans, x+i);
                panpan[i%2 ? i/2+1 : i/2] += panpan[i];
                panpan[i/2] += panpan[i];
                x += panpan[i];
            }
        }
        if(panp[9]){
            x = pan[9];
            panp[3] += panp[9];
            panp[6] += panp[9];
            for(int i = 8; i >= 1; --i){
                if(!panp[i]) continue;
                ans = std::min(ans, x+i);
                panp[i%2 ? i/2+1 : i/2] += panp[i];
                panp[i/2] += panp[i];
                x += panp[i];
            }
        }
        printf("Case #%d: %d\n", kase, ans);
    }
    fclose(stdout);
    return 0;
}