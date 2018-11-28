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

string str;
string result = "";

int solve(int m) {
    int p = 0;
    for (int i = 0; i < m; ++i) {
        if (str[i] > str[p]) p = i;
    }
    return p;
}

int count(char c, int m) {
    int cont = 0;
    for (int i = 0; i < m; ++i) {
        cont += str[i] == c;
    }
    return cont;
}

void solve2(int m) {
    int pos = solve(m);
    int cont = count(str[pos], m);

    if (pos != 0) solve2(pos);

    for (int i = 0; i < cont; ++i) result = str[pos] + result;
    for (int i = pos+1; i < m; ++i) {
        if (str[i] != str[pos]) result = result + str[i];
    }
}

int main() {
    ios::sync_with_stdio(false);

    int T; cin >> T;

    FOR(i,0,T) {
        cin >> str;
        result = "";
        cout << "Case #" << i+1 << ": ";
        solve2(str.size());
        cout << result;
        cout << endl;
    }
    return 0;
}
