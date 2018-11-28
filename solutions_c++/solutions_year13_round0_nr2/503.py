#include <cstdio>

const int MAXV = 100, MAXN = 100;
int val[MAXN][MAXN];

int main()
{
	int T, R, C;
	
	scanf("%d", &T);
	
	for(int tc = 1; tc <= T; tc++)
	{
		scanf("%d%d", &R, &C);
		for(int i = 0; i < R; i++)
			for(int j = 0; j < C; j++)
				scanf("%d", &val[i][j]);
		
		bool failed = false;
		for(int i = 1; i <= MAXV; i++)
		{
			for(int r = 0; r < R && !failed; r++)
				for(int c = 0; c < C; c++)
					if(val[r][c] == i)
					{
						bool pass = true;
						//column check
						for(int rr = 0; rr < R; rr++)
						{
							if(val[rr][c] != -1 && val[rr][c] != i)
							{
								pass = false;
								break;
							}							
						}
						
						if(pass)
						{
							for(int rr = 0; rr < R; rr++)
								val[rr][c] = -1;
						}
						
						//row check
						if(!pass)
						{
							pass = true;
							for(int cc = 0; cc < C; cc++)
								if(val[r][cc] != -1 && val[r][cc] != i)
								{
									pass = false;
									break;
								}
							
							if(pass)
							{								
								for(int cc = 0; cc < C; cc++)
									val[r][cc] = -1;
							}
						}
						
						if(!pass)
						{
							failed = true;
							break;
						}
					}
					
			if(failed) break;
		}
		
		if(failed) printf("Case #%d: NO\n", tc);
		else printf("Case #%d: YES\n", tc);
	}
	
	return 0;
}