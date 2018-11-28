#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <ctime>
#include <cassert>
#include <cctype>

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <unordered_map>

using namespace std;

typedef pair<int, int> pii;
typedef vector<int> vi;
typedef long long ll;
typedef unsigned long long ull;
typedef unsigned uint;

template <class T> inline T sqr(const T& a) { return a * a; }
template <class T> inline void updMin(T& a, const T& b) { if (b < a) a = b; }
template <class T> inline void updMax(T& a, const T& b) { if (b > a) a = b; }

const int dx[] = {0, 1, 0, -1};
const int dy[] = {-1, 0, 1, 0};

int getDir(int c)
{
    if (c == '^')
        return 0;
    if (c == '>')
        return 1;
    if (c == 'v')
        return 2;
    if (c == '<')
        return 3;
    throw "bad direction";
}


void solution()
{
    string buf;

    int r, c;
    cin >> r >> c;
    getline(cin, buf);

    vector <string> a(r);
    for (int i = 0; i < r; ++i)
    {
        getline(cin, a[i]);
    }


    int ans = 0;
    for (int i = 0; i < r; ++i)
    {
        for (int j = 0; j < c; ++j)
        {
            int cc = a[i][j];
            if (cc == '.')
                continue;

            //cout << "i = " << i << " " << "j = " << j << ":\n";
            //cout << "getDir = " << getDir(c) << "\n";

            vector <bool> foundDir(4);
            bool foundSmth = false;
            for (int t = 0; t < 4; ++t)
            {
                //cout << "T = " << t << " : \n";
                int x = j;
                int y = i;
                x += dx[t];
                y += dy[t];
                bool found = false;
                while (x >= 0 && x < c && y >= 0 && y < r)
                {
                    //cout << "(x, y) = (" << x << ", " << y << ") " << "\n";
                    if (a[y][x] != '.')
                    {
                        found = true;
                        break;
                    }
                    x += dx[t];
                    y += dy[t];
                }
                foundDir[t] = found;
                foundSmth = foundSmth || found;
                //cout << "found = " << int(found) << " ";
            }
            //cout << "\n##############\n";
            //cout << "\n";

            if (foundDir[getDir(cc)])
                continue;
            if (!foundSmth)
            {
                cout << "IMPOSSIBLE\n";
                return;
            }
            ++ans;

        }
    }

    cout << ans << "\n";

   
}



int main()
{
    //freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);

    ios::sync_with_stdio(false);


    int nTests;
    cin >> nTests;
    for (int test = 1; test <= nTests; ++test)
    {
        cout << "Case #" << test << ": ";
        solution();
        //cout << "\n";
    }



    return 0;
}
