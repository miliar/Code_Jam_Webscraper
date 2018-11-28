#include <cstdio>
#include <cstring>

int main()
{
	int t;
	scanf("%d", &t);
	for(int c = 1; c<=t; c++)
	{
		int n,m;
		scanf("%d %d", &n, &m);
		int data[200][200];
		
		int maxh[200], maxv[200];
		memset(&maxh, 0, sizeof(maxh));
		memset(&maxv, 0, sizeof(maxv));
		
		for(int y=0;y<n;y++)
		for(int x=0;x<m;x++)
		{
			scanf("%d", &data[x][y]);
			if(data[x][y]>maxh[y]) maxh[y] = data[x][y];
			if(data[x][y]>maxv[x]) maxv[x] = data[x][y];
		}
		
		bool valid = true;
		for(int y=0;y<n;y++)
		for(int x=0;x<m;x++)
		{
			if(data[x][y]<maxh[y] && data[x][y]<maxv[x]) valid = false;
		}
		
		printf("Case #%d: %s\n", c, valid?"YES":"NO");
	}
}
