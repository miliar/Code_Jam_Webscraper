#include <cstdio>
#include <cstring>
using namespace std;

int r, c, m;
char board[5][6];

void dfs(int i, int j)
{
    if(board[i][j] == '#')
        board[i][j] = '.';
    else if(board[i][j] == '&')
	{
        board[i][j] = '.';
        for(int di = -1; di < 2; ++di)
            for(int dj = -1; dj < 2; ++dj)
                if(0 <= i + di && i + di < r && 0 <= j + dj && j + dj < c)
                    dfs(i + di, j + dj);
	}
}



void solve(int cs)
{
    scanf("%d%d%d", &r, &c, &m);
    printf("Case #%d:\n", cs);
	if(m + 1 == r * c)
	{
		for(int i = 0; i < r; ++i)
		{
			for(int j = 0; j < c; ++j)
				printf("%s", (i == j && i == 0) ? "c" : "*");
			puts("");
		}
		return;
	}
    for(int mask = 0; mask < (1 << (r * c)); ++mask)
	{
		int cnt = 0;
		for(int i = 0; i < r * c; ++i)
			cnt += (mask & (1 << i)) != 0;
		if(cnt != m)
			continue;
		memset(board, 0, sizeof(board));
		for(int i = 0; i < r * c; ++i)
			{
				if(mask & (1 << i))
					board[i / c][i % c] = '*';
				else
					board[i / c][i % c] = '&';
			}
        for(int i = 0; i < r; ++i)
            for(int j = 0; j < c; ++j)
                if(board[i][j] == '*')
                    for(int di = -1; di < 2; ++di)
                        for(int dj = -1; dj < 2; ++dj)
                            if(0 <= i + di && i + di < r && 0 <= j + dj && j + dj < c && board[i + di][j + dj] == '&')
                                board[i + di][j + dj] = '#';
		//for(int p = 0; p < r; ++p)
        //    printf("%s\n", board[p]);
		//puts("");
		for(int i = 0; i < r; ++i)
		{
            bool flag = true;
            for(int j = 0; j < c; ++j)
                if(board[i][j] == '&')
				{
                    dfs(i, j);
					for(int p = 0; p < r; ++p)
						for(int q = 0; q < c; ++q)
							flag &= board[p][q] != '#';
                    if(flag)
					{
                        board[i][j] = 'c';
                        for(int p = 0; p < r; ++p)
                            printf("%s\n", board[p]);
                        return;
					}
                    else
                        break;
				}
            if(!flag)
                break;
		}
	}
    printf("Impossible\n");
}

int main()
{
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
#endif
	int t;
	scanf("%d", &t);
	for(int i = 0; i < t; ++i)
		solve(i + 1);
	return 0;
}