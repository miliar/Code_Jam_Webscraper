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


int solve(string str) {
    int cont = 0;
    bool curr = (str[0] == '+');
    for (int i = 0; i < str.size(); ++i) {
        if (curr && str[i] == '-') cont++;
        else if (!curr && str[i] == '+') cont++;

        curr = (str[i] == '+');
    }
    return cont;
}

int main() {
    ios::sync_with_stdio(false);

    int T; cin >> T;

    for (int i = 0; i < T; ++i) {
        string str; cin >> str;

        int s = solve(str + "+");
        cout << "Case #" << i +1 << ": " << s << endl;
    }

    return 0;
}
