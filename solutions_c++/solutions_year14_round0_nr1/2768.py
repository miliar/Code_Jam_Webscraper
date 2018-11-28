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

int T;
int main() 
{
    freopen("input.txt", "r", stdin);
    freopen("outpu.txt", "w", stdout);
    cin >> T;
    for(int Ti = 1; Ti <= T; ++Ti)
    {
        int f, s;
        int a[4][4], b[4][4];
        cin >> f;
        for(int i = 0; i < 4; ++i)
            for(int j = 0; j < 4; ++j)
                cin >> a[i][j];
        cin >> s;
        for(int i = 0; i < 4; ++i)
            for(int j = 0; j < 4; ++j)
                cin >> b[i][j];
        
        f--, s--;
        int cnt = 0, ld;
        for(int i = 0; i < 4; ++i)
            for(int j = 0; j < 4; ++j)
                if(a[f][i] == b[s][j])
                {
                    ++cnt;
                    ld = b[s][j];
                }
        cout << "Case #" << Ti << ": ";
        if(cnt == 1)
            cout << ld << '\n';
        else if(cnt > 1)
            cout << "Bad magician!\n";
        else
            cout << "Volunteer cheated!\n";
    }

    return 0;
}

