#include <bits/stdc++.h>
using namespace std;

char play(char pc1, char pc2) {
    char c1 = min(pc1, pc2);
    char c2 = max(pc1, pc2);
    if (c1 == c2 || c1 == '=' || c2 == '=')
        return '=';
    if (c1 == 'R' && c2 == 'S')
        return 'R';
    if (c1 == 'P' && c2 == 'S')
        return 'S';
    if (c1 == 'P' && c2 == 'R')
        return 'P';
    printf("%c%c\n", c1, c2);
    assert(false);
}

char win(const string &s, int a, int b) {
    if (a == b - 1)
        return s[a];
    if (a == b - 2) {
        return play(s[a], s[b - 1]);
    } else {
        return play(win(s, a, (a+b)/2),
                    win(s, (a+b)/2, b));
    }
}

string comb(const string &a, const string &b) {
    if (a < b)
        return a + b;
    else
        return b + a;
}

string build(char c, int n) {
    if (n == 0)
        return string(1, c);
    if (c == 'R')
        return comb(build('R', n-1), build('S', n-1));
    else if (c == 'S')
        return comb(build('P', n-1), build('S', n-1));
    else if (c == 'P')
        return comb(build('P', n-1), build('R', n-1));
    assert(false);
}

int main() {
    int cases;
    scanf("%d", &cases);
    for (int cs = 1; cs <= cases; cs++) {
        int n, r, p, s;
        scanf("%d%d%d%d", &n, &r, &p, &s);
        bool found = false;
        for (char c : {'R', 'P', 'S'}) {
            string y = build(c, n);
            int count[255];
            memset(count, 0, sizeof(count));
            for (int i = 0; i < int(y.size()); i++)
                count[y[i]]++;
            if (count['P'] == p && count['R'] == r && count['S'] == s) {
                found = true;
                assert(win(y, 0, int(y.size())) == c);
                printf("Case #%d: %s\n", cs, y.c_str());
                break;
            }
        }
        if (!found)
            printf("Case #%d: IMPOSSIBLE\n", cs);
    }
}
