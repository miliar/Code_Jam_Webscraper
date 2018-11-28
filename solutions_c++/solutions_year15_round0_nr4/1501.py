#include <bits/stdc++.h>

#define mp make_pair
#define pb push_back
#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define what_is(x) cerr << #x << ": " << x << endl;

using namespace std;

void ans(int t, const char *s) {
    printf("Case #%d: %s\n", t, s);
}

int main() {
    #ifdef LOCAL
        freopen("input", "r", stdin);
        freopen("output", "w", stdout);
    #endif

    int T, X, R, C;
    scanf("%d", &T);
    forn(t, T) {
        cin >> X >> R >> C;
        if (R > C)
            swap(R, C);
        switch(X) {
            case 4:
                if ((R * C) % 4 != 0 || R <= 2) {
                    ans(t + 1, "RICHARD");
                } else {
                    ans(t + 1, "GABRIEL");
                }
                break;
            case 1:
                ans(t + 1, "GABRIEL");
                break;
            case 2:
                if ((R * C) % 2 != 0) {
                    ans(t + 1, "RICHARD");
                } else {
                    ans(t + 1, "GABRIEL");
                }
                break;
            case 3: 
                if ((R * C) % 3 != 0 || R == 1) {
                    ans(t + 1, "RICHARD");
                } else {
                    ans(t + 1, "GABRIEL");
                }
                break;
                
        }
    }

}
