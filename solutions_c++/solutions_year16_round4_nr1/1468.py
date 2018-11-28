#include <bits/stdc++.h>

using namespace std;

int n, r, p, s;

string temp;
string ans;

bool win(char a, char b) {
    if (a == 'R') return b == 'S';
    if (a == 'S') return b == 'P';
    if (a == 'P') return b == 'R';
}

bool ok(string a) {
    int log = n;
    for (int it = 0; it < log; ++it) {
        string newA = "";
        for (int i = 0; i < a.size(); i += 2) {
            if (a[i] == a[i + 1]) return false;
            if (win(a[i], a[i + 1]))
                newA += a[i];
            else
                newA += a[i + 1];
        }
        a = newA;
    }
    return true;
}

void go(int i, int r, int p, int s) {;
    if (ans != "") return;
    if (i == (1 << n)) {
        if (ok(temp))
            ans = temp;
        return;
    }
    if (p > 0) {
        temp += 'P';
        go(i + 1, r, p - 1, s);
        temp.erase(temp.size() - 1);
    }
    if (r > 0) {
        temp += "R";
        go(i + 1, r - 1, p, s);
        temp.erase(temp.size() - 1);
    }
    if (s > 0) {
        temp += "S";
        go(i + 1, r, p, s - 1);
        temp.erase(temp.size() - 1);
    }
}

string naive() {
    temp = "";
    ans = "";
    go(0, r, p, s);
    if (ans == "") ans = "IMPOSSIBLE";
    return ans;
}

int main() {
    //freopen("input.txt", "r", stdin);
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int ntest; cin >> ntest;
    for (int it = 1; it <= ntest; ++it) {
        cout << "Case #" << it << ": ";
        cin >> n >> r >> p >> s;
        cout << naive() << endl;
    }
    return 0;
}
