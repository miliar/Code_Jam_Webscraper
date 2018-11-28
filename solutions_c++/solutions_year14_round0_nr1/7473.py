#include <cstdio>
int arr[20];
int main(){
    int T,flag,ans,row,d;
    scanf("%d",&T);
    for(int k=1;k<=T;k++){
        for(int i=1;i<=16;i++) arr[i]=0;
         scanf("%d",&row);
         for(int i=1;i<=4;i++)
            for(int j=1;j<=4;j++){
                scanf("%d",&d);
                if(i==row)
                    arr[d]=i;
            }
            flag=ans=0;
        scanf("%d",&row);
         for(int i=1;i<=4;i++)
            for(int j=1;j<=4;j++){
                scanf("%d",&d);
                if(i==row&&arr[d]>0){
                    if(ans>0) flag=1;
                      ans=d;
                }
            }
        printf("Case #%d: ",k);
        if(flag) printf("Bad magician!\n");
        else if(ans==0) printf("Volunteer cheated!\n");
        else if(flag==0) printf("%d\n",ans);
    }
   return 0;
}
