#include<cstdio>
int main()
{
    int i,j,k,t,a[2][4][4],arr[2],count,res,l;
    scanf("%d",&t);
    l=1;
    while(l<=t){
        for(i=0;i<2;i++)
        {
            scanf("%d",&arr[i]);
            for(j=0;j<4;j++){
                for(k=0;k<4;k++){
                    scanf("%d",&a[i][j][k]);
                }
            }
        }
        arr[0]--;
        arr[1]--;
        count=0;
        res=0;
        for(i=0;i<4;i++){
            for(j=0;j<4;j++){
                if(a[0][arr[0]][i]==a[1][arr[1]][j]){
                    res=a[0][arr[0]][i];
                    count++;
                }
            }
        }
        printf("Case #%d: ",l);
        if(count==1){
            printf("%d",res);
        }
        else if(count==0){
            printf("Volunteer cheated!");
        }
        else{
            printf("Bad magician!");
        }
        printf("\n");
        l++;
    }
    return 0;
}
