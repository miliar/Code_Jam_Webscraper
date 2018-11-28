#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int n, m;
vector<vector<int> > a;



inline bool checkRow(int row, int x)
{
    int i = 0, barrier = a[row][x];
    for (; i < m; ++i) if (a[row][i] > barrier) break;
    if (i == m) return true;
    i = 0;
    for (; i < n; ++i) if (a[i][x] > barrier) break;
    return i == n;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t;

    scanf("%d", &t);


    for (int i = 1; i <= t; ++i)
    {
        scanf("%i%i", &n, &m);
        a.assign(n, vector<int>(m, 0));
        for (int k = 0; k < n; ++k)
            for (int j = 0; j < m; ++j)
                scanf("%i", &a[k][j]);
        
        bool isOk = true;
        for (int j = 0; j < n && isOk; ++j)
        {
            int k = min_element(a[j].begin(), a[j].end()) - a[j].begin();
            for (int h = 0; h < m; ++h)
                if (a[j][h] == a[j][k] && isOk)
                    isOk = checkRow(j, h);
        }

        if (isOk)
            printf("Case #%i: YES\n", i);
        else
            printf("Case #%i: NO\n", i);
    }
    
    return 0;
}