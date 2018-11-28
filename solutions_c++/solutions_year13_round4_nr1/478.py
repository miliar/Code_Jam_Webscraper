#include <cstdio>
#include <algorithm>
#include <iostream>
using namespace std;

typedef long long ll;

ll calc(int dist, int num, int n) {
    ll res = (ll)dist * (ll)n;
    res -= (ll) dist * ((ll) dist-1) / 2;
    return res * (ll)num;
}

int counter = 0;
void make() {
    printf("Case #%d: ", ++counter);

    ll expected = 0, result = 0;
    int n, m; scanf("%d %d", &n, &m);
    
    vector< pair<int, int> > in, out, inside;
    for (int i=0; i<m; ++i) {
        int x, y, z; scanf("%d %d %d", &x, &y, &z);
        in.push_back(make_pair(x, z));
        out.push_back(make_pair(y, z));
        expected += calc(y-x, z, n);
    }
    sort(in.begin(), in.end());
    sort(out.begin(), out.end());
    
    int i=0;
    for (int j=0; j<m; ++j) {
        while ((i<m) && (in[i].first <= out[j].first)) {
            inside.push_back(in[i++]);
        }
        int p = out[j].first;
        int rest = out[j].second;

        while(rest != 0) {
            int leave = min(rest, inside.back().second);
            result += calc(p - inside.back().first, leave, n);
           
            inside.back().second -= leave;
            if (inside.back().second == 0) inside.pop_back();
            
            rest -= leave;
        }
    }

    printf("%lld\n", expected - result);
}

int main() {
    int t; scanf("%d", &t);
    while(t--) {
        make();
    }
    return 0;
}
