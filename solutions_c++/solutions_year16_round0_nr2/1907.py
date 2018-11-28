#include <stdio.h>
char S[102];

int solve(void){
    int n = 1;
    int s = (S[0]=='-');
    char prev = S[0];    
    int i=1;
    while((S[i]=='+') || (S[i]=='-')){
        if(S[i]!=prev){
            prev = S[i];
            s = 1 - s;
            ++n;
        }
        ++i;
    }
    if(s==0){
        return n-1;
    }
    return n;
}

int main(){
    int T;
    scanf("%d\n", &T);
    for(int t=1;t<=T;++t){
        scanf("%s\n", S);
        int sol = solve();
        printf("Case #%d: %d\n", t, sol);
    }
}
