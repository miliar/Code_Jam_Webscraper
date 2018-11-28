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

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    LLI t, n, cs = 1;
    cin >> t;
    while (t--) {
        set<LLI>digits = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
        cin >> n;
        if (n == 0) {
            cout << "Case #" << cs++ << ": " << "INSOMNIA" << "\n";
            continue;
        }
        LLI temp = n, i = 1;
        while (true) {
            temp = n * i;
            while (temp != 0) {
                LLI r = temp % 10;
                temp = temp / 10;
                if (digits.find(r) != digits.end()) {
                    digits.erase(r);
                }
            }
            if (digits.size() == 0) {
                cout << "Case #" << cs++ << ": " << n*i << "\n";
                break;
            }
            i++;
        }
    }
    return 0;
}
