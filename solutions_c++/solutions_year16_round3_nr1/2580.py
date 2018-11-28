#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
typedef unsigned long long ULL;
typedef unsigned int UI;
bool cmp(pair<int, char> p1, pair<int, char> p2)
{
    return p1.first > p2.second;
}
int main()
{
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
    ULL T;
    cin >> T;
    for (ULL t = 1; t <= T; ++t) {
        ULL N;
        cin >> N;
        vector<pair<int, char> > vc;
        char ch = 'A';
        ULL total = 0;
        for (ULL n = 0; n < N; ++n) {
            UI x;
            cin >> x;
            total += x;
            pair<int, char> px(x, ch);
            ++ch;
            vc.push_back(px);
        }
        sort(vc.begin(), vc.end());
        string ans;
        while (vc[N-1].first > 0) {
            if (vc[N-1].first == vc[N-2].first) {
                if (total != 3) {
                ans += vc[N-2].second;
                --vc[N-2].first;
                --total;
                }
            }
            ans += vc[N-1].second;
            ans += " ";
            --vc[N-1].first;
                --total;
            sort(vc.begin(), vc.end());
        }
        cout << "Case #" << t << ": " << ans << endl;
    }
}
