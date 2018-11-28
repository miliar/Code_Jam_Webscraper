#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<algorithm>
#include<string>
#include<iostream>

using namespace std;

bool f[10];
int n,t,i;


void calc(int x, bool *f)
{
	int n = x;
	while(n > 0)
	{
		f[n % 10] = true;
		n /= 10;
	}
}

int main()
{
	freopen("g1.in","r",stdin);
	freopen("g1.out","w",stdout);
	scanf("%d",&t);
	for(int k = 1; k <= t; k++)
	{
		scanf("%d",&n);
		memset(f,0,sizeof(f));
		if(n == 0)
		{
			printf("Case #%d: INSOMNIA\n",k);
			continue;
		}
		bool ans = false;
		for(i = 1;; i++)
		{
			calc(i*n,f);
			bool check = true;
			for(int j = 0; j < 10; j++)
				if(!f[j])
					check = false;
			ans = check;
			if(ans == true)
				break;
		}
		printf("Case #%d: %d\n",k,i*n);
	}
	return 0;
}
