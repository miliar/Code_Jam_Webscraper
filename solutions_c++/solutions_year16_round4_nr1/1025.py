#include <iostream>
#include <map>
#include <string>
#include <vector>
using namespace std;

int T, N, R, P, S;

map<pair<int, int>, string> MEMO; // Type, Depth -> Text
const string CONV[] = {"P", "R", "S"};

string rec(int type, int depth) {
    if (depth == 0) {
        return CONV[type];
    }
    if (MEMO.count(make_pair(type, depth)))
        return MEMO[make_pair(type, depth)];
    string ret;
    if (type == 0) {
        ret = min(rec(0, depth - 1) + rec(1, depth - 1), rec(1, depth - 1) + rec(0, depth - 1));
    } else if (type == 1) {
        ret = min(rec(1, depth - 1) + rec(2, depth - 1), rec(2, depth - 1) + rec(1, depth - 1));
    } else {
        ret = min(rec(2, depth - 1) + rec(0, depth - 1), rec(0, depth - 1) + rec(2, depth - 1));
    }
    return MEMO[make_pair(type, depth)] = ret;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> T;
    for (int TC = 1; TC <= T; ++TC) {
        cin >> N >> R >> P >> S;
        string ans(1 << N, 'Z');
        cout << "Case #" << TC << ": ";
        for (int a = 0; a < 3; ++a) { // Fix this as winner
            string tmp = rec(a, N);
            int tr = 0, tp = 0, ts = 0;
            for (auto e: tmp) {
                if (e == 'P') ++tp;
                else if (e == 'R') ++tr;
                else ++ts;
            }
            if (tr == R && tp == P && ts == S) {
                ans = min(ans, tmp);
            }
        }
        if (ans == string(1 << N, 'Z')) cout << "IMPOSSIBLE\n";
        else cout << ans << "\n";
    }
    return 0;
}
