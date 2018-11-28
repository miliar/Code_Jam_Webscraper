#include <stdio.h>
long long ptp[10000005],numnum,m,k,num,pt[50],log[20];
long long tobase(int base,long long origi)
{
	long long neww=0,plus=1,b=base;
	while(origi!=0)
	{
		if(origi%2==1)
			neww+=plus;
		plus*=b;
		origi/=10;
	}
	return neww;
}
long long isprime(long long t,int lnum)
{
	for(int i=0;ptp[i]*ptp[i]<=t&&i<numnum;i++)
		if(t%ptp[i]==0)
		{
			log[lnum]=ptp[i];
			return ptp[i];
		}
	return -1;
}
void runcheck(long long x)
{
	int i;
	for(i=2;i<=10;i++)
		if(isprime(tobase(i,x),i)==-1)
			return;
	num++;
	printf("%lld ",x);
	for(i=2;i<=10;i++)
		printf("%lld ",log[i]);
	printf("\n");
}
void run(long long now,long long pos)
{
	if(num==k)
		return;
	//printf("%lld ",now);
	if(pos==m-1)
	{
		runcheck(now);
		return;
	}
	run(now+pt[pos],pos+1);
	run(now,pos+1);
}
void doe(int x)
{
	printf("Case #%d:\n",x);
	scanf("%lld %lld",&m,&k);
	run(pt[m-1]+1,1);
	printf("\n");
}
int main()
{
	numnum=1;
	ptp[0]=2;
	for(long long i=3;i<=110000000LL;i+=2)
	{
		if(i%1000000==999999)
			//printf("%lld ",i);
		for(int i2=0;ptp[i2]*ptp[i2]<=i;i2++)
			if(i%ptp[i2]==0)
				goto fail;
		ptp[numnum++]=i;
		fail:
			1;
	}
	pt[0]=1;
	for(int i=1;i<=32;i++)
		pt[i]=pt[i-1]*10;
	freopen("Cin.in","r",stdin);
	freopen("Cout.out","w",stdout);
	int n;
	scanf("%d",&n);
	for(int i=1;i<=n;i++)
		doe(i);
	return 0;
}
