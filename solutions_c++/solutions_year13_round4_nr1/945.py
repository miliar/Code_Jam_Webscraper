#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;
#define MOD 1000002013

int main() {
int _t; scanf("%d", &_t);
for(int _i=1; _i<=_t; _i++) {
    int n, m; scanf("%d %d", &n, &m);
    vector<pair<int, int> > ev;
    int total=0;
    for(int i=0; i<m; i++) {
        int o, e, p; scanf("%d %d %d", &o, &e, &p);
        ev.push_back(make_pair(o, -p));
        ev.push_back(make_pair(e, p));
        int d = e-o;
        total += p * (d*n - d*(d-1)/2);
        total %= MOD;
    }
    sort(ev.begin(), ev.end());
    //for(int i=0; i<ev.size(); i++) printf("%d: %d %d\n", i, ev[i].first, ev[i].second);
    vector<pair<int, int> > s;
    //printf("total: %d\n", total);
    for(int i=0; i<ev.size(); i++) {
        ev[i].second *= -1;
        if(ev[i].second > 0) {
            s.push_back(ev[i]);
        } else {
            while(ev[i].second != 0) {
                if(s.back().second >= -ev[i].second) {
                    int d = ev[i].first - s.back().first;
                    //printf("Subtracting %d\n", ev[i].second * (d*n - d*(d-1)/2));
                    total -= -ev[i].second * (d*n - d*(d-1)/2);
                    total %= MOD;
                    s.back().second += ev[i].second;
                    ev[i].second = 0;
                } else {
                    ev[i].second += s.back().second;
                    int d = ev[i].first - s.back().first;
                    //printf("Subtracting %d\n", s.back().second * (d*n - d*(d-1)/2));
                    total -= s.back().second * (d*n - d*(d-1)/2);
                    total %= MOD;
                    s.pop_back();
                }
            }
        }
    }
    printf("Case #%d: %d\n", _i, total);
}
}
        
        
