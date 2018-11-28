#include<stdio.h>

int N;

int process(){
    if(N == 0) return -1;
    int c[10]={0,}, i, M = N, x, cnt = 0;
    while(1){
        x = M;
        while(x>0){
            if(c[x%10] == 0){
                cnt++;
                c[x%10] = 1;
            }
            x /= 10;
        }
        if(cnt == 10){
            return M;
        }
        M += N;
    }
}

int main(){
    int T, t;
    scanf("%d",&T);
    for(t=1;t<=T;t++){
        scanf("%d",&N);
        int res = process();
        printf("Case #%d: ", t);
        if(res == -1) printf("INSOMNIA\n");
        else printf("%d\n",res);
    }
    return 0;
}
