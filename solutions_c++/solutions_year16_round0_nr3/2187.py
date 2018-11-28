#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <algorithm>

#define ll long long

using namespace std;

string create(int len, int x) {

    string s = "";

    while (x > 0) {
        if (x % 2 == 1) {
            s += "11";
        } else {
            s += "00";
        }
        x /= 2;
    }

    while (s.length() < 2 * len) {
        s += "00";
    }

    return s;

}

void solve(int n, int j) {

    for (int i = 0; i < j; ++i) {
        string s = create((n - 4) / 2, i);
        s = "11" + s + "11";
        cout << s << " ";
        for (int i = 0; i < 9; ++i) {
            cout << i + 3 << " ";
        }
        cout << endl;
    }


}

int main() {

    int T;
    cin >> T;

    for (int i = 0; i < T; ++i) {

        int n, j;
        cin >> n >> j;

        cout << "Case #" << 1 << ": " << endl;

        solve(n, j);

    }

}

