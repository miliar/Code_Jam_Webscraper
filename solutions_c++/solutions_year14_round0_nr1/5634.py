#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <ctime>
#include <climits>
#include <cassert>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <set>
#include <map>
#include <bitset>
#include <utility>
#include <algorithm>

#define forn(i, n) for (int i = 0; i < int(n); i++)

using namespace std;

int main(int argc, char* argv[])
{
    int tt;
    cin >> tt;

    forn(tx, tt)
    {
        int answers[2];
        int a[2][4][4];
        int masks[16] = {0};

        forn(x, 2)
        {
            cin >> answers[x];
            forn(i, 4)
                forn(j, 4)
                    cin >> a[x][i][j];
            forn(j, 4)
                masks[a[x][answers[x] - 1][j] - 1] ^= (1 << x);
        }

        int cnt = 0;
        int v = -1;

        forn(i, 16)
            if (masks[i] == 3)
                cnt++, v = i + 1;

        cout << "Case #" << (tx + 1) << ": ";
        
        if (cnt == 1)
            cout << v << endl;
        else
            if (cnt > 1)
                cout << "Bad magician!" << endl;
            else
                cout << "Volunteer cheated!" << endl;
    }
}

