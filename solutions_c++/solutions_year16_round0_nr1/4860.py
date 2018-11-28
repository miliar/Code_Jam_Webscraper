#include <bits/stdc++.h>

using namespace std;

int main()
{
	int t, flag, ind=0;
	long long int n, temp, N;
	int a[12];
	scanf("%d",&t);
	while(t--)
	{
		ind++;
		scanf("%lld",&n);
		N = n;
		for(int i=0;i<10;i++)	a[i]=0;
		while(n < 100*N)
		{
			temp = n;
			while(temp>0)
			{
				a[temp%10]++;
				temp/=10;
			}
			flag=0;
			for(int i=0;i<10;i++)
			{
				if(!a[i])	flag=1;
			}
			if(!flag)	break;
			n += N;
		}
		flag=0;
		for(int i=0;i<10;i++)
			if(!a[i])	flag=1;
		if(!flag)
			printf("Case #%d: %lld\n", ind, n);
		else
			printf("Case #%d: INSOMNIA\n", ind);
	}
	return 0;
}