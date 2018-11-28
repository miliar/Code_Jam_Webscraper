#include <iostream>
#include <algorithm>
#include <vector>


using namespace std;

string count(int n, int& a, char A, int& b, char B, int& c, char C) {
    if (n) {
        string r = count(n-1, a, A, b, B, c, C);
        string s = count(n-1, b, B, c, C, a, A);
        if (r < s) return r + s;
        else return s + r;
    } else {
        a += 1;
        return string(1, A);
    }
}

void tc() {
    int N, R, P, S;
    cin >> N >> R >> P >> S;
    int r = 0, p = 0, s = 0;
    vector<string> rr;
    string res;
    if ((res = count(N, r, 'R', s, 'S', p, 'P')), r == R && p == P && s == S) rr.push_back(res);
    r = p = s = 0;
    if ((res = count(N, s, 'S', p, 'P', r, 'R')), r == R && p == P && s == S) rr.push_back(res);
    r = p = s = 0;
    if ((res = count(N, p, 'P', r, 'R', s, 'S')), r == R && p == P && s == S) rr.push_back(res);
    static int cas = 1;
    cout << "Case #" << cas++ << ": ";
    if (rr.size()) cout << rr[0];
    else cout << "IMPOSSIBLE";
    cout << endl;
}

int main() {
    int T;
    cin >> T;
    while (T--) tc();
}
