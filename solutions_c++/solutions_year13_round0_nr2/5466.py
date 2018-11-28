#include <iostream>
#include <sstream>
#include <string.h>
#include <stdio.h>
#include <math.h>

using namespace std;

//#define MY_DEBUG
//#define MY_DEBUG2

int grass[100][100];
int check[100][100];

int main(void)
{
    int T=0, loop=0;

    cin >> T;
    
#ifdef MY_DEBUG
    printf("=> T=%d\n", T);
#endif

    while (++loop <= T)
    {
        int N=0, M=0;
        cin >> N >> M;

#ifdef MY_DEBUG
    printf("=> N=%d, M=%d\n", N, M);
#endif

        memset(grass, 0, sizeof(grass));
        memset(check, 0, sizeof(check));
        for (int i=0; i<N; i++)
        {
            for (int j=0; j<M; j++)
            {
                cin >> grass[i][j];
                if (grass[i][j] == 1)
                    check[i][j] = 1;
            }
        }

#ifdef MY_DEBUG
        printf("=> grass\n");
        for (int i=0; i<N; i++)
        {
            printf("=> ");
            for (int j=0; j<M; j++)
            {
                printf("%d", grass[i][j]);
            }
            printf("\n");
        }
        printf("=> check\n");
        for (int i=0; i<N; i++)
        {
            printf("=> ");
            for (int j=0; j<M; j++)
            {
                printf("%d", check[i][j]);
            }
            printf("\n");
        }
#endif

        // do horizontal
#ifdef MY_DEBUG2
        printf("==> do horizontal\n");
#endif
        for (int i=0; i<N; i++)
        {
            int j = 0;
            for (j=0; j<M; j++)
            {
#ifdef MY_DEBUG2
        printf("==> grass[%d][%d]=%d\n", i, j, grass[i][j]);
#endif
                if ( grass[i][j] != 1 )
                    break;
            }
            if (j==M)
            {
                for (int j=0; j<M; j++)
                    check[i][j] = 0;
            }
        }
        // do reverse horizontal
#ifdef MY_DEBUG2
        printf("==> do reverse horizontal\n");
#endif
        for (int i=0; i<N; i++)
        {
            int j = 0;
            for (j=M-1; j>=0; j--)
            {
#ifdef MY_DEBUG2
        printf("==> grass[%d][%d]=%d\n", i, j, grass[i][j]);
#endif
                if ( grass[i][j] != 1 )
                    break;
            }
            if (j==-1)
            {
                for (int j=0; j<M; j++)
                    check[i][j] = 0;
            }
        }
        // do vertical
#ifdef MY_DEBUG2
        printf("==> do vertical\n");
#endif
        for (int j=0; j<M; j++)
        {
            int i = 0;
            for (i=0; i<N; i++)
            {
#ifdef MY_DEBUG2
        printf("==> grass[%d][%d]=%d\n", i, j, grass[i][j]);
#endif
                if ( grass[i][j] != 1 )
                    break;
            }
            if (i==N)
            {
                for (int i=0; i<N; i++)
                    check[i][j] = 0;
            }
        }
        // do reverse vertical
#ifdef MY_DEBUG2
        printf("==> do reverse vertical\n");
#endif
        for (int j=0; j<M; j++)
        {
            int i = 0;
            for (i=N-1; i>=0; i--)
            {
#ifdef MY_DEBUG2
        printf("==> grass[%d][%d]=%d\n", i, j, grass[i][j]);
#endif
                if ( grass[i][j] != 1 )
                    break;
            }
            if (i==-1)
            {
                for (int i=0; i<N; i++)
                    check[i][j] = 0;
            }
        }


#ifdef MY_DEBUG
        printf("=> check\n");
        for (int i=0; i<N; i++)
        {
            printf("=> ");
            for (int j=0; j<M; j++)
            {
                printf("%d", check[i][j]);
            }
            printf("\n");
        }
#endif

        int fail = 0;
        for (int i=0; i<N && fail==0; i++)
        {
            for (int j=0; j<M; j++)
            {
                if (check[i][j] > 0)
                {
                    fail = 1;
                    break;
                }
            }
        }
        
        if (fail == 0)
            printf("Case #%d: YES\n", loop);
        else
            printf("Case #%d: NO\n", loop);
    }

    return 0;
}
