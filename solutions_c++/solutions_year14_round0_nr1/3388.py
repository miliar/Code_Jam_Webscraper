#include <iostream>
#include<stdio.h>
#include<algorithm>
#include<string.h>
using namespace std;

int main()
{
    int t;
    scanf("%d",&t);
    FILE *ptr;
    ptr=fopen("file.txt","w");

    for(int i=1;i<=t;i++)
    {

      int row1,row2,arr[5],barr[5];
      scanf("%d",&row1);

      int mat[6][6];

      for(int j=1;j<=4;j++)
        for(int k=1;k<=4;k++)
         scanf("%d",&mat[j][k]);


      for(int j=1;j<=4;++j)
        arr[j]=mat[row1][j];

      scanf("%d",&row2);

      for(int j=1;j<=4;j++)
        for(int k=1;k<=4;k++)
         scanf("%d",&mat[j][k]);

      for(int j=1;j<=4;++j)
        barr[j]=mat[row2][j];

       int counts=0,ans;

       for(int j=1;j<=4;j++)
      {
          for(int k=1;k<=4;k++)
          {
              if(arr[j]==barr[k])
              {
                  counts++;
                  ans=arr[j];
              }
          }
      }


      if(counts==1)
        fprintf(ptr,"Case #%d: %d\n",i,ans);

      else if(counts==0)
        fprintf(ptr,"Case #%d: Volunteer cheated!\n",i);

      else
        fprintf(ptr,"Case #%d: Bad magician!\n",i);
    }
    fclose(ptr);
    return 0;
}
