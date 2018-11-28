#include <bits/stdc++.h>
using namespace std;
long long seive[11111111];
vector <long long> primes;
long long convert(long long num[],long long len,long long base)
{
	long long res=0,i;
	for(i=0;i<len;i++)
	{
		if(num[i])
			res+=pow(base,i);
	}
	return res;
}
void getNum(long long num[],long long len,long long a)
{
	long long i=1;
	memset(num,0,sizeof(long long)*len);
	num[0]=num[len-1]=1;
	while(a!=0)
	{
		num[i++]=a%2;
		a/=2;
	}
}
long long getDivisor(long long a)
{
	long long i;
	if(a<11111111&&!seive[a])
		return -1;
	for(i=0;primes[i]*primes[i]<=a&&i<primes.size();i++)
	{
		if(a%primes[i]==0)
			return primes[i];
	}
	return -1;
}
int main()
{
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	long long t,n,i,T,jj,lim,v,divisors[11],j,flag,count;
	memset(seive,0,sizeof(long long)*11111111);
	for(i=2;i<11111111;i++)
	{
		if(seive[i])
			continue;
		primes.push_back(i);
		for(j=2*i;j<11111111;j+=i)
			seive[j]=1;	
	}
	scanf("%lld",&T);
	for(t=1;t<=T;t++)
	{
		scanf("%lld %lld",&n,&jj);
		long long *num = new long long[n];
		lim = pow(2,n-2);
		i=count=0;
		printf("Case #%lld:\n",t);
		while(count<jj&&i<lim)
		{
			getNum(num,n,i);
			flag=1;
			for(long long base=2;base<=10;base++)
			{
				v=convert(num,n,base);
				//printf("%lld : %lld\n",base, v);
				divisors[base]=getDivisor(v);
				if(divisors[base]==-1)
				{
					flag=0;
					break;
				}	
			}
			if(flag)
			{
				count++;
				for(j=n-1;j>=0;j--)
					printf("%lld",num[j]);
				for(long long base=2;base<=10;base++)
					printf(" %lld",divisors[base]);
				printf("\n");
			}
			i++;	
		}		
	}
	return 0;
}