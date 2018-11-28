#include <cstdio>
#include <cstring>

int no;

void testCase(int no) 
{
	int N, M;
	scanf("%d %d", &N, &M);
	int m[N][M];
	for(int y = 0; y < N; y++)
	{
		for(int x = 0; x < M; x++) 
		{
			scanf("%d", &m[y][x]);	
		}
	}

	if(N == 1 || M == 1) 
	{
		printf("YES\n");
		return;
	}

	for(int y = 0; y < N; y++)
    {
        for(int x = 0; x < M; x++)
        {
     		bool mX, mY;
			mX = mY = true;
		
			for(int i = 0; i < N; i++)
			{
				if(m[i][x] > m[y][x])
				{
					mY = false;
					break;
				}
			}

            for(int i = 0; i < M; i++)
            {
                if(m[y][i] > m[y][x])
                {
                    mX = false;
                    break;
                }
            }

			if(false == mX && false == mY)
			{
				printf("NO\n");
				return;
			}
        }
    }
	printf("YES\n");
}


int main()
{
	int N; scanf("%d", &N);
	getchar();	
	for(no = 0; no < N; no++)
	{
		printf("Case #%d: ", no + 1);
		testCase(no);
	}
	return 0;	
}
