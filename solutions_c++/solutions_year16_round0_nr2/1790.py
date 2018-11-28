#include <bits/stdc++.h>
using namespace std;

string s;
int ans;

void perform(int ind) {
    string ex = "";
    for (int i = ind; i >= 0; i--) {
        if (s[i] == '+') ex += "-";
        else ex += "+";
    }
    for (int i = 0; i <= ind; i++) s[i] = ex[i];
    ans++;
}

void plusex() {
    int ind = -1;
    for (int i = 0; i < s.length() && ind == -1; i++) {
        if (s[i] == '-') ind = i;
    }
    if (ind > 0) perform(ind - 1);
}

int main(void) {
    if (fopen("b-small.in", "r")) {
        freopen("b-small.in", "r", stdin);
        freopen("b-small.out", "w", stdout);
    }
    if (fopen("b-large.in", "r")) {
        freopen("b-large.in", "r", stdin);
        freopen("b-large.out", "w", stdout);
    }
    int t;
    cin >> t;
    for (int ii = 1; ii <= t; ii++) {
        cin >> s;
        ans = 0;
        int ind = s.length() - 1;
        while (ind >= 0) {
            while (ind >= 0 && s[ind] == '+') ind--;
            if (ind >= 0) {
                plusex();
                perform(ind);
            }
        }
        printf("Case #%d: %d\n", ii, ans);
    }
    return 0;
}
