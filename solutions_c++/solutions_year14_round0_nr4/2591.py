#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <iostream>
#include <map>
#include <set>
#include <list>

using namespace std;

const int MAX = 1e5;
const int INF = 1e9;
const double EPS = 1e-9;

int main() 
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    double one[1010], two[1010];
    
    int T;
    scanf("%d", &T);
    for(int Ti = 1; Ti <= T; ++Ti)
    {
        int n;
        scanf("%d", &n);
        
        for(int i = 0; i < n; ++i)
            scanf("%lf", (one + i));
        for(int i = 0; i < n; ++i)
            scanf("%lf", (two + i));
        
        sort(one, one + n);
        sort(two, two + n);
        
        int onel = 0, oner = n - 1;
        int twol = 0, twor = n - 1;
        int cntfst = 0, cntscnd = 0;
        while(onel <= oner)
        {
                if(one[onel] > two[twol])
                {
                    ++cntfst;
                    ++twol;
                }
                else
                    --twor;
                ++onel;
        }
        
        bool used[1010];
        for(int i = 0; i < n; ++i)
            used[i] = false;
        
        for(int i = 0; i < n; ++i)            
        {
            double cur = one[i];
            int j = 0;
            for(; j < n && (two[j] < cur || used[j]); ++j)
                ;
            
            if(j == n)
            {
                ++cntscnd;
                for(j = 0; !used[j]; ++j)
                    ;
                used[j] = true;
            }
            else
            {
                used[j] = true;                
            }
        }
        
        printf("Case #%d: %d %d\n", Ti, cntfst, cntscnd);
    }

    return 0;
}

