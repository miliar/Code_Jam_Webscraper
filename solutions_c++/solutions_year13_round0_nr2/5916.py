#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <sstream>
using namespace std;
typedef long long ll;
const double pi = atan(1.0)*4.0;
const double eps = 1e-8;

bool possible(int column, int row, int** lawn, int dimX, int dimY)
{
    int height = lawn[column][row];
    bool sameRowPossible = true;
    bool sameColumnPossible = true;
    for (int x = 0; x < dimX; ++x) {
        if (lawn[x][row] > height) {
            sameRowPossible = false;
            break;
        }
    }
    for (int y = 0; y < dimY; ++y) {
        if (lawn[column][y] > height) {
            sameColumnPossible = false;
            break;
        }
    }
    return sameRowPossible || sameColumnPossible;
}

void solve(int cnum) {
    int Y, X;
    cin >> Y >> X;
    int res=0;
    int **lawn = new int*[X];
    for(int i = 0; i < X; ++i) {
        lawn[i] = new int[Y]();
    }
    for (int y = 0; y < Y; ++y) {
        for (int x = 0; x < X; ++x) {
            cin >> lawn[x][y];
        }
    }
    for (int y = 0; y < Y; ++y) {
        for (int x = 0; x < X; ++x) {
            if (!possible(x,y,lawn,X,Y)) {
                res = 1;
                break;
            }
        }
    }

    cout << "Case #" << cnum << ": " << (res == 0 ? "YES" : "NO") << endl;;
    //cleanup
    for(int i = 0; i < X; ++i) {
        delete [] lawn[i];
    }
    delete [] lawn;
}

int main() {
    int n;
    cin >> n;
    for (int cnum=1; cnum<=n; cnum++) {
        solve(cnum);
    }
    return 0;
}
