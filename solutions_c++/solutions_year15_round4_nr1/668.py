#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>

using namespace std;

string g[1000];
int r, c;

int check(int x, int y) {
    if (g[x][y] == '.')
        return 0;
    int t = 1;
    int f = 0;
    // up
    for (int i = x - 1; i >= 0; --i) {
        if (g[i][y] != '.') {
            f = 1;
            if (g[x][y] == '^')
                t = 0;
        }
    }
    for (int i = x + 1; i < r; ++i) {
        if (g[i][y] != '.') {
            f = 1;
            if (g[x][y] == 'v') {
                t = 0;
            }
        }
    }
    for (int j = y - 1; j >= 0; --j) {
        if (g[x][j] != '.') {
            f = 1;
            if (g[x][y] == '<') {
                t = 0;
            }
        }
    }
    for (int j = y + 1; j < c; ++j) {
        if (g[x][j] != '.') {
            f = 1;
            if (g[x][y] == '>')
                t = 0;
        }
    }
    if (f == 0)
        return -1;
    return t;
}

int calc()
{
    int ans = 0;
    for (int i = 0; i < r; ++i) {
        for (int j = 0; j < c; ++j) {
            int p = check(i, j);
            if (p == -1)
                return -1;
            ans += p;
        }
    }    
    return ans;
}


void work(ifstream &fin, int caseno)
{
    fin >> r >> c;
    for (int i = 0; i < r; ++i) {
        fin >> g[i];
    }
    
    int ans = calc();
    
    if (ans == -1) {
        cout << "Case #" << caseno << ": IMPOSSIBLE" << endl;
    } else {
        cout << "Case #" << caseno << ": " << ans << endl;
    }
}

int main()
{
    ifstream fin;
    fin.open("input");
    int t;
    fin >> t;
    for (int i = 0; i < t; ++i) {
        work(fin, i + 1);
    }
    fin.close();
    return 0;
}
