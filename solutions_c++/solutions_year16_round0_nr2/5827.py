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

vector<int> v;

int main() {
    cin.sync_with_stdio(false);

    int t;
    cin >> t;
    for (int I = 1; I <= t; I++) {
        string s;
        cin >> s;

        while (!s.empty() && s.back() == '+')
            s.pop_back();

        int cnt;
        if (s.empty()) cnt = 0;
        else cnt = 1;

        for (int i = 1; i < (int)s.size(); i++)
            if (s[i] != s[i - 1])
                cnt++;

        cout << "Case #" << I << ": " << cnt << '\n';
    }

    return 0;
}

