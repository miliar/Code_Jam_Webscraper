#include<cstdio>
using namespace std;

main()
{int T;
freopen("B-large.in","r",stdin);	
freopen ("Q2Ishan.txt","w",stdout);
double F,C,X,R;
scanf("%d",&T);
for(int i=1;i<=T;++i)
{

scanf("%lf",&C);
scanf("%lf",&F);
scanf("%lf",&X);

R=2;
double cookies=0;
double time=0;
while(1)
{if(cookies>=X)
	break;
if(X<=C)
	{time+= (X-cookies)/R;
	break;}
else
{time+=(C-cookies)/R;
cookies=C;
if(((X-C)/R)>=X/(R+F))
{cookies=0;
R+=F;
}
else
{time+=(X-C)/R;
break;
}

}
}printf("Case #%d: ",i);
printf("%lf \n",time);
}
}
