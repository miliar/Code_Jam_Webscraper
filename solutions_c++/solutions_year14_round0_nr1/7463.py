#include <stdio.h>

int main()
{
  int n;
  int flag[100];
  int num[100];
  scanf("%d",&n);
  for(int i=0;i<n;i++)
  {
    flag[i]=0;
    int a[4][4];
    int b[4][4];
    int x,y;
    scanf("%d",&x);
    for(int ai=0;ai<4;ai++)
        scanf("%d%d%d%d",&a[ai][0],&a[ai][1],&a[ai][2],&a[ai][3]);
    scanf("%d",&y);
    for(int bi=0;bi<4;bi++)
        scanf("%d%d%d%d",&b[bi][0],&b[bi][1],&b[bi][2],&b[bi][3]);
    for(int test1=0;test1<4;test1++)
    {
        for(int test2=0;test2<4;test2++)
        {
            if(a[x-1][test1]==b[y-1][test2])
            {
                flag[i]++;
                num[i]=a[x-1][test1];
            }
        }
    }

  }

  for(int j=0;j<n;j++)
  {
   if(flag[j]==0)
   {
       printf("Case #%d: Volunteer cheated!\n",j+1);
   }

   else if(flag[j]==1)
   {
      printf("Case #%d: %d\n",j+1,num[j]);
   }

   else if(flag[j]>1)
   {
       printf("Case #%d: Bad magician!\n",j+1);
   }

  }

    return 0;
}
