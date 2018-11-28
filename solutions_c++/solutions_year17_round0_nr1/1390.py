#include <stdio.h>

int T, ans, S, K;

bool pancakes[1001];
int main(){
    // freopen("/Users/depa/Downloads/A-large.in", "r", stdin);
    scanf("%d", &T);
    for(int t = 1; t <= T; ++t){
        S = 0;
        char s[1001];
        
        scanf("%s", s);
        for(int i = 0; s[i] != NULL; ++i){
            pancakes[i] = (s[i] == '+'? true: false);
            S++;
        }
        
        scanf("%d", &K);
        int ans = 0;
        for(int i = 0; i <= S - K; ++i){
            if(!pancakes[i]){
                for(int j=i; j < i+K; ++j){
                    pancakes[j] = !pancakes[j];
                }
                ans++;
            }
        }
        
        bool isPossibale = true;
        for(int i = 0; i < S; ++i){
            if(!pancakes[i]){
                isPossibale = false;
                break;
            }
        }
        if(isPossibale)
            printf("Case #%d: %d\n", t, ans);
        else
            printf("Case #%d: IMPOSSIBLE\n", t);
    }
    
    return 0;
}
