#include<stdio.h>

int main()
{

    freopen("ques11.in","r+",stdin);
    freopen("out11.out","w+",stdout);

    int t;
    scanf("%d",&t);

    int k=0;
    while(t--)
     {
         k++;
         int i,j;

         int xx;
         scanf("%d",&xx);

         int mat1[4][4];

         for(i=0;i<4;i++)
           for(j=0;j<4;j++)
              scanf("%d",&mat1[i][j]);

         int yy;
         scanf("%d",&yy);

         int mat2[4][4];

         for(i=0;i<4;i++)
           for(j=0;j<4;j++)
              scanf("%d",&mat2[i][j]);


         int count=0;
         int ans;

         for(i=0;i<4;i++)
           {
               for(j=0;j<4;j++)
                 {
                     if(mat1[xx-1][i] == mat2[yy-1][j])
                       {
                           count++;
                           ans=mat1[xx-1][i];
                       }
                 }
           }


         if(count==1)
           printf("Case #%d: %d\n",k,ans);
         else if(count==0)
           printf("Case #%d: %s\n",k,"Volunteer cheated!");
         else if(count>1)
           printf("Case #%d: %s\n",k,"Bad magician!");

     }
    return 0;
}
