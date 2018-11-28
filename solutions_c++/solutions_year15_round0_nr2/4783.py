#include <iostream>
#include <cstdio>

using namespace std;

const int MAXN = 1010;

int ar[MAXN],N,M;

void solve(){
    scanf("%d",&N);
    for(int i = 0; i < N; i++)
        scanf("%d",&ar[i]);
    
    int ans = 2e9;
    for(int x = 1; x <= 1000; x++){
        int t = x;
        for(int i = 0; i < N; i++){
            t += (ar[i] - 1) / x;
        }
        ans=min(ans, t);
    }
    printf("%d\n", ans);
}

int main(){
    scanf("%d",&M);
    
    for(int i = 1; i <= M; i++){
        printf("Case #%d: ", i);
        solve();
    }
    
    return 0;
}
