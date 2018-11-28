#include<bits/stdc++.h>
typedef long long ll;
using namespace std;

string padding(ll x, size_t n) {
    char buf[256];
    sprintf(buf, "%I64d", x);
    string ans = buf;
    while(ans.length() < n) ans.insert(ans.begin(), '0');
    return ans;
}

struct TAns {
    ll x, y;

    bool operator<(const TAns& other) const {
        return llabs(x - y) < llabs(other.x - other.y) || 
               (llabs(x - y) == llabs(other.x - other.y) && x < other.x) || 
               (llabs(x - y) == llabs(other.x - other.y) && x == other.x && y < other.y);
    }
};

ll calcExtrem(const string& s, size_t i, ll v, bool maxim) {
    for (size_t j = i; j < s.length(); ++j) {
        int d = maxim ? 9 : 0;
        if (s[j] != '?') {
            d = s[j] - '0';
        }
        v = v * 10 + d;
    }    
    return v;
}

TAns calcBest(const string& s1, const string& s2, size_t i, ll v1, ll v2);

TAns subCalcBest(const string& s1, const string& s2, size_t i, ll v1, ll v2, int d1, int d2) {
    if (d1 == d2) {
        return calcBest(s1, s2, i + 1, v1 * 10 + d1, v2 * 10 + d2);    
    }
    if (d1 < d2) {
        return {calcExtrem(s1, i + 1, v1 * 10 + d1, true), calcExtrem(s2, i + 1, v2 * 10 + d2, false)};
    }

    return {calcExtrem(s1, i + 1, v1 * 10 + d1, false), calcExtrem(s2, i + 1, v2 * 10 + d2, true)};
}

TAns calcBest(const string& s1, const string& s2, size_t i, ll v1, ll v2) {
    if (i == s1.length()) {
        return {v1, v2};
    }

    
    if (s1[i] != '?' && s2[i] != '?') {
        return subCalcBest(s1, s2, i, v1, v2, s1[i] - '0', s2[i] - '0');
    }

    if (s1[i] == '?' && s2[i] == '?') {
        bool first = true;
        TAns best;
        for (int d1 = 0; d1 <= 1; ++d1) {
            for (int d2 = 0; d2 <= (d1 == 0); ++d2) {
                TAns variant = subCalcBest(s1, s2, i, v1, v2, d1, d2);
                if (first || variant < best) {
                    best = variant;                
                    first = false;
                }
            }
        }

        return best;
    }

    if (s1[i] == '?') {
        int d2 = s2[i] - '0';
        bool first = true;
        TAns best;
        for (int d1 = max(0, d2 - 1); d1 <= min(9, d2 + 1); ++d1) {
            TAns variant = subCalcBest(s1, s2, i, v1, v2, d1, d2);
            if (first || variant < best) {
                best = variant;                
                first = false;
            }
        }
        return best;
    }
    if (s2[i] == '?') {
        int d1 = s1[i] - '0';
        bool first = true;
        TAns best;
        for (int d2 = max(0, d1 - 1); d2 <= min(9, d1 + 1); ++d2) {
            TAns variant = subCalcBest(s1, s2, i, v1, v2, d1, d2);
            if (first || variant < best) {
                best = variant;                
                first = false;
            }
        }
        return best;
    }

    assert(false);
}


int main() {
    freopen(".in", "r", stdin);
    freopen(".out", "w", stdout);

    int T;
    cin >> T;    
    for (int test = 1; test <= T; ++test) {
        string s1, s2;
        cin >> s1 >> s2;
        const int n = s1.size();
        TAns ans = calcBest(s1, s2, 0, 0, 0);
        cout << "Case #" << test << ": " << padding(ans.x, n) << " " << padding(ans.y, n) << endl;
        cerr << clock() << endl;
    }

    return 0;
}
