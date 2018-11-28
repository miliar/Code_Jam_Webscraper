#include <cstdio>

int foo(int N){
    bool vis[10] = {0};
    int cnt = 0, i = 1;
    while(cnt != 10){
        int N2 = N*i;
        while(N2 > 0){
            if(vis[N2%10] == 0){
                vis[N2%10] = 1;
                cnt++;
            }
            N2 /= 10;
        }
        i++;
    }
    return i;
}

int main(){
    int T;
    scanf("%d", &T);
    int mx = 1;
    /*
    for(int i = 1 ; i <= 1000000 ; i++){
        int ret = foo(i);
        if(ret > mx) mx = ret;
    }
    printf("%d\n", mx);
    */
    for(int i = 1 ; i <= T ; i++){
        int N;
        scanf("%d", &N);
        if(N == 0)
            printf("Case #%d: INSOMNIA\n", i);
        else
            printf("Case #%d: %d\n", i, (foo(N)-1)*N);
    }
}
