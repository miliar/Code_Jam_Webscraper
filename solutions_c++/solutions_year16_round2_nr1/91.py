#include<bits/stdc++.h>
typedef long double ld;
typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int uint;
using namespace std;

void Add(vector<int>& cnt, char ch, char ansc, string phrase, string& ans) {
    int x = cnt[ch - 'A'];
    for (int i = 0; i < phrase.length(); ++i) {
        cnt[phrase[i] - 'A'] -= x;
        assert(cnt[phrase[i] - 'A'] >= 0);
    }

    for (int i = 0; i < x; ++i) ans += ansc;
}


int main() {
    freopen(".in", "r", stdin);
    freopen(".out", "w", stdout);

    int T;
    cin >> T;    
    for (int test = 1; test <= T; ++test) {
        string s;
        cin >> s;
        vector<int> cnt(27);
        for (int i = 0; i < s.length(); ++i) {
            int x = s[i] - 'A';
            cnt[x] += 1;
        }

        string ans;
        Add(cnt, 'Z', '0', "ZERO", ans);
        Add(cnt, 'X', '6', "SIX", ans);
        Add(cnt, 'W', '2', "TWO", ans);
        Add(cnt, 'S', '7', "SEVEN", ans);
        Add(cnt, 'V', '5', "FIVE", ans);
        Add(cnt, 'G', '8', "EIGHT", ans);
        Add(cnt, 'I', '9', "NINE", ans);
        Add(cnt, 'F', '4', "FOUR", ans);
        Add(cnt, 'O', '1', "ONE", ans);
        Add(cnt, 'T', '3', "THREE", ans);
        sort(ans.begin(), ans.end());
        assert(cnt == vector<int>(27));

        cout << "Case #" << test << ": " << ans << endl;
    }

    return 0;
}
