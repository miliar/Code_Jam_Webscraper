#include<cstdio>
#include<algorithm>

using namespace std;

int main(){
    bool Hash[10];
    int N, M, i , j, K, cnt;
    scanf("%d",&N);
    for(i=1;i<=N;i++){
        scanf("%d",&M);
        if(M==0){
            printf("Case #%d: INSOMNIA\n",i);
            continue;
        }
        for(j=0;j<10;j++)
            Hash[j] = 0;
        cnt = 10;
        for(j=1;cnt>0;j++){
            K = M*j;
            while(K>0){
                if(!Hash[K%10]){
                    Hash[K%10] = 1;
                    cnt--;
                }
                K /= 10;
            }
        }
        printf("Case #%d: %d\n",i, M*(j-1));
    }
}
