#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;

int main(){
    int runs, N, i, j, standing, cnt, ppl;
    char s[1002];
    scanf("%d", &runs);
    for(j=1; j<=runs; j++){
        scanf("%d%s", &N, s);
        //printf("%d_%s_", N, s);
        cnt = 0;
        standing = s[0] - 48;
        for(i=1; i<=N; i++){
            ppl = (s[i] - 48);
            if(standing < i && ppl>0){
                cnt += i - standing;
                standing += cnt;
            }
            standing += ppl;
        }
        printf("Case #%d: %d\n", j, cnt);
    }
}
