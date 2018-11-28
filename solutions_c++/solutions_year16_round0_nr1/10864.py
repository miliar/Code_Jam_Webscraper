#include <cstdio>

int main(){
    int Case, n;
    bool dig[10] = {false};
    bool f = true;
    FILE *fPtr;
    fPtr = freopen("output.txt", "w", stdout);

    scanf("%d", &Case);
    for(int c = 1; c <= Case; c++){
        scanf("%d", &n);

        for(int i = 0; i < 10; i++) dig[i] = false;

        long long ans;
        for(int i = 1;;i++){
            ans = n * i;
            if(ans == n * (i - 1)){
                f = false;
                break;
            }

            long long tmp = ans;
            while(tmp >= 10){
                dig[tmp % 10] = true;
                tmp = tmp / 10;
            }
            dig[tmp] = true;

            int k = 0;
            for(k = 0; k < 10; k++){
                if(!dig[k]) break;
            }
            if(k == 10){
                f = true;
                break;
            }
        }
        if(!f) printf("Case #%d: INSOMNIA\n", c);
        else printf("Case #%d: %lld\n", c, ans);
    }
    return 0;
}
