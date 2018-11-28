#include <iostream>
#include <algorithm>

using namespace std;

int t;
int n;
int r, p, s;

string gen(string x, int n) {
    if (n == 0) return x;
    if (x == "R") {
        string a = gen("R",n-1);
        string b = gen("S",n-1);
        if (a < b) return a + b;
        else return b + a;
    }
    if (x == "S") {
        string a = gen("P",n-1);
        string b = gen("S",n-1);
        if (a < b) return a + b;
        else return b + a;
    }
    if (x == "P") {
        string a = gen("P",n-1);
        string b = gen("R",n-1);
        if (a < b) return a + b;
        else return b + a;
    }
}

bool ok(string x, int r, int p, int s) {
    for (int i = 0; i < x.size(); i++) {
        if (x[i] == 'R') r--;
        if (x[i] == 'P') p--;
        if (x[i] == 'S') s--;
    }
    return r == 0 && p == 0 && s == 0;
}

void solve(int z) {
    cout << "Case #" << z << ": ";
    cin >> n >> r >> p >> s;
    string u;
    string x;
    x = gen("R",n);
    if (ok(x,r,p,s) && (u == "" || x < u)) u = x;
    x = gen("S",n);
    if (ok(x,r,p,s) && (u == "" || x < u)) u = x;
    x = gen("P",n);
    if (ok(x,r,p,s) && (u == "" || x < u)) u = x;
    if (u == "") cout << "IMPOSSIBLE\n";
    else cout << u << "\n";
}

int main() {
    cin >> t;
    for (int i = 1; i <= t; i++) solve(i);
}
