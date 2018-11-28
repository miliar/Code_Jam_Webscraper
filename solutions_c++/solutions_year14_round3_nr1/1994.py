#include<cstdio>
#include<cmath>
#include<string.h>
#include<stdlib.h>
using namespace std;
long pmodQ(int a, int b, int Q)
{a=a%Q;
if(b==0)
	return 1;
if(b==1)
return a;
if(b==2)
	return (a*a)%Q;
if(b%2==0)
	return	pmodQ(pmodQ(a,b/2,Q),2,Q)%Q;
else
	return (a*pmodQ(a,b-1,Q))%Q;	 
}

main()
{freopen("A.txt","w",stdout);
freopen("A-small-attempt1.in","r",stdin);
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;++t)
	{
	char A[100];
	scanf("%s",A);
	char *B=strtok(A,"/");
	long int P=atoi(B);
	B=strtok(NULL,"\n");
	
	long int Q=atoi(B);
	
	long P_1=P%Q;
	long x=pmodQ(2,40,Q);

	if((x*P_1)%Q!=0)
	{printf("Case #%d: impossible\n",t);
	}
	else
	{printf("Case #%d: %d\n",t,(int)(ceil(log2(Q)-log2(P))));
	}
}
}
