#include <bits/stdc++.h>
#define fr(i,a,b) for (int i = (a); i < (b); ++i)
using namespace std;

string s;
int ans;

bool isvowel(char c) {
    return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
}

int qnt(const string &ss) {
    int cnt = !isvowel(ss[0]), maxi = cnt;
    fr(i,1,ss.size()) {
        if (!isvowel(ss[i])) ++cnt;
        else {
            maxi = max(maxi, cnt);
            cnt = 0;
        }
    }
    return max(maxi,cnt);
}

int main() {
    freopen("a.in", "r", stdin);
    freopen("a.tx", "w", stdout);
    int nt; scanf("%d", &nt);
    int n, _ = 0;
    while (nt--) {
        cin >> s;
        scanf("%d", &n);
        ans = 0;
        for (int i = 0; i < s.size(); ++i) {
            for (int j = 1; j <= s.size()-i; ++j) {
                string nxt = s.substr(i,j);
                //cout << nxt << " " << qnt(nxt) << endl;
                if (qnt(nxt) >= n)
                    ++ans;
            }
        }
        printf("Case #%d: %d\n", ++_, ans);
    }
    return 0;
}
