#include<stdio.h>
#include<conio.h>
#include<iostream.h>


int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t,ans,i,j,x=1,count,a1,a2;
    int a[4][4],b[4][4];
    scanf("%d",&t);
    while(x<=t){
                int check[17]={0};
                count=0;
                ans=0;
                scanf("%d",&a1);
                a1--;
                for(i=0;i<4;i++){
                                 for(j=0;j<4;j++){
                                                  scanf("%d",&a[i][j]);
                                 }
                }
                                 
                 
               for(i=0;i<4;i++){
                                check[a[a1][i]]=1;
                                
               }
               
               scanf("%d",&a2);
               a2--;
                for(i=0;i<4;i++){
                                 for(j=0;j<4;j++){
                                                  scanf("%d",&b[i][j]);
                                 }
                }
                
                for(i=0;i<4;i++){
                                 if(check[b[a2][i]]==1){
                                                       count++;
                                                       ans=b[a2][i];
                                 }
                }
                
                
                printf("Case #%d: ",x);
                if(count==1)
                            printf("%d\n",ans);
                else if(count==0)
                                 printf("Volunteer cheated!\n");
                else
                                 printf("Bad magician!\n");
               
    x++;
    }
    return 0;
}
