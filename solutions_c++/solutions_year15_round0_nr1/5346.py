#include <cstdio>

int T;
int Smax;
char Shy[1010];

int main(){
    scanf("%d", &T);
    for(int case_T=1 ; case_T<=T ; case_T++){
        scanf("%d", &Smax);
        scanf("%s", Shy);
        int sum = 0;
        int res = 0;
        for(int i=0;i<=Smax;i++){
            if('1' <= Shy[i]){
                if(sum < i){
                    res += i - sum;
                    sum = i;
                }
                sum += Shy[i] - '0';
            }
        }
        printf("Case #%d: %d\n", case_T, res);
    }
    return 0;
}