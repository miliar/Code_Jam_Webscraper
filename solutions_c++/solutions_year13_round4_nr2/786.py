#include<cstdio>
#include<iostream>
long long z,p,n,potn,a,b,c,d,zawsze,raz,k;
bool zawsz(int nizszych,int rund,int miej)
{
long long ktory=0;
for(int i=0;i<rund;i++)
	{	
	if(nizszych>0)ktory+=(potn>>(i+1));
	nizszych--;
	nizszych/=(2);
	//printf("%lld %lld %lld\n",ktory,nizszych,i);
	
	}
return ktory<=miej-1;
}
bool ra(int wyzszych,int rund,int miej)
{
long long ktory=potn-1;
for(int i=0;i<rund;i++)
	{	
	if(wyzszych>0)ktory-=(potn>>(i+1));
	wyzszych--;
	wyzszych/=2;
	//printf("%lld %lld %lld\n",ktory,wyzszych,i);
	}
return ktory<=miej-1;
}
main()
{
scanf("%lld",&z);
for(int uu=1;uu<=z;uu++)
	{
	printf("Case #%d: ",uu);
	scanf("%lld%lld",&n,&k);
	potn=1<<n;
	for(int i=0;i<potn;i++)//wyznaczamy najwieekszy który raz wygra
		{
	//	printf("\n\n%d\n",i);
		if(ra(potn-i-1,n,k))raz=i;
		}
	for(int i=0;i<potn;i++)
		{
	//	printf("\n\n%d\n",i);
		if(zawsz(i,n,k))zawsze=i;
		}
	printf("%lld %lld\n",zawsze,raz);
	}
}
