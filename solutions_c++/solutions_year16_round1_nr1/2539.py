#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <string>

using namespace std;

string s;
string f;
void solve() {
    int len = s.size();
    f = "";
    f = f + s[0];
    for(int i = 1;i < len; i++) {
        string a = s[i] + f;
        string b = f + s[i];
        if(a > b) {
            f = a;
        }
        else {
            f = b;
        }
    }
    cout << f << endl;
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("Aout.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for(int i = 1; i <= t; i++) {
        printf("Case #%d: ", i);
        cin >> s;
        solve();
    }
    return 0;
}

