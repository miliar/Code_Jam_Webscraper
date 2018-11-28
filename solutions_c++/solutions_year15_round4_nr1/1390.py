#include <iostream>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <cstring>
#include <queue>
#include <ctime>
#include <cassert>
#include <cstdio>
#include <algorithm>
#include <unordered_set>
#include <unordered_map>
#include <bitset>
#include <memory.h>
#include <stack>
#include <cstdlib>


#define fr first
#define sc second
#define mp make_pair
#define pb push_back
#define CLEAR(a, b) memset(a, b, sizeof(a))
#define FOR(i, a, b) for(int i = (a); i < (b); ++i)
typedef long double LD;
typedef long long LL; 

using namespace std;


const int N = -1;
const int INF = 1e9;

int ans;
int T;
int arrow;
string a[101];
int xx[4] = {-1, 0, 1, 0};
int yy[4] = {0, 1, 0, -1};
int b[103][103];
int x[10003], y[10003], t[10003];
int f[10003][4];
int r, c;
int main()
{
    cin >> T;
    FOR(I, 1, T+1)
    {
        cin >> r >> c;
        FOR(i, 0, r)
            cin >> a[i];
        arrow = 0;
        for (int i = 0; i < r; ++i)
            for (int j = 0; j < c; ++j)
            {
                b[i][j] = -1;
                if (a[i][j] != '.')
                {
                    x[arrow] = i;
                    y[arrow] = j;
                    b[i][j] = arrow;
                    if (a[i][j] == '^') t[arrow] = 0;
                    if (a[i][j] == '>') t[arrow] = 1;
                    if (a[i][j] == 'v') t[arrow] = 2;
                    if (a[i][j] == '<') t[arrow] = 3;
                    ++arrow;
                }
            }
        bool exist = true;
        ans = 0;
        for (int i = 0; i < arrow; ++i)
        {
            bool found = false;
            for (int d = 0; d < 4; ++d)
            {
                int tx = x[i], ty = y[i];
                tx += xx[d]; ty += yy[d];
                while (tx >= 0 && tx < r && ty >= 0 && ty < c && b[tx][ty] == -1)
                {
                    tx += xx[d]; 
                    ty += yy[d];
                }
                if (tx < 0 || tx >= r || ty < 0 || ty >= c)
                    f[i][d] = -1;
                else
                {
                    f[i][d] = b[tx][ty];
                    found = true;
                }
                //cout << i << f[i][d] << found << endl;
            }
            if (!found) exist =false;
            if (f[i][t[i]] == -1)
                ans++;
        }
        if (!exist)
            cout << "Case #" << I << ": " << "IMPOSSIBLE"<< endl;
        else
            cout << "Case #" << I << ": " << ans << endl;
    }
}
