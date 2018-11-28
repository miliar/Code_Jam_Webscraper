#include <iostream>
#include <fstream>
#include <vector>
#include <iomanip>
#include <cstdlib>
#include <cstring>
#include <string>
#include <algorithm>
#include <set>
#include <queue>
#include <map>

#define pb push_back
#define mp make_pair
#define F first
#define S second

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef long double ld;

const int INF = int(1e9);
const int MOD = int(1e9) + 7;
const ll INFll = 1ll * INF * INF;

int a[4][4];

void read() {
    for (int i = 0; i < 4; ++i)
       for (int j = 0; j < 4; ++j)
            cin >> a[i][j];
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    #ifdef LOCAL
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif
    int t;
    cin >> t;
    for (int o = 1; o <= t; ++o) {
        cout << "Case #" << o << ": ";
        int x;
        cin >> x;
        x--;
        read();
        vi u(17);
        for (int i = 0; i < 4; ++i)
            u[a[x][i]] = 1;
        cin >> x;
        x--;
        read();
        int k = 0;
        for (int i = 0; i < 4; ++i)
            if (u[a[x][i]])
                k++;
        if (k == 0)
            cout << "Volunteer cheated!";
        else
            if (k > 1)
                cout << "Bad magician!";
            else {
                for (int i = 0; i < 4; ++i)
                    if (u[a[x][i]]) {
                        cout << a[x][i];
                    }
            }
        cout << endl;
    }
    return 0;
}

