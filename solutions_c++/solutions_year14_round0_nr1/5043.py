#include<stdio.h>
#include<conio.h>
void main()
{
clrscr(); int flag=0,c;
int a1[4][4];int t1[4],t2[4];
int a2[4][4];
int n1,n2,t;
scanf("%d",&t);
for(int x=0;x<t;x++)
{

  scanf("%d",&n1);
  for(int x1=0;x1<4;x1++)
  {
   for(int y1=0;y1<4;y1++)
   {
    scanf("%d",&a1[x1][y1]);
   }
  }
  for(int z1=0;z1<4;z1++)
  {
   t1[z1]=a1[n1][z1];
   }
   scanf("%d",&n2);
   for(int x2=0;x2<4;x2++)
   {
   for(int y2=0;y2<4;y2++)
   {
   scanf("%d",&a2[x2][y2]);
   }
   }
   for(int z2=0;z2<4;z2++)
   t2[z2]=a2[n2][z2];
   for(int b1=0;b1<4;b1++)
   {
    for(int b2=0;b2<4;b2++)
    {
      if(t1[b1]==t2[b2])
      {
      flag++;
      c=t1[b1];
      }

  } }
  clrscr();
  printf("Case #");
  printf("%d",(x+1));
  printf(": ");
  if(flag==0)
  printf("volunteer cheater");
  if(flag==1)
  printf("%d",c);
  if(flag>1)
  printf("bad magician");
  printf("\n");
}
getch();
}



