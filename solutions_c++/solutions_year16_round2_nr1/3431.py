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

int ok;
string v[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
unordered_map<char, int> f;
vector<int> st;

void back(int n) {
    if (n == 0) {
        for (auto it : st)
            cout << it;
        cout << '\n';
        ok = 1;
        return;
    }

    int last;
    if (st.empty())
        last = 0;
    else
        last = st.back();

    for (int i = last; i < 10; i++) {
        if (ok)
            return;

        int mlc = 100;
        for (auto c : v[i]) {
            if ((i == 3 || i == 7) && c == 'E')
                mlc = min(mlc, f[c] / 2);
            else if (i == 9 && c == 'N')
                mlc = min(mlc, f[c] / 2);
            mlc = min(mlc, f[c]);
        }

        if (mlc) {
            st.pb(i);
            for (auto c : v[i])
                f[c]--;
            back(n - v[i].size());
            st.pop_back();
            for (auto c : v[i])
                f[c]++;
        }
    }
}

int main() {
    cin.sync_with_stdio(false);


    int t;
    cin >> t;
    for (int I = 1; I <= t; I++) {
        string s;
        cin >> s;

        f.clear();
        for (auto c : s)
            f[c]++;

        cout << "Case #" << I << ": ";
        ok = 0;
        back(s.size());
    }

    return 0;
}
