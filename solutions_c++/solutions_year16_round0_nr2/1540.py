#include <cstdio>
#include <cstring>

char S[110];

int main(){
    int T, tc = 0;
    scanf("%d", &T);
    
    while(T--){
        scanf("%s", S);
        
        int cnt = 0;
        for(int i=1; S[i]!='\0'; i++){
            if(S[i] != S[i-1]) cnt++;
        }
        
        if(S[strlen(S)-1] == '-') cnt++;
        
        printf("Case #%d: %d\n", ++tc, cnt);
    }
}
