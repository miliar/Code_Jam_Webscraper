#include<stdio.h>

int main(){

    freopen("A-large.in", "r", stdin);
    freopen("file.txt", "w", stdout);

    int T;
    bool used[50], r = false;
    long long N, v, t;

    scanf("%d", &T);

    for(int cas = 0; cas < T; ++cas){
        scanf("%lld", &N);

        for(int i = 0; i < 20; ++i){
            used[i] = false;
        }

        v = N; r = false;
        for(int i = 0; i < 1111; ++i){
            t = v;
            used[t % 10] = true;
            while(t > 0){
                used[t % 10] = true;
                t /= 10;
            }

            r = true;
            for(int j = 0; j < 10; ++j){
                if(used[j] == false){
                    r = false;
                    break;
                }
            }

            if(r == true)
                break;

            v += N;
        }

        printf("Case #%d: ", cas + 1);

        if(r == false)
            printf("INSOMNIA\n");
        else
            printf("%lld\n", v);
    }


return 0;
}
