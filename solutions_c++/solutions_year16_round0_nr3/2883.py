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
#define MAX 100000010
// #define MAX 10010

#define DEBUG false
#define debug(x) if (DEBUG) cout << #x << " = (" << x << ")\n"

int T, N, J;

set<string> s;

typedef long long ll;
bool p[MAX];
vector<ll> P;


void crivo(int m) {
    memset(p, true, sizeof p);
    p[0] = p[1] = false;

    // for (int i = 4; i < MAX; i += 2) p[i] = false;

    P.push_back(2);

    for (int i = 3; i < MAX; i += 2) {
        if (!p[i]) continue;

        P.push_back(i);
        for (int j = 2*i; j < sqrt(i)+5; j += i) p[j] = false;
    }
}

vector<ll> V[1<<15+2];
vector<ll> answers;

ll generate(int mask, int b) {
    ll r = 1;
    ll pot = b;
    int cont = 0;
    while (mask != 0) {
        if (mask & 1) r += pot;
        mask >>= 1;
        pot *= b;
        cont++;
    }
    while (cont++ < N-2) pot *= b;
    r += pot;
    return r;
}

bool is_prime(ll v, ll& div) {
    if (v < 2) return div = v, false;
    if (v % 2 == 0) return div = 2, v == 2;

    for (int i = 0; i < P.size(); ++i) {
        if (P[i] == v) return true;
        if (v % P[i] == 0) return div = P[i], false;
    }

    return true;
}

void solve() {

    for (int i = 0; i < (1<<(N-2)); ++i) {
        bool flag = false;
        // cout << i << endl;
        for (int b = 2; b < 11 && !flag; ++b) {
            ll v = generate(i, b);
            // cout << b << ": " << v << endl;
            ll div;
            flag = flag || is_prime(v, div);

            if (!flag) {/*V[i].push_back(v);*/ V[i].push_back(div);}
        }

        if (!flag) {
            answers.push_back(i);
            if (answers.size() == J) break;
        }

    }
}

string to_str(int mask) {
    string str = "1";
    int cont = 0;
    while (mask != 0) {
        if (mask & 1)   str = "1" + str;
        else            str = "0" + str;
        mask >>= 1;
        cont++;
    }
    while (cont++ < N-2) str = "0" + str;
    str = "1" + str;
    // cout << str << endl;
    return str;
}
int main() {
    ios::sync_with_stdio(false);


    cin >> T;
    cin >> N >> J;

    // cout << generate(5, 4) << endl;
    crivo(MAX);
    solve();

    cout << "Case #1:" << endl;
    for (int i = 0; i < answers.size(); ++i)  {
        int answer = answers[i];
        cout << to_str(answer);
        for (int j = 0; j < V[answer].size(); ++j) cout << " " << V[answer][j];
        cout << endl;
    }
    // for (int i = 0; i < answers.size(); ++i)  {
    //     int answer = answers[i];
    //     // cout << to_str(answer);
    //     for (int j = 0; j < V[answer].size(); ++j) cout << " " << V[answer][j];
    //     cout << endl;
    // }


    return 0;
}
