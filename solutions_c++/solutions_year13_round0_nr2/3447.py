#include <cassert>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector< vector< int > > field;

bool solve() {
    vector< int > max_on_x(field.size(), 0),
                  max_on_y(field.front().size(), 0);
    for (int x = 0; x < max_on_x.size(); x++)
        for (int y = 0; y < max_on_y.size(); y++) {
            max_on_x[x] = max(max_on_x[x], field[x][y]);
            max_on_y[y] = max(max_on_y[y], field[x][y]);
        }
    for (int x = 0; x < max_on_x.size(); x++)
        for (int y = 0; y < max_on_y.size(); y++)
            if (field[x][y] != max_on_x[x] && field[x][y] != max_on_y[y])
                return false;
    return true;
}

int main() {
    int n;
    cin >> n;
    for (int i = 1; i <= n; i++) {
        int x, y;
        cin >> x >> y;
        field.assign(x, vector< int >(y));
        for (auto &row : field)
            for (auto &cell : row)
                cin >> cell;
        auto ans = solve();
        cout << "Case #" << i << ": " << (ans ? "YES" : "NO") << "\n";
    }
    return 0;
}
