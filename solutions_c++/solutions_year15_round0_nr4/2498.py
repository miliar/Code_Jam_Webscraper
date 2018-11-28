using namespace std;
#include <bits/stdc++.h>
#define fto(i, l, r) for(int i = l; i <= r; ++i)

int n, r, c;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int nTest;
    scanf("%d", &nTest);
    fto(iTest, 1, nTest) {
        scanf("%d%d%d", &n, &r, &c);
        if (r > c) swap(r, c);
        string s;

        if (n == 1) s = "GABRIEL";
        else if (n == 2) {
            if (r%2 && c%2) s = "RICHARD";
            else s = "GABRIEL";
        }
        else if (n == 3) {
            if (r == 1 || r*c%3) s = "RICHARD";
            else s = "GABRIEL";
        }
        else if (n == 4) {
            if ((r <= 2 && c <= 4) || (r == 3 & c == 3)) s = "RICHARD";
            else s = "GABRIEL";
        }
        printf("Case #%d: %s\n", iTest, s.c_str());
    }
}
