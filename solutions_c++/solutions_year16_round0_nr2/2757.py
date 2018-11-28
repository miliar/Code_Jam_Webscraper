#include<stdio.h>
#include<string.h>

int l;
char S[101];

int process(){
    l = strlen(S);
    int i, cnt = 0;
    for(i=1;i<l;i++){
        if(S[i] != S[i-1]) cnt++;
    }
    if(S[l-1] == '-') cnt++;
    return cnt;
}

int main(){
    int T, t;
    scanf("%d",&T);
    for(t=1;t<=T;t++){
        scanf("%s",S);
        int res = process();
        printf("Case #%d: %d\n", t, res);
    }
    return 0;
}
