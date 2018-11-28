#include <iostream>
#include <cstdio>
using namespace std;

int main(void)
{
    int T, N, M;
    int a[100][100];
    
    scanf("%d", &T);
    for(int cst = 1; cst <= T; ++cst)
    {
        scanf("%d%d", &N, &M);
        
        for(int i = 0; i < N; ++i)
            for(int j = 0; j < M; ++j)
                scanf("%d", &a[i][j]);
                
                
        for(int i = 0; i < N; ++i)
        {
            for(int j = 0; j < M; ++j)
            {
                int flag1 = 0;
                int flag2 = 0;
                
                for(int k = 0; k < N; ++k)
                {
                    if(a[k][j] > a[i][j])
                    {
                        flag1 = 1;
                        break;
                    }
                }
                
                for(int k = 0; k < M; ++k)
                {
                    if(a[i][k] > a[i][j])
                    {
                        flag2 = 1;
                        break;
                    }
                }
                
                if(flag1 && flag2)
                {
                    printf("Case #%d: NO\n", cst);
                    goto END;
                }
            }
        }
        
        printf("Case #%d: YES\n", cst);
        END: ;
    }
}

                
                
