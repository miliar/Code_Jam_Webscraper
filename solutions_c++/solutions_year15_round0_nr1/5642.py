#include <cstdio>
#include <cstring>

int main(){
    freopen("2.inp", "r", stdin);
    freopen("2.out", "w", stdout);
    int t, sum, in, Max, len, p;
    char Inp[1005];
    scanf("%d", &t);
    for(int i = 1; i <= t; ++i){
        sum = in = 0;
        scanf("%d %s", &Max, Inp);
        len = strlen(Inp);
        for(int j = 0; j < len; ++j){
            p = Inp[j]-'0';
            if(sum < j){
                in+=j-sum;
                sum+=j-sum;
            }
            sum+=p;
        }
        printf("Case #%d: %d\n", i, in);
    }
    return 0;
}
