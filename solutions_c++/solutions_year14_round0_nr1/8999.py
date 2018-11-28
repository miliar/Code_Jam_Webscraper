#include<stdio.h>
int T,resp,resp2,aux,numeros[20],numeros2[20],res,num;
int main(){
    scanf("%d",&T);
    for(int caso=1;caso<=T;caso++){
        res=0;
        scanf("%d",&resp);
        for(int i=1;i<=4;i++){
           for(int j=1;j<=4;j++){
              scanf("%d",&aux);
              numeros[aux]=i;
           }
        }
        scanf("%d",&resp2);
        for(int i=1;i<=4;i++){
           for(int j=1;j<=4;j++){
              scanf("%d",&aux);
              numeros2[aux]=i;
           }
        }
        for(int i=1;i<=16;i++){
            if(numeros[i]==resp&&numeros2[i]==resp2){
                res++;
                num=i;
            }
        }
        switch(res){
            case 0:
                printf("Case #%d: Volunteer cheated!\n",caso);
            break;
            case 1:
                printf("Case #%d: %d\n",caso,num);
            break;
            default:
                printf("Case #%d: Bad magician!\n",caso);
            break;
        }
    }
    return 0;
}
