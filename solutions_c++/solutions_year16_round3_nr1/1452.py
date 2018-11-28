#include<bits/stdc++.h>
using namespace std;
int main(){
    freopen("A-large.in","r",stdin);
    freopen("yLarge.txt","w",stdout);
    int T,N,P[27];
    scanf("%d",&T);
    for(int t=1;t<=T;++t){
        memset(P,0,sizeof(P));
        scanf("%d",&N);
        for(int i=0;i<N;++i)
            scanf("%d",&P[i]);
        printf("Case #%d: ",t);
        while(1){
            int sum=0;
            int num=0;
            int max=0;
            for(int i=0;i<N;++i){
                if(P[i]>max){
                    max=P[i];
                    num=i;
                }
                sum+=P[i];
            }
            //printf("%d\n",sum);
            if(sum==0)
                break;
            sum--;
            printf("%c",num+'A');
            P[num]--;
            for(int i=0;i<N;++i){
                if(P[i]*2>sum){
                    P[i]--;
                    printf("%c",i+'A');
                    break;
                }
            }
            printf(" ");
        }
        printf("\n");
    }
    return 0;
}
