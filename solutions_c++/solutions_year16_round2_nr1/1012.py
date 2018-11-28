#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

string s;
int cnt['Z' + 1];
vector <int> res;

void Check(char ch, string s, int v) {
    if (cnt[ch] == 0) return;
    for(int i = 1; i <= cnt[ch]; ++i) res.push_back(v);

    int vv = cnt[ch];
    for(int i = 0; i < s.size(); ++i)
        cnt[s[i]] -= vv;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int nTests = 0;
    scanf("%d\n", &nTests);
    for(int i = 1; i <= nTests; ++i) {
        cin >> s;
        memset(cnt, 0, sizeof cnt);
        for(int i = 0; i < s.size(); ++i) ++cnt[s[i]];
        res.clear();
        Check('Z', "ZERO", 0);
        Check('W', "TWO", 2);
        Check('X', "SIX", 6);
        Check('S', "SEVEN", 7);
        Check('G', "EIGHT", 8);
        Check('H', "THREE", 3);
        Check('R', "FOUR", 4);
        Check('F', "FIVE", 5);
        Check('O', "ONE", 1);
        Check('I', "NINE", 9);

        sort(res.begin(), res.end());
        printf("Case #%d: ", i);
        for(int v: res) printf("%d", v);
        printf("\n");
    }

    return 0;
}

