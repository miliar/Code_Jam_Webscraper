#include<stdio.h>
#include<string.h>
int a[4][4],b[4][4];
int main(){
    int ca,cc,i,j;
    int r1,r2;
    int sum,ans;
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%d",&ca);
    for (cc=1;cc<=ca;cc++){
         printf("Case #%d: ",cc);
         scanf("%d",&r1);
         for (i=0;i<4;i++)
             for (j=0;j<4;j++) scanf("%d",&a[i][j]);
         scanf("%d",&r2);
         for (i=0;i<4;i++)
             for (j=0;j<4;j++) scanf("%d",&b[i][j]);
         r1--;
         r2--;
         sum=0;
         for (i=0;i<4;i++)
             for (j=0;j<4;j++)
                 if (a[r1][i]==b[r2][j]) sum++,ans=a[r1][i];
         
         if (sum==0) printf("Volunteer cheated!\n");
         else if (sum>1) printf("Bad magician!\n");
         else printf("%d\n",ans);
    }
    return 0;
}
           
