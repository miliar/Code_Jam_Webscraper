#include <cassert>
#include <cstdio>

const int N = 128;
int r, c;
char f[N][N];

bool fall(int y, int x, char arr)
{
	int dx = 0, dy = 0;
	switch(arr)
	{
	case '^': dy = -1; break;
	case 'v': dy = 1; break;
	case '>': dx = 1; break;
	case '<': dx = -1; break;
	default: assert(false); break;
	}
	
	x += dx;
	y += dy;
	for(;;)
	{
		if(x < 0 || y < 0 || x >= c || y >= r)
			return true;
		
		if(f[y][x] != '.')
			return false;
			
		x += dx;
		y += dy;
	}
}


int solve()
{
	int res = 0;
	
	for(int y = 0; y < r; y++)
		for(int x = 0; x < c; x++)
			if(f[y][x] != '.')
			{
				if(!fall(y, x, f[y][x]))
					continue;
					
				res++;
				bool fuck = fall(y, x, '^') && fall(y, x, 'v') && fall(y, x, '>') && fall(y, x, '<');
				if(fuck)
					return -1;
			}
			
	return res;
}

int main()
{
	freopen("input.txt", "r", stdin);
	
	int tn;
	scanf("%i\n", &tn);
	for(int t = 1; t <= tn; t++)
	{
		scanf("%i %i\n", &r, &c);
		
		for(int i = 0; i < r; i++)
		{
			for(int j = 0; j < c; j++)
				scanf("%c", &f[i][j]);
			scanf("\n");
		}
		
		//for(int i = 0; i < r; i++)
		//{
		//	for(int j = 0; j < c; j++)
		//		printf("%c", f[i][j]);
		//	printf("\n");
		//}
		
		int res = solve();
		printf("Case #%i: ", t);
		if(res >= 0)
			printf("%i", res);
		else
			printf("IMPOSSIBLE");
		printf("\n");
	}
	
	return 0;
}

