#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

char ans[60][60];

int main()
{
    int T;
    scanf("%d", &T);

    for(int tt = 1; tt <= T; tt++)
    {
        printf("Case #%d:\n", tt);
 
        int R, C, M;
        scanf("%d%d%d", &R, &C, &M);
        int S = R * C - M;
        bool solved = true;
        bool tran = false;
        memset(ans, '*', sizeof(ans));

        if(R > C)
        {
            swap(R, C);
            tran = true;
        }
 
        if(S == 1)
            ans[0][0] = 'c';
        else if(R == 1)
        {
            for(int i = M; i < C; i++)
                ans[0][i] = '.';
            ans[0][C - 1] = 'c';
        }
        else if(S == 2 || S == 3 || S == 5 || S == 7 || (R == 2 && (S & 1)))
            solved = false;
        else
        {
            for(int i = 0; i < 2; i++)
                for(int j = 0; j < 2; j++)
                    ans[i][j] = '.';
            S -= 4;

            int A = 2, B = 2;
            while(S >= 2 && (A < R || B < C))
            {
                if(B >= C || (A < R && A <= B))
                    ans[A][0] = ans[A][1] = '.', A++;
                else
                    ans[0][B] = ans[1][B] = '.', B++;
                S -= 2;
            }
            
            for(int i = 2; S && i < R; i++)
                for(int j = 2; S && j < C; j++, S--)
                    ans[i][j] = '.';

            ans[0][0] = 'c';
        }

        if(!solved)
            puts("Impossible");
        else
        {
            if(tran)
                for(int i = 0; i < C; i++, printf("\n"))
                    for(int j = 0; j < R; j++)
                        printf("%c", ans[j][i]);
            else
                for(int i = 0; i < R; i++, printf("\n"))
                    for(int j = 0; j < C; j++)
                        printf("%c", ans[i][j]);

        }
    }

    return 0;
}
