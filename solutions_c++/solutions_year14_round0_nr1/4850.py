#include <iostream>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

string itos(int x) {
    string res = "";
    if (x == 0) return "0";
    while (x != 0) {
        int y = x % 10;
        res += y + '0';
        x /= 10;
    }
    reverse(res.begin(), res.end());
    return res;
}

int main() {
    int t;
    cin >> t;
    for (int I = 1; I <= t; I++) {
        int n; cin >> n;
        vector<vector<int>> v(4);
        for (int i = 0; i < 4; i++) {
            v[i].resize(4);
            for (int &j : v[i]) {
                cin >> j;
            }
        }
        
        vector<vector<int>> w(4);
        int m; cin >> m;
        for (int i = 0; i < 4; i++) {
            w[i].resize(4);
            for (int &j : w[i]) {
                cin >> j;
            }
        }

        int matches = 0;
        int found = 0;
        for (int i = 0; i < 4; i++) {
                for (int j = 0; j < 4; j++) {
                    if (v[n-1][i] == w[m-1][j]) {
                            matches++;
                            found = v[n-1][i];
                    }
                }
        }

        string res;
        if (matches == 1) {
            res = itos(found);           
        } else if (matches == 0) {
            res = "Volunteer cheated!";
        } else {
                res = "Bad magician!";
        }

        cout << "Case #" << I << ": " << res << endl;
    }
    return 0;
}

