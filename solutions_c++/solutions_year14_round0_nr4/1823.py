#include <algorithm>
#include <iostream>
#include <map>
#include <set>
#include <vector>
#include <complex>
#include <cstring>
#include <cstdio>
#include <queue>

using namespace std;

int T, n;
double val;
deque<double> q1, q2;
set<double> s2;
double s1[10000];

int main() {
    freopen("D-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    cin>>T;
    int cs = 0;
    while (T--) {
        cin>>n;
        q1.clear(); q2.clear(); s2.clear();
        for (int i = 0; i < n; i++) {
            cin>>val; q1.push_back(val); s1[i] = val;
        }
        for (int i = 0; i < n; i++) {
            cin>>val; q2.push_back(val); s2.insert(val);
        }
        sort(q1.begin(), q1.end());
        sort(q2.begin(), q2.end());
        int ans = 0;
        for (int i = 0; i < n; i++) {
            int ca = 0;
            for (int j = 0; j < q2.size(); j++) {
                if (q1[j] > q2[j]) ++ca;
            }
            ans = max(ans, ca);
            q1.pop_front(); q2.pop_back();
        }
        int ans2 = 0;
        for (int i = 0; i < n; i++) {
            set<double>::iterator it = s2.upper_bound(s1[i]);
            if (it != s2.end()) ++ans2, s2.erase(it);
        }
        ans2 = n - ans2;
        printf("Case #%d: ", ++cs);
        cout<<ans<<" "<<ans2<<endl;

    }
    return 0;
}
