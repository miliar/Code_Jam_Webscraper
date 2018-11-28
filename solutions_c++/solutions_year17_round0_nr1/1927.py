#include <bits/stdc++.h>
using namespace std;

typedef vector<int> veci;
typedef pair<int,int> pii;
typedef vector<pii> vecii;
typedef long long ll;
typedef vector<ll> vecl;
typedef pair<ll,ll> pll;
typedef vector<pll> vecll;
#define EPS (1e-9)
#define MOD (int(1e9+7))
#define INF (int(1e9+9))
#define fi first
#define se second

void flip (string &s, int head, int tail) {
    for (int i=head; i<tail; ++i) {
        if (s[i]=='-') {
            s[i] = '+';
        } else {
            s[i] = '-';
        }
    }
}

int main()
{
    ios::sync_with_stdio(false);
    int tcases;
    cin >> tcases;
    for (int tc=1; tc<=tcases; ++tc)
{
    string s;
    int k;

    cin >> s >> k;
    
    int cnt = 0;
    for (int i=0; i<int(s.length())-k+1; ++i) {
        if (s[i]=='-') {
            flip(s,i,i+k);
            cnt++;
        }
    }

    if (all_of(s.begin(), s.begin()+int(s.length()), [](const char& c){return (c=='+');})) {
        cout << "Case #" << tc << ": " << cnt << endl;
    } else {
        cout << "Case #" << tc << ": " << "IMPOSSIBLE" << endl;
    }
}
    return 0;
}
