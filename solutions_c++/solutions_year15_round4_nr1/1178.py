#include <bits/stdc++.h>
using namespace std;

#define A first
#define B second

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;

const int man = 105;

int n, m;
char mat[man][man];
char car[4] = {'^', '>', 'v', '<'};
int dr[4] = {-1, 0, 1, 0};
int dc[4] = {0, 1, 0, -1};

bool good(int r, int c, int k) {
    r += dr[k], c += dc[k];
    while (1) {
        if (r<0 || r>=n || c<0 || c>=m) return 0;
        if (mat[r][c] != '.') return 1;
        r += dr[k], c += dc[k];
    }
}

void go(int cnum) {
    cin >> n >> m;
    for (int i=0; i<n; i++)
        for (int j=0; j<m; j++)
            cin >> mat[i][j];

    int an = 0;

    for (int i=0; i<n; i++)
        for (int j=0; j<m; j++)
            if (mat[i][j] != '.') {
                int bet = 1000;
                for (int k=0; k<4; k++)
                    if (good(i, j, k))
                        bet = min(bet, car[k] == mat[i][j] ? 0 : 1);
                if (bet == 1000) {
                    cout << "Case #" << cnum << ": " << "IMPOSSIBLE" << endl;
                    return;
                }
                an += bet;
            }

    cout << "Case #" << cnum << ": " << an << endl;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t;
    cin >> t;
    for (int i=1; i<=t; i++) go(i);
}
