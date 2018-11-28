#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <string>
#include <iostream>
#include <cmath>
#include <cctype>
#include <sstream>
#include <algorithm>
#include <iomanip>
#include <set>
#include <queue>

using namespace std;

int main()
{
    int T;
    cin >> T;
    for (int sc = 0; sc < T; sc++) {
        int i, j, k;
        int r[2], a[2][4][4];
        for (k = 0; k < 2; k++) {
            cin >> r[k]; r[k]--;
            for (i = 0; i < 4; i++)
                for (j = 0; j < 4; j++)
                    cin >> a[k][i][j];
        }

        k = -1;
        for (i = 0; i < 4; i++)
            for (j = 0; j < 4; j++)
                if (a[0][r[0]][i] == a[1][r[1]][j])
                    if (k == -1) k = a[0][r[0]][i]; else k = -2;
         
        cout << "Case #" << sc+1 << ": ";
        if (k == -1) cout << "Volunteer cheated!";
        else if (k == -2) cout << "Bad magician!";
        else cout << k;
        cout << endl;
    }
    
    return 0;
}
