#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> ii;
typedef long long ll;
typedef unsigned long long ull;

#define fi first
#define se second
#define mp make_pair
#define pb push_back

#define FOR(i,a,b) for(int (i) = (a); (i) < (b); ++(i))

#define INF 0x3f3f3f3f
#define MAX -1

#define DEBUG false
#define debug(x) if (DEBUG) cout << #x << " = (" << x << ")\n"

bool digits[10];
int cont;

bool mark(int n) {

    while (n != 0) {
        int rest = n % 10;
        if (digits[rest] == false) cont++;

        digits[rest] = true;

        n /= 10;
    }

    return cont == 10;
}

int solve(int n) {
    memset(digits, false, sizeof digits);
    cont = 0;
    int i;

    bool flag = false;
    for (i = 1; i < 100; ++i) {
        if (mark(i * n)) { flag = true; break; }
    }

    return (flag) ? i*n : -1;
}

int main() {
    ios::sync_with_stdio(false);

    int T; cin >> T;

    for (int i = 0; i < T; ++i) {
        int N; cin >> N;
        int s = solve(N);

        if (s == -1)
            cout << "Case #" << i +1 << ": INSOMNIA"  << endl;
        else
            cout << "Case #" << i +1 << ": " << s << endl;
    }

    return 0;
}
