#include <stdio.h>

int main(){
    int T;
    scanf("%d", &T);
    for(int i=0; i<T; i++){
        char S[105];
        int ans=0, k;
        scanf("%s", S);
        printf("Case #%d: ", i+1);
        // DO NOT FORGET CASES WHERE |S| = 1
        for(k=1; S[k]!='\0'; k++){
            if(S[k] == S[k-1]) continue;
            if(S[k] == '-') S[k-1] = '-';
            else S[k-1] = '+';
            ans++;
        }
        if(S[k-1] == '-') ans++;
        printf("%d", ans);
        printf("\n");
    }
}