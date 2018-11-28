#include <bits/stdc++.h>
using namespace std;

int main() {
    ifstream cin("testD.in");
    ofstream cout("testD.out");

    int t; cin >> t;
    int cnt = 0;
    
    vector<vector<vector<string>>> cache(21, vector<vector<string>> (21, vector<string> (21, "")));
    
    cache[4][2][4] = "RICHARD";
    cache[4][3][4] = "GABRIEL";

    for(int tCase = 1; tCase <= t; ++tCase) {
        cout << "Case #" << tCase << ": ";
        int n, r, c; cin >> n >> r >> c;

        if(r * c % n || (n > r && n > c) || n > 6 || (n + 1) / 2 > r || (n + 1) / 2 > c) {
            cout << "RICHARD\n";
            continue;
        }

        if((r >= n && c >= n) || (n <= 3)) {
            cout << "GABRIEL\n";
            continue;
        }

        if(r > c)
            swap(r, c);

        cout << cache[n][r][c] << "\n";
    }

    cerr << cnt << "\n";
}
