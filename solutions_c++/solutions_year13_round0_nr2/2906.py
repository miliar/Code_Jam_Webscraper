#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int board[105][105];
int rows, cols;
int maxh, minh;

bool ok(int h) {
    set<int> r, c;
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            if (board[i][j] >= h) {
                r.insert(i);
                c.insert(j);
			}
		}
	}
    for (auto i : r) {
        for (auto j : c) {
            if (board[i][j] < h) return false;
		}
	}
    return true;
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int cases;
    cin >> cases;
    for (int cas = 1; cas <= cases; ++cas) {
        cin >> rows >> cols;
        maxh = 0;
        minh = INT_MAX;
        for (int i = 0; i < rows; ++i) {
            for (int j = 0; j < cols; ++j) {
                cin >> board[i][j];
                maxh = max(maxh, board[i][j]);
                minh = min(minh, board[i][j]);
			}
		}
        bool okay = true;
        for (int h = maxh; h >= minh; --h) {
            okay &= ok(h);
            if (!okay) break;
		}
		cout << "Case #" << cas << ": " << (okay ? "YES" : "NO") << "\n";
	}
}
