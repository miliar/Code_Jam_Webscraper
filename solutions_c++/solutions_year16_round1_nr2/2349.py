#include<stdio.h>

int check[2501];
int main(){
    int test;
    scanf("%d",&test);
    for(int kk =1; kk<=test;kk++){
        int n;
        scanf("%d",&n);
        for(int i=1;i<=2500;i++){
            check[i] = 0;
        }
        for(int i=1;i<=2*n-1;i++){
            for(int j=1;j<=n;j++){
                int x;
                scanf("%d",&x);
                check[x] ++;
            }
        }
        printf("Case #%d: ",kk);
        for(int i=1;i<=2500;i++){
            if(check[i]%2 == 1){
                printf("%d ",i);
            }
        }
        printf("\n");
    }

}