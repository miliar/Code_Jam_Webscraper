#include<stdio.h>
#include<conio.h>
#include<iostream.h>

void main()
{
 int cas,a,b,c,d,t1,t2;
 char game[4][4],r;
 freopen("1Al.in","r",stdin);
 freopen("1Al.out","w",stdout);
 scanf("%d",&cas);
 for(a=1;a<=cas;a++)
 {
  d=0,t1=10,t2=10;
  printf("Case #%d: ",a);
	  for(b=0;b<4;b++)
  {
   getchar();
   for(c=0;c<4;c++)
   {
    scanf("%c",&game[b][c]);
    if(game[b][c]=='T')
    {
     t1=b,t2=c;
    }
    if(game[b][c]=='.')
    {
     d=1;
    }
   }
  }
  getchar();
  int m,f=0;
  for(b=0;b<2;b++)
  {
   if(b==0)
   {
    game[t1][t2]='X';
   }
   if(b==1)
   {
    game[t1][t2]='O';
   }
    for(m=0;m<4;m++)
    {
     if((game[m][0]=='O'||game[m][0]=='X')&&(game[m][0]==game[m][1])&&(game[m][0]==game[m][2])&&(game[m][0]==game[m][3]))
     {
      r=game[m][0];
      f=1;
      break;
     }
     else if((game[0][m]=='O'||game[0][m]=='X')&&game[0][m]==game[1][m]&&game[0][m]==game[2][m]&&game[0][m]==game[3][m])
     {
     r=game[0][m];
      f=1;
      break;
     }
     else if((game[0][0]=='O'||game[0][0]=='X')&&game[0][0]==game[1][1]&&game[0][0]==game[2][2]&&game[0][0]==game[3][3])
     {
     r=game[0][0];
      f=1;
      break;
     }
     else if((game[0][3]=='O'||game[0][3]=='X')&&game[0][3]==game[1][2]&&game[0][3]==game[2][1]&&game[0][3]==game[3][0])
     {
      r=game[0][3];
      f=1;
      break;
     }
    }
  }
  if(r=='X'&&f==1)
  {
   printf("X won\n");
   continue;
  }
  if(r=='O'&&f==1)
  {
   printf("O won\n");
   continue;
  }
  if(d==1&&f==0)
  {
   printf("Game has not completed\n");
  }
  if(d==0&&f==0)
  {
   printf("Draw\n");
  }
 }
}