#include <stdio.h>
#include <string.h>
char data[1001];
int main(){
    freopen("test.in","r",stdin);
    freopen("large.out","w",stdout);
    int T;
    int tt = 1;
    scanf("%d",&T);
    while(T--){
        int m;
        scanf("%d ",&m);
        for(int i = 0;i <= m;i++){
            data[i] = getchar() - '0';
        }
        int sum = 0;
        int need = 0;
        for(int i = 0 ;i <= m;i++){
            if(sum < i){
                need += i - sum;
                sum = i + data[i];
            }else{
                sum += data[i];
            }
        }
        printf("Case #%d: %d\n",tt++,need);
    }
}