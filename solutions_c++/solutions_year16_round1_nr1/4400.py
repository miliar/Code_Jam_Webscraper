#include <cstdio>

char S[1100], ans[2100];

int main(){
    int T, tc = 0;
    scanf("%d", &T);
    
    while(T--){
        scanf("%s", S);
        
        int b = 1000, e = 1000;
        ans[1000] = S[0];
        
        for(int i=1; S[i]!='\0'; i++){
            if(S[i] >= ans[b]){
                ans[--b] = S[i];
            } else {
                ans[++e] = S[i];
            }
        }
        
        printf("Case #%d: ", ++tc);
        
        for(int i=b; i<=e; i++){
            printf("%c", ans[i]);
        }
        printf("\n");
    }
}
