#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <cstring>
#include <map>
#include <set>
#include <cstdlib>
#include <cmath>
using namespace std;

const int MAXK = 10, MAXN = 3;
int TC, R, N, M, K;
int val[MAXK], cv[MAXN];
bool found;

void solve(int depth)
{
    if(found) return ;

    if(depth == N)
    {
        int upper = (1<<N);
        set <int> pval;

        for(int i = 0; i < upper; i++)
        {
            int product = 1;
            for(int j = 0; j < N; j++)
                if(i & (1<<j))
                    product *= cv[j];
            pval.insert( product );
        }
        
        bool check = true;
        for(int i = 0; i < K; i++)
            if(pval.count( val[i] ) == 0)
            {
                check = false;
                break;
            }
        
        if(check)
        {
            found = true;
            for(int i = 0; i < N; i++)
                printf("%d", cv[i]);
            printf("\n");
        }
        return ;
    }
        
    for(int i = 2; i <= M; i++)
    {
        cv[depth] = i;
        solve(depth+1);
    }
}

int main()
{
    scanf("%d", &TC);

    
    for(int tc = 1; TC--; ++tc)
    {
        printf("Case #%d:\n", tc);
        scanf("%d%d%d%d", &R, &N, &M, &K);
        
        for(int i = 0; i < R; i++)
        {
            found = false;
            for(int j = 0; j < K; j++)
                scanf("%d", &val[j]);
            solve(0);
        }
    }
    return 0;
}
