#include <stdio.h>

int ln[110][110];
int bi[110], bj[110];

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.txt", "w", stdout);
	int T;
	int cs = 1;
	scanf("%d", &T);
	while(T--)
	{

		int N, M;
		int i, j;
		scanf("%d%d", &N, &M);
		for(i = 1 ; i <= N ; i++)
		{
			for(j = 1 ; j <= M ; j++)
			{
				scanf("%d", &ln[i][j]);
			}
		}
		
		for(i = 1 ; i <= N ; i++)
		{
			int mx = 0;
			for(j = 1 ; j <= M ; j++)
			{
				if(ln[i][j] > mx)
				{
					mx = ln[i][j];
				}
			}
			bi[i] = mx;
		}
		for(j = 1 ; j <= M ; j++)
		{
			int mx = 0;
			for(i = 1 ; i <= N ; i++)
			{
				if(ln[i][j] > mx)
				{
					mx = ln[i][j];
				}
			}
			bj[j] = mx;
		}
		int chk = true;
		for(i = 1 ; i <= N ; i++)
		{
			for(j = 1 ; j <= M ; j++)
			{
				if(ln[i][j] != bi[i] && ln[i][j] != bj[j])
				{
					chk = false;
					break;
				}
			}
			if(chk == false)
			{
				break;
			}
		}
		if(chk == true)
		{
			printf("Case #%d: YES\n", cs);
		}
		else
		{
			printf("Case #%d: NO\n", cs);
		}
		cs++;
	}
	return 0;
}
