#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <set>
#include <map>
#include <vector>
#include <queue>
using namespace std;

const long long MOD = 1000002013;
const long long INV = 500001007;
int T, M;
long long N;
//pos, 0 in 1 out, num
vector<pair<pair<int,int>, int> > E;
pair<pair<int,int>,int> S[1011];
int sz;

long long cost(long long k) {
    return (k*N%MOD-(k*(k-1)%MOD)*INV%MOD)%MOD;
}

int main(){
    freopen("A-large.in","r",stdin);
    freopen("al.out","w",stdout);
    cin >> T;
    for(int cas = 1; cas <= T; ++cas) {
        E.clear();
        cin >> N >> M;
        int o, e, p;
        long long ans = 0;
        for(int i = 0; i < M; ++i){
            cin >>o>>e>>p;
            E.push_back(make_pair(make_pair(o,0),p));
            E.push_back(make_pair(make_pair(e,1),p));
            ans = (ans+cost(e-o)*p%MOD)%MOD;
        }
        sort(E.begin(), E.end());
        sz = 0;
        for(int i = 0; i < E.size(); i++){
            int x = E[i].first.first, y = E[i].first.second, z = E[i].second;
            if(y == 0){
                S[sz++] = E[i];
            } else{
                while(z > 0) {
                    long long d = min(z, S[sz-1].second);
                    ans = (ans-cost(x-S[sz-1].first.first)*d%MOD)%MOD;
                    S[sz-1].second -= d;
                    z -= d;
                    if(S[sz-1].second == 0)
                        sz--;
                }
            }
        }
        ans = (ans%MOD+MOD)%MOD;
        cout<<"Case #" <<cas<<": "<<ans<<endl;
    }
    return 0;
}
