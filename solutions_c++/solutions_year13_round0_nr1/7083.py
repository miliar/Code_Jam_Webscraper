#include<iostream>
#include<stdio.h>
#include<conio.h>

using namespace std;

int main()
{freopen("input.in","r",stdin);
freopen("output.out","w",stdout);
int c,k;
scanf("%d",&c);
for(k=1;k<=c;k++)
{
  char c[5][5];
   int i,j,cntx,cnto,cntt,draw=0,counter=0;
   for(i=0;i<4;i++)
   {for(j=0;j<4;j++)
   cin>>c[i][j];}
   
   for(i=0;i<4&&counter==0;i++)
   {cntx=0;
   cnto=0;
   cntt=0;
   for(j=0;j<4;j++)
   {if(c[i][j]=='X')
   cntx++;
   else
   if(c[i][j]=='O')
   cnto++;
   else
   if(c[i][j]=='T')
   cntt++;
   else
   if(c[i][j]=='.')
   draw++;
   }
   if((cntx==4)||((cntx==3)&&(cntt==1)))
   {printf("Case #%d: X won\n",k);
   counter++;
   break;}
   else if((cnto==4)||((cnto==3)&&(cntt==1)))
   {printf("Case #%d: O won\n",k);
   counter++;
   break;}
}

for(i=0;i<4&&counter==0;i++)
   {cntx=0;
   cnto=0;
   cntt=0;
   for(j=0;j<4;j++)
   {if(c[j][i]=='X')
   cntx++;
   else
   if(c[j][i]=='O')
   cnto++;
   else
   if(c[j][i]=='T')
   cntt++;
   else
   if(c[j][i]=='.')
   draw++;
   }
   if((cntx==4)||((cntx==3)&&(cntt==1)))
   {printf("Case #%d: X won\n",k);
   counter++;
   break;}
   else if((cnto==4)||((cnto==3)&&(cntt==1)))
   {printf("Case #%d: O won\n",k);
   counter++;
   break;}
}

cntx=0;
cnto=0;
cntt=0;
for(i=0;i<4&&counter==0;i++)
{
  if(c[i][i]=='X')
  cntx++;
  else if(c[i][i]=='O')
  cnto++;
  else
  if(c[i][i]=='T')
  cntt++;
}
if((cntx==4)||((cntx==3)&&(cntt==1)))
   {printf("Case #%d: X won\n",k);
   counter++;}
   else if((cnto==4)||((cnto==3)&&(cntt==1)))
   {printf("Case #%d: O won\n",k);
   counter++;}
   
cntx=0;
cnto=0;
cntt=0;
for(i=0;i<4&&counter==0;i++)
{
  if(c[i][3-i]=='X')
  cntx++;
  else if(c[i][3-i]=='O')
  cnto++;
  else
  if(c[i][3-i]=='T')
  cntt++;
}
if((cntx==4)||((cntx==3)&&(cntt==1)))
   {printf("Case #%d: X won\n",k);
   counter++;}
   else if((cnto==4)||((cnto==3)&&(cntt==1)))
   {printf("Case #%d: O won\n",k);
   counter++;}

if(counter==0)
{if(draw>0)
printf("Case #%d: Game has not completed\n",k);
else
printf("Case #%d: Draw\n",k);
}
}
getch();
return 0;
}
