#include <cstdlib>
#include <iostream>
#include <cmath>
#include <string>
#include <iomanip>
#include <sstream>
#include <cstdio>

using namespace std;

int grid [100][100];
int x_max[100], y_max[100];

void solve() {
    int X, Y;
    int x, y;
    
    cin >> X >> Y;
    
    for (x=0; x<X; x++) x_max[x] = 0;
    for (y=0; y<Y; y++) y_max[y] = 0;

    for (x=0; x<X; x++) {
        for (y=0; y<Y; y++) {
            cin >> grid[x][y];
            if (x_max[x] < grid[x][y]) x_max[x] = grid[x][y];
            if (y_max[y] < grid[x][y]) y_max[y] = grid[x][y];
        }
    }
    
    //for (x=0; x<X; x++) cout << x_max[x] << " "; cout << endl;
    //for (y=0; y<Y; y++) cout << y_max[y] << " "; cout << endl;

    
    for (x=0; x<X; x++)
        for (y=0; y<Y; y++)
            if (!(grid[x][y] == x_max[x] || grid[x][y] == y_max[y])) {
                cout << "NO";
                return;
            }
    cout << "YES";
}


int main(int argc, char** argv) {
    int tmax;
    cin >> tmax;
    
    
    for (int t=1; t<=tmax; t++) {
        
        cout << "Case #" << t << ": ";
        solve();
        cout << endl;
    }
}
