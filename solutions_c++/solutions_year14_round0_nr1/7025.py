#include <memory.h>
#include <iostream>
#include <algorithm>
#include <cstdio>

using namespace std;

int maze[10][10], used[100];

int main()
{
    freopen("Asmall.out", "w", stdout);
    int t, te;
    cin >> t;
    te = t;
    while(t--)
    {
        memset(used, 0, sizeof(used));
        int r1, r2;
        cin >> r1;
        r1--;
        for(int i = 0; i < 4; i++)
            for(int j = 0; j < 4; j++)
                cin >> maze[i][j];
        for(int i = 0; i < 4; i++)  used[maze[r1][i]]++;
        int q = 0;
        cin >> r2;
        r2--;
        for(int i = 0; i < 4; i++)
            for(int j = 0; j < 4; j++)
                cin >> maze[i][j];
        for(int i = 0; i < 4; i++)  used[maze[r2][i]]++;
        q = 0;
        int ans;
        for(int i = 0; i < 17; i++) if(used[i] == 2) q++, ans = i;
        if(q == 0) cout << "Case #" << te-t << ": Volunteer cheated!\n";
        else if(q == 1) cout << "Case #" << te-t <<": " << ans << endl;
        else cout << "Case #" << te-t << ": Bad magician!\n";
    }
    return 0;
}
