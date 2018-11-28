#include<stdio.h>
#include<math.h>
#include<string.h>
char k[110];
int is_hw(long long n)
{
	int i,j,len;
	long long m=sqrt(n);
	memset(k,0,sizeof(k));
	i=0;
	while(m!=0)
	{
		k[i]=m%10+'0';
		m/=10;
		i++;
	}
	len=i;
	i=0;j=len-1;
	for(;i<j;i++,j--)
	{
		
		//printf("%lld\n",n);
		if(k[i]!=k[j]) return 0;
	}
	//////////////////////////////
	memset(k,0,sizeof(k));
	i=0;
	while(n!=0)
	{
		k[i]=n%10+'0';
		n/=10;
		i++;
	}
	len=i;
	i=0;j=len-1;
	for(;i!=j;i++,j--)
	{
		//printf("----\n");
		if(k[i]!=k[j]) return 0;
	}
	return 1;
}
int is_sqrt(long long n)
{
	long long m=sqrt(n);
	if(m*m==n) return 1;
	else return 0;
}
int main()
{
	//freopen("C-small-attempt2.in","r",stdin);
    //freopen("C-small-attempt0.out","w",stdout);
	long long a,b,T,i,cnt,t;
	while(scanf("%lld",&T)!=EOF)
	{
		t=0;
		while(T--)
		{
			scanf("%lld%lld",&a,&b);
			cnt=0;
			t++;
			for(i=a;i<=b;i++)
			{
				if(is_sqrt(i)&&is_hw(i))
				{
					
					cnt++;
				}
			}
			printf("Case #%lld: %lld\n",t,cnt);
		}
	}
	
	return 0;
}
