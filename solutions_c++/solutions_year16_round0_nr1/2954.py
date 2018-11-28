#include <bits/stdc++.h>
#ifdef DEBUG
#define D(x...) fprintf(stderr,x) 
#else
#define D(x...)
#endif
using namespace std;
int T, N, m ;
bool seen[10];
int main ()
{
	freopen("infile.txt", "r", stdin);
	freopen("outfile.txt", "w", stdout);
	scanf("%d", &T);
	for(int t=1; t<=T; t++)
	{
		scanf(" %d ", &N);
		if(N==0)
		{
			printf("Case #%d: INSOMNIA\n",t);
			D("solved %d\n", t);
			continue;
		}
		for(int i=0; i<10; i++)
		{
			seen[i]=false;
		}
		int ans=1, cnt=0;
		while(cnt < 10)
		{
			int c=N* ans;
			while(c!=0)
			{
				if(seen[c%10]==false)
				{
					seen[c%10]=true;
					cnt++;
				}
				c/=10;
			}
			ans++ ;
		}
		printf("Case #%d: %d\n",t, N*(ans-1));
		D("solved %d max %d\n", t, ans-1 );
		m = max(m, ans-1);
	}
	D("max %d\n", m);
}