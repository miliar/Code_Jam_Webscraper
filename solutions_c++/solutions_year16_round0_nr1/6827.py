#include <iostream>
#include <cstdio>
using namespace std;

int n,i,T;
long long x;
int b[10],cnt;

int main()
{
	//freopen("a.out","w",stdout);
	scanf("%d",&T);
	for(int t = 1; t <= T; ++ t)
	{
		printf("Case #%d: ",t);
		scanf("%d",&n); cnt = 10;
		memset(b,0,sizeof(b));
		for(i = 1; i <= 10005; ++ i)
		{
			x = 1LL* n * i;
			while(x)
			{
				if(!b[x%10]) --cnt,b[x%10] = 1;
				x /= 10;
			}	
			if(cnt == 0) break;
		}
		if(!cnt) printf("%d\n",n*i);
		else printf("INSOMNIA\n");
	}
	return 0;
}
 
