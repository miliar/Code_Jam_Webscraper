#include<stdlib.h>
#include<stdio.h>

bool judge(long long x)
{
	bool ret = true;
	int arr[20];

	int len = 0;
	while(1)
	{
		arr[len++] = x%10;
		x/=10;
		if(x==0)

			break;
	}

	for(int i=0;i<len/2;i++)
	{
		if(arr[i]==arr[len-1-i])
		{
			continue;
		}
		else
		{
			ret = false;
		}
	}
	return ret;
}

		

int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	
	
	int T;
	scanf("%d\n",&T);
	for(int t=0;t<T;t++)
	{
		long long a,b;
		long long count = 0;
		scanf("%lld%lld",&a,&b);
		for(long long x=1;x<=b;x++)
		{
			long long x2 = x*x;
			if(x2>b)
				break;
			
			if(x2<a)
				continue;

			bool rt1,rt2;
			rt1 = judge(x);
			rt2 = judge(x2);
			if(rt1&&rt2)
			{
				count++;
				//printf("(%lld) ",x2);
			}
		}
		printf("Case #%d: %lld\n",t+1,count);
	}

	return 0;
}