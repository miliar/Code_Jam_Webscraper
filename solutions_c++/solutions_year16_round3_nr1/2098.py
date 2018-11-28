#include <cstdio>
int P[30];
int main(){
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    
    int T, N;
    scanf("%d",&T);
    
    for(int cases=1; cases<=T; cases++){
        printf("Case #%d:",cases);
        scanf("%d",&N);
        int tot=0, num=N, tmp1, tmp2, tmp3, tmp4;
        for(int i=1; i<=N; i++){
            scanf("%d",&P[i]);
            tot+=P[i];
        }
        while(tot){
            tmp1=tmp2=tmp3=tmp4=0;
            for(int i=1; i<=N; i++){
                if(P[i]>tmp1){
                    tmp1=P[i];
                    tmp2=i;
                }
            }
            tmp1=0;
            for(int i=1; i<=N; i++){
                if(P[i]>tmp1 && i!=tmp2){
                    tmp1=P[i];
                    tmp3=i;
                }
            }
            if(num>=3){
                tmp1=0;
                for(int i=1; i<=N; i++){
                    if(P[i]>tmp1 && i!=tmp2){
                        tmp1=P[i];
                        tmp4=i;
                    }
                }
            }
            if(num<=2){
                if(P[tmp3]==P[tmp2]){
                    printf(" %c%c",tmp2+'A'-1, tmp3+'A'-1);
                    tot-=2; P[tmp2]--; P[tmp3]--;
                }
                else{
                    printf(" %c",tmp2+'A'-1);
                    tot--; P[tmp2]--;
                }
            }
            else{
                if(tot-2>=P[tmp4]*2 && P[tmp3]==P[tmp2]){
                    printf(" %c%c",tmp2+'A'-1, tmp3+'A'-1);
                    tot-=2; P[tmp2]--; P[tmp3]--;
                    if(!P[tmp2]) num--;
                    if(!P[tmp3]) num--;
                }
                else{
                    printf(" %c",tmp2+'A'-1);
                    tot--; P[tmp2]--;
                    if(!P[tmp2]) num--;
                }
            }

        }
        printf("\n");
    }
    return 0;
}
