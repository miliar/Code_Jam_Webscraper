/**
 *@author:  Orchid
 *@Problem: Counting Sheep
 *@Contest: GCJ 2016
 */
#include <bits/stdc++.h>
#define ULLI unsigned long long int
#define LLI long long int
#define pb push_back
#define mem(a,p) memset(a,p,sizeof(a))
#define fi first
#define se second
#define mp make_pair
#define mt make_tuple
#define tg(p,i) get<i>(p)
#define bitcount __builtin_popcount
#define checkbit(n,b) ((n>>b)&1)
#define gcd __gcd
#define rep(i,a,b) for(int i=a;i<b;++i)
#define all(a) a.begin(),a.end()
#define sz(a) ((int)(a.size()))
#define DREP(a) sort(all(a));a.erase(unique(all(a)),a.end())
#define ns ios_base::sync_with_stdio(false);cin.tie(0)
using namespace std;
#define VI vector<int>
#define PII pair<int,int>
#define VPII vector<pair<int,int>>
#define MOD 1000000007LL
#define EPS 1e-12

char toggle(char c) {
    return (c == '+') ? '-' : '+';
}

int computeAns(string s) {
    int len = s.size(), ans = 0;
    int i, j;
    for (i = len - 1; i >= 0; --i) {
        if (s[i] == '-') {
            s[i] = toggle(s[i]);
            ans++;
            for (j = i - 1; j > 0; --j) {
                if (s[j] == '-') {
                    s[j] = toggle(s[j]);
                } else break;
            }
            i = j + 1;
            for (; j >= 0; --j) {
                s[j] = toggle(s[j]);
            }
        }
    }
    return ans;
}
int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int t, cs = 1;
    string s;
    cin >> t;
    while (t--) {
        cin >> s;
        cout << "Case #" << cs++ << ": " << computeAns(s) << "\n";
    }
    return 0;
}
