#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <utility>

using namespace std;

bool smile[16];
int R, C, ans;

int CountTheWall()
{
	bool smile_2D[16][16];
	int cnt = 0;
	for (int i = 0; i < R; ++i)
	{
		for (int j = 0; j < C; ++j)
		{
			smile_2D[i][j] = smile[i*C+j];
			if (i-1 >= 0 && smile_2D[i][j] == true && smile_2D[i-1][j] == true)
			{
				++cnt;
			}
			if (j-1 >= 0 && smile_2D[i][j] == true && smile_2D[i][j-1] == true)
			{
				++cnt;
			}
		}
	}
	
	return cnt;
}

void backtrace(int now, int boundary, int choose_boundary)
{
	if (now == boundary)
	{
		int choose_now = 0;
		for (int i = 0; i < boundary; ++i)
		{
//			printf("%d", smile[i]);
			if (smile[i] == true)
			{
				++choose_now;
			}
		}
//		printf("\n");
		if (choose_now == choose_boundary)
		{
			ans = min(ans, CountTheWall());
//			printf("right number\n");
//			printf("ans: %d\n", ans);
		}
		
		return;
	}
	backtrace(now+1, boundary, choose_boundary);
	smile[now] = true;
	backtrace(now+1, boundary, choose_boundary);
	smile[now] = false;
}

int main()
{
    freopen ("B-small-attempt0.in","r",stdin);
    freopen ("B-small-attempt0.out","w",stdout);

    int cas, N;
	
	scanf("%d", &cas);

    for (int c = 1; c <= cas; ++c)
    {
        scanf("%d%d%d", &R, &C, &N);
		
		memset(smile, false, sizeof(smile));
		ans = 10000000;
		
		backtrace(0, R*C, N);

        printf("Case #%d: %d\n", c, ans);
    }

    return 0;
}