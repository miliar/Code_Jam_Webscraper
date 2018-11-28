#include <stdio.h>

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    
    int A[1005];
    
    int cases;
    scanf("%d", &cases);
    
    for (int iindex = 1; iindex <= cases; iindex++)
    {
        int N;
        scanf("%d", &N);
        for (int i = 1; i <= N; i++)
        {
            scanf("%d", &A[i]);
        }
        
        int ans = 0;
        for (;;)
        {
            if (N == 1)
            {
                break;
            }
            
            int min = 1000000005;
            int index = 0;
            
            for (int i = 1; i <= N ; i++)
            {
                if (A[i] < min)
                {
                    min = A[i];
                    index = i;
                }
            }
            
            if (N - index > index - 1)
            {
                ans += index - 1;
            }
            else
            {
                ans += N - index;
            }
            
            for (int i = index; i < N; i++)
            {
                A[i] = A[i + 1];
            }
            
            N--;
        }
        
        printf("Case #%d: %d\n", iindex, ans);
    }
    
    return 0;
}
