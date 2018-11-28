#include<iostream>
#include<fstream>
using namespace std;
int main()
{
freopen("in","r",stdin);
freopen("out","w",stdout);
int t,flag=0;
scanf("%d",&t);
for(int i=1;i<=t;i++)
{
int x,r,c;
printf("Case #%d: ",i);
scanf("%d%d%d",&x,&r,&c);
//printf("%d %d %d",x,r,c);
switch(x)
{
case 1: flag=0;
	break;
case 2: if((r*c)%2!=0)
	{
	flag=1;
	}
	else {flag=0;}
	break;
case 3: if(((r*c)%3==0))
		{
			if((r==1 && c==3))	
			{flag=1;}
			else if((c==1 && r==3)){flag=1;}
			else
			flag=0;
		}
		else
		{flag=1;}
	break;
case 4: if(((r*c)%4==0))
		{
			if((r==1 && c==4))
			{flag=1;}
			else if((r==4 && c==1))
			{flag=1;}
			else if((r==2 && c==2))
			{flag=1;}
			else if((r==2 && c==4))
			{
				flag=1;
}
			else if((r==4 && c==2))
			{flag=1;
}
			else
			{flag=0;}
		}
		else
		{flag=1;}
		break;
}
if(flag==1)
printf("RICHARD\n");
else
printf("GABRIEL\n");
}
return 0;
}