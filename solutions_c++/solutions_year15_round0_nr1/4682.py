#include<stdio.h>
#include<stdlib.h>
int main(){
    int T;
    scanf("%d",&T);
    for(int ca=0;ca<T;ca++){
        int ans = 0;
        int sum = 0;
        char str[1024];
        int s;
        scanf("%d %s",&s,str);
        for(int i=0;i<=s;i++){
            if(i > sum){
                int now = (i - sum);
                sum += now;
                ans += now;
            }
            sum += str[i] - '0';
        }
        printf("Case #%d: %d\n", ca + 1, ans);
    }
    return 0;
}
