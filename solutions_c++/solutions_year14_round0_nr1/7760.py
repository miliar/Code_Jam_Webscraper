#include<stdio.h>

int map[5][5];
int mpa[5][5];
int ans[102];

int magic()
{
   int ra,rb;
   scanf("%d",&ra);
   for(int i=1;i<=4;i++)
    for(int j=1;j<=4;j++)
     scanf("%d",&map[i][j]);
   scanf("%d",&rb);
   for(int i=1;i<=4;i++)
    for(int j=1;j<=4;j++)
     scanf("%d",&mpa[i][j]);
   int ch=0,kp;
   for(int i=1;i<=4;i++)
    for(int j=1;j<=4;j++)
     if(map[ra][i]==mpa[rb][j])
     {
       ch++;
       kp=map[ra][i];
     }
   if(ch==1)
    return kp;
   else if(ch==0)
    return 17;
   else
    return 0;
}

int main()
{
    int n;
    scanf("%d",&n);
    for(int i=1;i<=n;i++)
     ans[i]=magic();
    for(int i=1;i<=n;i++)
    {
      int f=ans[i];
      printf("Case #%d: ",i);
      if(f==17)
       printf("Volunteer cheated!");
      else if(f==0)
       printf("Bad magician!");
      else
       printf("%d",f);
      printf("\n");
    }
    scanf(" ");
    return 0;
}
