#include <iostream>
#include <iomanip>
#include <cmath>
#include <vector>
#include <algorithm>
#define F first
#define S second
using namespace std;
typedef long double ld;
ld t[1111][3];
ld ufind[1111];
ld f(ld x) {
    return x*x;

}
int find(int a) {
    if(ufind[a] == a) return a;
    return ufind[a] = find(ufind[a]);
}
void merge(int a, int b) {
    ufind[find(a)] = find(b);
}
int main() {
    int  tt;
    cin>>tt;
    for(int xx = 1; xx <= tt; ++xx) {
        cout<<"Case #"<<xx<<": ";
        int n, s;
        cin>>n>>s;
        for(int i = 0; i < n; ++i) {
            ufind[i] = i;
        }
        for(int i= 0; i < n; ++i) {
            for(int j = 0; j < 3; ++j) {
                cin>>t[i][j];
            }
            for(int j = 0; j < 3; ++j) {
                int a;
                cin>>a;
            }
        }
        vector<pair<ld, pair<int , int> > > v;
        for(int i = 0; i < n; ++i) {
            for(int j = 0; j < n; ++j) {
                if(i == j) continue;
                v.push_back({f(t[i][0]-t[j][0]) + f(t[i][1]-t[j][1]) + f(t[i][2] - t[j][2]), {i, j}});
            }
        }
        sort(v.begin(), v.end());
        for(int i = 0; i < v.size(); ++i) {
            merge(v[i].S.F, v[i].S.S);
            if(find(1) == find(0)) {
                cout<<fixed<<setprecision(20)<<sqrt(v[i].F)<<'\n';
                goto ohi;
            }
        }
        ohi:;
    }
}
