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

bool prime(ll x) {
    for (ll i = 3; i * i <= x; i += 2)
        if (x % i == 0)
            return 0;

    return 1;
}

bool good(vector<int>& nr) {
    for (int i = 2; i <= 10; i++) {
        ll flc = 0;
        for (int j = 0; j < 16; j++)
            flc = flc * i + nr[j];

        if (prime(flc))
            return 0;
    }

    return 1;
}

ll getdiv(ll x) {
    for (ll i = 3; i * i <= x; i += 2)
        if (x % i == 0)
            return i;
}

void solve(vector<int>& nr) {
    for (int i = 0; i < 16; i++)
        cout << nr[i];

    cout << " ";
    for (int i = 2; i <= 10; i++) {
        ll flc = 0;
        for (int j = 0; j < 16; j++)
            flc = flc * i + nr[j];

        cout << getdiv(flc) << " ";
    }

    cout << '\n';
}

int main() {
    srand(time(0));
    cin.sync_with_stdio(false);

    freopen("c.out", "w", stdout);

    int n = 16;
    int j = 50;

    vector<int> nr;
    vector<vector<int>> sol;
    while (1) {
        nr.clear();
        for (int i = 0; i < 16; i++)
            nr.pb(0);

        nr[0] = nr[15] = 1;

        int k = rand() % 15;
        vector<int> mlc;
        for (int i = 1; i < 15; i++)
            mlc.pb(i);

        random_shuffle(all(mlc));

        for (int i = 0; i < k; i++)
            nr[mlc[i]] = 1;

        bool bagpula = 0;
        for (int i = 0; i < (int)sol.size(); i++) {
            bool same = 1;
            for (int j = 0; j < 16; j++)
                if (sol[i][j] != nr[j])
                    same = 0;

            if (same) {
                bagpula = 1;
                break;
            }
        }

        if (bagpula)
            continue;

        if (good(nr))
            sol.pb(nr);

        if (sol.size() == j)
            break;
    }

    cout << "Case #1:" << '\n';
    for (int i = 0; i < (int)sol.size(); i++, cerr << endl) {
        solve(sol[i]);
    }

    return 0;
}

