#include <iostream>
#include <stdio.h>
#include <map>
#include <set>
#include <vector>
#include <algorithm>
#include <math.h>

using namespace std;

int m1[5][5];
int m2[5][5];
int r1, r2;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for(int i = 0 ; i < t ; ++i)
    {
        cin >> r1;
        for(int i = 0 ; i < 4 ; ++i)
            for(int j = 0 ; j < 4 ; ++j)
                cin >> m1[i][j];
        cin >> r2;
        for(int i = 0 ; i < 4 ; ++i)
            for(int j = 0 ; j < 4 ; ++j)
                cin >> m2[i][j];
        
        cout << "Case #" << i+1 << ": ";
        
        --r1, --r2;
        int ans = -1, cnt = 0;
        for(int k = 0 ; k < 4 ; ++k)
        {
            for(int p = 0 ; p < 4 ; ++p)
            if(m2[r2][p] == m1[r1][k])
            {
                ans = m1[r1][k];
                ++cnt;
            }
        }
        if(cnt == 0)
            cout << "Volunteer cheated!\n";
        else if(cnt > 1)
            cout << "Bad magician!\n";
        else
            cout << ans << "\n";
    }
    return 0;
}
