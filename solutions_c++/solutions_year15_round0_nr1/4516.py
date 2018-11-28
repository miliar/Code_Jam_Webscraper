#include<stdio.h>
#include<string.h>
char A[1100];
int main(){
    int T, S, i, j, sum, cnt;
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    scanf("%d", &T);
    for(i=1; i<=T; i++){
        scanf("%d", &S);
        scanf("%s", A);
        sum=cnt=0;
        for(j=0; j<strlen(A); j++){
            if(A[j]=='0') continue;
            if(j<=sum) sum+=A[j]-'0';
            else{
                cnt+=j-sum;
                sum+=j-sum+A[j]-'0';
            }
        }
        printf("Case #%d: %d\n", i, cnt);
    }
    return 0;
}
