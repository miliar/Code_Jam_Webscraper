#include<stdio.h>
int main(){
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    int T, N, cnt, tmp, i, cases;
    scanf("%d",&T);
    for(cases=1; cases<=T; cases++){
        printf("Case #%d: ",cases);
        scanf("%d",&N);
        if(N==0){puts("INSOMNIA"); continue;}
        cnt=0;
        for(i=1; i<=100; i++){
            tmp=N*i;
            while(tmp){
                cnt|=1<<(tmp%10);
                tmp/=10;
            }
            if(cnt==1023) break;
        }
        printf("%d\n",N*i);
    }
    return 0;
}
