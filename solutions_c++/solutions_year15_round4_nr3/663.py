#include <bits/stdc++.h>
using namespace std;

#define A first
#define B second

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef long double ld;

const int maxn = 205;

int n;
vector<string> v[maxn];
vector<int> vi[maxn];
bool flag[10000][2];
map<string, int> comp; int cnt;

void go(int cnum) {
    cerr << cnum << endl;
    comp.clear(); cnt = 0;
    cin >> n;
    string junk; getline(cin, junk);
    for (int i=0; i<n; i++) {
        v[i].clear();
        vi[i].clear();
        string s;
        getline(cin, s);
        int k = 0;
        for (int j=0; j<s.length(); j++) {
            if (s[j] == ' ') {
                v[i].push_back(s.substr(k, j-k));
                k = j+1;
            }
        }
        v[i].push_back(s.substr(k));

        for (string t : v[i]) comp[t] = 0;
    }

    for (auto it=comp.begin(); it!=comp.end(); it++)
        it->second = cnt++;

    for (int i=0; i<n; i++) {
        vi[i].resize(v[i].size());
        for (int j=0; j<v[i].size(); j++)
            vi[i][j] = comp[v[i][j]];
    }

    int m = n-2, ans = 1e9;
    for (int i=0; i<1<<m; i++) {
        memset(flag, 0, sizeof(flag));
        for (int j=0; j<m; j++) {
            bool b = i&1<<j;
            for (int k=0; k<v[j+2].size(); k++)
                flag[vi[j+2][k]][b] = 1;
        }
        for (int j=0; j<v[0].size(); j++)
            flag[vi[0][j]][0] = 1;
        for (int j=0; j<v[1].size(); j++)
            flag[vi[1][j]][1] = 1;

        int num = 0;
        for (int i=0; i<cnt; i++)
            if (flag[i][0] && flag[i][1]) num++;
        ans = min(ans, num);
    }
    cout << "Case #" << cnum << ": " << ans << endl;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t;
    cin >> t;
    for (int i=1; i<=t; i++) go(i);
}
