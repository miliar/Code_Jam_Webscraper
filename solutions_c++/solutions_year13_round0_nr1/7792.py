#include<iostream>
using namespace std;
int main()
{freopen("A-large.in","r",stdin);
freopen("Output4.txt","w",stdout);
int t, i, j, countx, counto, countdot, countt, draw, stop, counter=0;
scanf("%d",&t);
while(t--)
{char x[5][5];
counter++;
stop=draw=0;
for(i=0;i<4;i++)
for(j=0;j<4;j++)
cin>>x[i][j];
scanf("\n");
for(i=0;i<4;i++)
{countx=counto=countdot=countt=0;
if(stop)
break;
for(j=0;j<4;j++)
if(x[i][j]=='X')
countx++;
else if(x[i][j]=='O')
counto++;
else if(x[i][j]=='T')
countt++;
else draw=1;
if(countx==4)
{printf("Case #%d: X won\n",counter);
stop=1;}
else if(counto==4)
{printf("Case #%d: O won\n",counter);
stop=1;}
else if(countx==3 && countt==1)
{printf("Case #%d: X won\n",counter);
stop=1;}
else if(counto==3 && countt==1)
{printf("Case #%d: O won\n",counter);
stop=1;}
}
for(j=0;j<4;j++)
{countx=counto=countdot=countt=0;
if(stop)
break;
for(i=0;i<4;i++)
if(x[i][j]=='X')
countx++;
else if(x[i][j]=='O')
counto++;
else if(x[i][j]=='T')
countt++;
else draw=1;
if(countx==4)
{printf("Case #%d: X won\n",counter);
stop=1;}
else if(counto==4)
{printf("Case #%d: O won\n",counter);
stop=1;}
else if(countx==3 && countt==1)
{printf("Case #%d: X won\n",counter);
stop=1;}
else if(counto==3 && countt==1)
{printf("Case #%d: O won\n",counter);
stop=1;}
}
countx=counto=countdot=countt=0;
for(i=0;i<4;i++)
{if(stop)
break;
for(j=0;j<4;j++)
if(i==j)
{if(x[i][j]=='X')
countx++;
else if(x[i][j]=='O')
counto++;
else if(x[i][j]=='T')
countt++;
else draw=1;}
}
if(countx==4)
{printf("Case #%d: X won\n",counter);
stop=1;}
else if(counto==4)
{printf("Case #%d: O won\n",counter);
stop=1;}
else if(countx==3 && countt==1)
{printf("Case #%d: X won\n",counter);
stop=1;}
else if(counto==3 && countt==1)
{printf("Case #%d: O won\n",counter);
stop=1;}
countx=counto=countdot=countt=0;
for(i=0;i<4;i++)
{if(stop)
break;
for(j=0;j<4;j++)
if(i+j==3)
{if(x[i][j]=='X')
countx++;
else if(x[i][j]=='O')
counto++;
else if(x[i][j]=='T')
countt++;
else draw=1;}
}
if(countx==4)
{printf("Case #%d: X won\n",counter);
stop=1;}
else if(counto==4)
{printf("Case #%d: O won\n",counter);
stop=1;}
else if(countx==3 && countt==1)
{printf("Case #%d: X won\n",counter);
stop=1;}
else if(counto==3 && countt==1)
{printf("Case #%d: O won\n",counter);
stop=1;}
if(!stop)
if(draw)
printf("Case #%d: Game has not completed\n",counter);
else printf("Case #%d: Draw\n",counter);}
return 0;}



