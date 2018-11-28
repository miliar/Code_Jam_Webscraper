#include<cstdio>
int main()
{
   // freopen("A_in.txt","r",stdin);
   // freopen("A_out.txt","w",stdout);
    int t,r1,r2,a[5][5],b[5][5],i,j,co=0,total,card;
    scanf("%d",&t);
    while(t--)
    {
      scanf("%d",&r1);
      for(i=1;i<=4;i++)
      for(j=1;j<=4;j++)
      scanf("%d",&a[i][j]);
      scanf("%d",&r2);
      for(i=1;i<=4;i++)
      for(j=1;j<=4;j++)
      scanf("%d",&b[i][j]);
      total=0;
      for(i=1;i<=4;i++)
      {
          for(j=1;j<=4;j++)
          if(a[r1][i]==b[r2][j]){ card=a[r1][i];total++;}
      }
      printf("Case #%d: ",++co);
      if(total==1)
      printf("%d\n",card);
      else if(total>1)
      printf("Bad magician!\n");
      else if(total==0)
      printf("Volunteer cheated!\n");
    }
    return 0;
}
