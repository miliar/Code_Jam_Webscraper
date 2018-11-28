#include<cstdio>

using namespace std;

int main()
{
    freopen("b.in", "r", stdin);
    freopen("b.out", "w", stdout);
    int cases;
    
    scanf("%d", &cases);
    for(int currentCase = 1; currentCase <= cases; currentCase++)
    {
            int a, b, k;
            scanf("%d %d %d", &a, &b, &k);
            
            long long sol = 0;
            for(int i = 0; i < a; i++)
                    for(int j = 0; j < b; j++)
                            if((i & j) < k)
                                  sol++;
            
            printf("Case #%d: %ld\n", currentCase, sol);
    }
    
    return 0;
}
