#include <stdio.h>
#include <memory.h>

int main(){
    int t, n;
    int hash[20];
    scanf("%d", &t);
    for (int i = 1; i <= t; i ++){
        memset(hash, 0, sizeof(hash));
        scanf("%d", &n);
        for (int j = 1; j <= 4; j ++){
            for (int k = 1; k <= 4; k ++){
                int tmp;
                scanf("%d", &tmp);
                if(j == n){
                    hash[tmp] = 1;
                }
            }
        }
        scanf("%d", &n);
        int res = 0, ans;
        for (int j = 1; j <= 4; j ++){
            for (int k = 1; k <= 4; k ++){
                int tmp;
                scanf("%d", &tmp);
                if(j == n){
                    if(hash[tmp]){
                        res ++;
                        ans = tmp;
                    }
                }
            }
        }
        if(res == 1){
            printf("Case #%d: %d\n", i, ans);
        }
        else if(res == 0){
            printf("Case #%d: Volunteer cheated!\n", i);
        }
        else{
            printf("Case #%d: Bad magician!\n", i);
        }
    }
    return  0;
}
