#include <iostream>
#include <string>
#include <map>
#include <stack>
#include <queue>
#include <set>
#include <vector>
#include <utility>
#include <algorithm>

using namespace std;

int table[101][101];
int tabact[101][101];

int refreshtab(int r, int c) {
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            table[i][j] = tabact[i][j] = 0;
            tabact[i][j] = 100;
        }
    }
}
int refreshtabact(int r, int c) {
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            tabact[i][j] = 100;
        }
    }
}

int min(int a, int b) {
    return a < b ? a : b;
}

int max(int a, int b) {
    return a > b ? a : b;
}

void print(int r, int c) {
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            cout << tabact[i][j] << "   ";
        }
        cout << "\t";
        for (int j = 0; j < c; j++) {
            cout << table[i][j] << "   ";
        }
        cout << "\n";
    }
    cout << "\n";
}

bool candorow(int i, int j, int r, int c) {
    for (int colpos = 0; colpos < c; colpos++) {
        if (table[i][j] < table[i][colpos]) {
            return false;
        }
    }
    return true;
}

bool candocol(int i, int j, int r, int c) {
    for (int rowpos = 0; rowpos < r; rowpos++) {
        if (table[i][j] < table[rowpos][j]) {
            return false;
        }
    }
    return true;
}

bool cando(int r, int c) {
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            bool rowcan = candorow(i, j, r, c);
            bool colcan = candocol(i, j, r, c);
            if (!rowcan && !colcan) {
                return false;
            }
        }
    }
    return true;
}

int main() {
    int T;
    cin >> T;
    for (int g = 1; g <= T; g++) {
        int r,c;
        cin >> r >> c;
        refreshtab(r,c);
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                cin >> table[i][j];
            }
        }
        bool res = cando(r, c);
        cout << "Case #" << g << ": " << (res ? "YES" : "NO") << "\n";
    }
    return 0;
}

