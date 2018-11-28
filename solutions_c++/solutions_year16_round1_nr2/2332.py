#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int n, s[60][60], lt[200][60], p[200], q[60], ans , gg[60];
class list{
public:
	int x[60];
}big[200], sma[200];

int scmp(list a, list b){
	for (int i = 0; i < n; ++i)
	{
		if (a.x[i] != b.x[i])
		{
			return a.x[i] < b.x[i];
		}
	}
	return 0;
}
int bcmp(list a, list b){
	for (int i =n-1; i >=0; --i)
	{
		if (a.x[i] != b.x[i])
		{
			return a.x[i] < b.x[i];
		}
	}
	return 0;
}

void dfs(int a, int prev){
	if (ans)
	{
		return;
	}
	if (a == n)
	{
		memset(gg, 0, sizeof(gg));
		for (int i = 0,j,x; i < n*2-1; ++i)
		{
			if(p[i]==0){
				for (j = 0; j < n; ++j)
				{
					for (x = 0; x < n; ++x)
						if (s[x][j] != sma[i].x[x])
						{
							break;
						}
					if (x==n) break;
				}
				if (j == n) return;
				gg[j] = 1;
			}
		}
		ans = 1;
		return;
	}

	for (int i = 0; i < 2*n-1 && i < 2*n-1-n+a+1; ++i)
	{
		if (ans)
		{
			return;
		}
		if (p[i] == 0 && sma[i].x[0] > prev)
		{
			p[i] = 1;
			for(int j=0;j<n;j++)
				s[a][j] = sma[i].x[j];
			dfs(a+1, sma[i].x[0]);
			p[i] = 0;
		}
	}
}

int main(void){
    int t;
    scanf("%d",&t);
    for(int tt=1;tt<=t;tt++){
    	scanf("%d", &n);
    	memset(p,0,sizeof(p));
    	for (int i = 0; i < n*2-1; ++i)
    	{
    		for (int j = 0; j < n; ++j)
    		{
    			scanf("%d", &lt[i][j]);
    			sma[i].x[j] = lt[i][j];
    		}
    	}
    	sort(sma, sma+n*2-1, scmp);
    	// sort(big, big+n*2-1, bcmp);

    	// p[0]=p[n-1]=1;

    	// for (int i = 0; i < n; ++i)
    	// {
    	// 	s[0][i] = sma[0].x[i];
    	// }

    	// if (sma[0].x[n-1] == big[n-1].x[0])
    	// {
    	// 	for (int i = 0; i < n; ++i)
    	// 	{
    	// 		s[i][n-1] = big[n-1].x[i];
    	// 	}
    	// } else {
    	// 	for (int i = 0; i < n; ++i)
    	// 	{
    	// 		s[n-1][i] = big[n-1].x[i];
    	// 	}
    	// }
    	ans = 0;
    	dfs(0, 0);

    	// for (int i = 0; i < n*2-1; ++i,puts(""))
    	// {
    	// 	for (int j = 0; j < n; ++j)
    	// 	{
    	// 		printf("%d", sma[i].x[j]);
    	// 	}
    	// }

    	// for (int i = 0; i < n; ++i,puts(""))
    	// {
    	// for (int j = 0; j < n; ++j)
    	// 	printf("%3d", s[i][j]);
    	// }

        printf("Case #%d:", tt);

        for (int i = 0; i < n; ++i)
        {
        	if (gg[i]==0)
        	{
        		for (int j = 0; j < n; ++j)
        		{
        			printf(" %d", s[j][i]);
        		}
        	}
        }
        puts("");
    }
    return 0;
}

