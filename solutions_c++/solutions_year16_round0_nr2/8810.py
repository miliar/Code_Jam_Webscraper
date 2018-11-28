#include <cstdio>

#define MAX_T 100
#define MAX_S 100

int T;
char S[MAX_S + 5];
int A[MAX_S + 5];
int num_S;

int solve(){
    int res = 0;
    for(int i=1; i<num_S; i++){
        if(A[i] != A[i-1]) res++;
    }
    if(A[num_S-1] == 0) res++;
    return res;
}

int main(){
    scanf("%d", &T);
    for(int t=1; t<=T; t++){
        scanf("%s", S);
        for(int i=0; S[i] != '\0'; i++){
            if(S[i] == '+') A[i] = 1;
            if(S[i] == '-') A[i] = 0;
            num_S = i+1;
        }
        printf("Case #%d: %d\n", t, solve());
    }
    return 0;
}
