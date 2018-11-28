#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    int t;
    cin >> t;
    
    for (int test = 0; test < t; test++)
    {
        int n, m;
        cin >> n >> m;
        int A[n][m], table[n][m];
        
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                cin >> A[i][j], table[i][j] = 100;
        
        for (int i = 0; i < n; i++)
        {
            int best = -1;
            
            for (int j = 0; j < m; j++)
                best = max(best, A[i][j]);
            
            for (int j = 0; j < m; j++)
                table[i][j] = min(table[i][j], best);
        }
        
        for (int j = 0; j < m; j++)
        {
            int best = -1;
            
            for (int i = 0; i < n; i++)
                best = max(best, A[i][j]);
            
            for (int i = 0; i < n; i++)
                table[i][j] = min(table[i][j], best);
        }
        bool flag = 1;
        
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                if (A[i][j] != table[i][j])
                    flag = 0;
        printf("Case #%d: %s\n", test + 1, (flag ? "YES" : "NO"));
    }
}
