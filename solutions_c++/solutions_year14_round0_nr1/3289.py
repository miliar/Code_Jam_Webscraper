#include<stdio.h>
int main(){
    int a[4][4],b[4][4],m,n,T,X;
    scanf("%d",&T);
    X=T;
    while(T--){
    int count=0,num;
    scanf("%d",&m);
    for(int i=0;i<4;i++)
        for(int j=0;j<4;j++){
            scanf("%d",&a[i][j]);
        }
        scanf("%d",&n);
    for(int i=0;i<4;i++)
        for(int j=0;j<4;j++){
            scanf("%d",&b[i][j]);
        }
    for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
     {       if(a[m-1][i]==b[n-1][j]){
                count++;
                num=a[m-1][i];
            }
            if(count>1)
                break;
    }
       if(count>1)
        printf("Case #%d: Bad magician!\n",X-T);
    else
        if(count==1)
            printf("Case #%d: %d\n",X-T,num);
            else
            printf("Case #%d: Volunteer cheated!\n",X-T);

}
}


