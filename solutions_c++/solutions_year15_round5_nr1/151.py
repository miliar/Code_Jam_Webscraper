#include <iostream>
#include <algorithm>
#include <vector>
#define F first
#define S second
using namespace std;
typedef long long ll;
const int MN = 1e6+100;
vector<int> v[MN];
ll mm[MN];
ll ss[MN];
ll upMin[MN];
ll upMax[MN];
void f(int x, ll upM, ll upm) {
    upm = min(upm, ss[x]);
    upM = max(upM, ss[x]);
    upMin[x] = upm;
    upMax[x] = upM;
    for(int y: v[x]) {
        f(y, upM, upm);
    }
}
int main() {
    int tt;
    cin>>tt;
    for(int xx = 1; xx <= tt; ++xx) {
        int n,d;
        cin>>n>>d;
        ll as, cs, rs;
        ll  am, cm, rm;
        cin>>ss[0]>>as>>cs>>rs>>mm[0]>>am>>cm>>rm;
        for(int i = 0; i < MN; ++i) {
            v[i].clear();
        }
        vector<pair<int, int> > co;
        co.push_back({ss[0], 0});
        for(int i = 1; i < n; ++i) {
            ss[i] = (ss[i-1]*as + cs) % rs;
            mm[i] = (mm[i-1]*am + cm) % rm;
            v[mm[i]%i].push_back(i);
        }
        f(0, ss[0], ss[0]);
        for(int i = 1; i < n; ++i) {
            co.push_back({upMax[i], i});
        }
        sort(co.begin(), co.end());
        int hi = 0;
        int ans = 0;
        int pois[MN] = {0};
        int best = 0;
//        for(int i = 0; i < n; ++i) {
//            cout<<upMin[i]<<' '<<upMax[i]<<'\n';
//        }
        for(int i = 0; i <= rs; ++i) {
            while(hi < n) {
                int x = co[hi].S;
                int maS = max(upMax[x], ss[x]);
                int miS = min(upMin[x], ss[x]);
                if(maS <= i + d) {
                    ++hi;
                    if(miS >= i) {
                        ++ans;
                        ++pois[miS];
                    }
                }
                else {
                    break;
                }
            }
            best = max(best, ans);
            ans -= pois[i];
        }
        cout<<"Case #"<<xx<<": "<<best<<'\n';
    }
}
