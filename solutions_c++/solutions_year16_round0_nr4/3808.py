#include<stdio.h>
#include<string.h>



int main(void){
    int i,j,xx=1,x,y,z,test,n,m;
    char shin[500];

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    scanf("%d",&test);
    while(xx<=test){
        scanf("%d %d %d",&x,&y,&z);
        printf("Case #%d:",xx);
        for(i=1;i<=x;i++){
            printf(" %d",i);
        }
        printf("\n");

        xx++;
    }
    return 0;
}

