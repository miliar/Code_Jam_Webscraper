#include<stdio.h>
int a[5][5],b[5][5];
int main()
{
  freopen("A-small-attempt0.in","r",stdin);
  freopen("out.txt","w",stdout);
  int t,i,j,k;
  scanf("%d",&t);
  for(k=1;k<=t;k++)
  { int n1,n2;
    scanf("%d",&n1);
    for(i=0;i<4;i++)
    {
       for(j=0;j<4;j++)
           {
             scanf("%d",&a[i][j]);
           }
    }
    scanf("%d",&n2);
    for(i=0;i<4;i++)
    {
       for(j=0;j<4;j++)
           {
            scanf("%d",&b[i][j]);
           }
    }
    int count=0,x;
    for(j=0;j<4;j++)
    {
      for(i=0;i<4;i++)
      {
        if(a[n1-1][j]==b[n2-1][i])
            {
             count++;
             x=a[n1-1][j];
            }
      }
    }
    if(count==1)
        printf("Case #%d: %d\n",k,x);
    else if(count==0)
            printf("Case #%d: Volunteer cheated!\n",k);
    else
        printf("Case #%d: Bad magician!\n",k);

  }
  return 0;
}
