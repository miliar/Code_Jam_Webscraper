#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <queue>
#include <cmath>
#include <set>

#define rep(i,n) for(int i=0;i<(n);i++)

using namespace std;

long long n;

long long fair(long long a, long long b) {
    long long d = b - a;
    return (2 * n + d - 1) * d / 2;
}

void solve() {
    long long ans = 0;
    long long m;
    cin >> n >> m;
    vector<pair<long long, long long> > e(2*m);
    rep(i,m) {
        long long p;
        cin >> e[2 * i].first >> e[2 * i + 1].first >> p;
        e[2 * i].second = -(e[2 * i + 1].second = p);
        ans -= p * fair(e[2 * i].first, e[2 * i + 1].first);
    }

    sort(e.begin(), e.end());
    
    map<long long, long long> list;

    rep(i, 2*m) {
        if (e[i].second < 0) {
            //cerr << e[i].first << " +" << -e[i].second << endl;
            list[e[i].first] += -e[i].second;
        } else {
            //cerr << e[i].first << " " << -e[i].second << endl;
            long long getoff = e[i].second;
            while(getoff) {
                for (typeof(list.rbegin()) it = list.rbegin(); it != list.rend(); ++it) {
                    if (getoff > it->second) {
                        //cerr << "from " << it->first << " to " << e[i].first << endl; 
                        ans += it->second * fair(it->first, e[i].first);
                        getoff -= it->second;
                        it->second = 0;
                    } else {
                        //cerr << "*from " << it->first << " to " << e[i].first << endl; 
                        ans += getoff * fair(it->first, e[i].first);
                        it->second -= getoff;
                        getoff = 0;
                    }
                    if (getoff == 0)break;
                }
            }
        }
    }

    cout << ans << endl;
}

int main() {
    int T;
    cin >> T;
    rep(i,T) {
        cout << "Case #" << i + 1 << ": ";
        solve();
    }
    return 0;
}
