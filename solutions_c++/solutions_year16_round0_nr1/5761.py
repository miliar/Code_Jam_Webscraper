#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define ld long double
#define pb push_back
#define mp make_pair
#define pii pair<int, int>
#define pll pair<ll, ll>
#define pdd pair<ld, ld>
#define all(x) (x).begin(), (x).end()
#define fi first
#define se second

const int NMAX = 1000005;

int sol[NMAX];

void add(set<int>& s, int x) {
    while (x) {
        s.insert(x % 10);
        x /= 10;
    }
}

int solve(int x) {
    set<int> s;
    for (int i = x;; i += x) {
        add(s, i);
        if (s.size() == 10)
            return i;
    }

}

int main() {
    cin.sync_with_stdio(false);

    int t;
    scanf("%d", &t);
    for (int I = 1; I <= t; I++) {
        int x;
        scanf("%d", &x);

        printf("Case #%d: ", I);

        if (x == 0)
            printf("INSOMNIA\n");
        else
            printf("%d\n", solve(x));
    }

    return 0;
}

