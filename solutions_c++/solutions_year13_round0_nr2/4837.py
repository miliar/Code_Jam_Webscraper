#include <algorithm>
#include <stdio.h>

//using namespace std;
int TAB[104][104];

int main()
{
	int t, n, m;
	scanf("%d", &t);
	for (int T=1;T<=t;++T)
	{
		scanf("%d %d", &n, &m);
		for(int i=0;i<n;++i) for(int j=0;j<m;++j) scanf("%d", TAB[i]+j);
		int max = 0, I, J;

		for(int i=0;i<n;++i) 
		{
			for(int j=0;j<m;++j)
			{
				if(TAB[i][j] > max)
				{
					max = TAB[i][j];
					I=i;
					J=j;
				}
			}
		}
		int i, j;
		for(i=0;i<n;++i)
		{
			if(i==I) continue;
			for(j=0;j<m;++j)
			{
				if(j==J) continue;
				if(TAB[i][j] != std::min(TAB[I][j], TAB[i][J]))
				{
					break;
				}
			}
			if(j<m) break;	
		}
		if(i<n) printf("Case #%d: NO\n", T);
		else printf("Case #%d: YES\n", T);
	}
	return 0;
}
