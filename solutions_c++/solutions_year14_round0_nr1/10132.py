#include<stdio.h>
int main(){
    int t,loop;
    int s1,s2,num_match,i,j,value=0;
    int a[16],b[16];
    scanf("%d",&t);
    loop=1;
    while(t--){
        scanf("%d",&s1);
        for(i=0;i<16;i++)
            scanf("%d",&a[i]);
        scanf("%d",&s2);
        for(i=0;i<16;i++)
            scanf("%d",&b[i]);
        num_match=0;
        for(i=(s1-1)*4;i<(s1-1)*4+4;i++){
            for(j=(s2-1)*4;j<(s2-1)*4+4;j++){
                if(a[i]==b[j]){
                    num_match++;
                    value=a[i];
                    break;
                }
            }
        }
        if(num_match==0){
            printf("Case #%d: Volunteer cheated!",loop);
        }
        else if(num_match==1){
            printf("Case #%d: %d",loop,value);
        }else{
            printf("Case #%d: Bad magician!",loop);
        }
        if(t!=0){
            printf("\n");
        }
        loop++;
    }
return 0;
}
