#include<stdio.h>
#include<stdlib.h>
int main(){
    int ca;
    int N;
    scanf("%d", &ca);
    for(int t=0;t<ca;t++){
        scanf("%d",&N);
        printf("Case #%d: ", t + 1);
        if(N == 0){
            printf("INSOMNIA\n");
            continue;
        }
        long long int now = 0;
        bool used[10];
        for(int i=0;i<10;i++)used[i] = false;
        while(1){
            now += N;
            long long int tmp = now;
            while(tmp != 0){
                used[tmp % 10] = true;
                tmp/=10;
            }
            bool allTrue = true;
            for(int i=0;i<10;i++){
                if(!used[i]){
                    allTrue = false;
                }
            }
            if(allTrue) break;
        }
        printf("%lld\n", now);
    }
    return 0;
}
