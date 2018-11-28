#include <bits/stdc++.h>
#define _ << " " <<

#define X first
#define Y second

using namespace std;

typedef pair<int, int> Point;
typedef long long lint;
char out[1050];

void solve() {
    string str; cin >> str;
    int len = str.size();
    string out = "";

    for(int i = 0; i < len; ++i) {
        bool after = true;
        for(int j = 0; j < i; ++j) {
            if(out[j] == str[i]) continue;
            if(out[j] < str[i]) {
                after = false;
                break;
            } else {
                break;
            }
        }
        if(after)
            out += str[i];
        else
            out = str[i] + out;
        //cerr << "tmp:" _ out << endl;
    }

    cout << out << endl;


}


int main() {
    ios_base::sync_with_stdio(false);
    int T; cin >> T;

    for(int t = 1; t <= T; ++t) {
        cout << "Case #" << t << ": ";
        solve();
    }
    return 0;
}

