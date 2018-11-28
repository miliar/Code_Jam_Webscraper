#include <stdio.h>
#include <string.h>

typedef unsigned long long ull;

int main(void){
    int i, t, nums[10], cont, n, caso = 1, flag;
    ull x, ans;

    scanf("%d", &t);
    while(t--){
        flag = 0;
        cont = 10;
        memset(nums, 0, sizeof(nums));
        scanf("%d", &n);
        for(i = 1; cont ; i++){
            ans = x = n * i;
            while(x){
                if(!nums[x % 10]){ nums[x % 10]++; cont--; }
                x /= 10;
            }
            if (i > 100){ flag = 1; break;}
        }
        printf("Case #%d: ", caso++);
        if(!flag) printf("%llu\n", ans);
        else printf("INSOMNIA\n");
    }



    return 0;
}
