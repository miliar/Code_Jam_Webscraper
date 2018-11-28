// Ticket Swapping / mrozik

#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cassert>
using namespace std;


int N, M;
int grandResult;

vector<pair<int, int> > IN, OUT;

static const int MOD = 1000002013;

__int128 daf;

__int128 cost(int dist, int cnt) {
    __int128 a = ((__int128)N)*N - ((__int128)dist)*(dist-1)/2;
//     a %= MOD;
    a *= cnt;
//     a %= MOD;
    return a;
}



int main() {
    ios_base::sync_with_stdio(false);
    
    int T; cin>>T;
    for (int t=1; t<=T; t++) {
        IN.clear(), OUT.clear();
        __int128 grand0 = 0;
        
        cin>>N>>M;
        
        for (int i=0; i<M; i++) {
            int o, e, p; cin>>o>>e>>p;
            IN.push_back(pair<int, int>(o, p));
            OUT.push_back(pair<int, int>(e, p));
            grand0 += cost(e-o, p);
//             cout<<o<<" -> "<<e<<"  "<<p<<"  "<<cost(e-o, p)<<endl;
        }
        
        sort(IN.begin(), IN.end());
        sort(OUT.begin(), OUT.end());
        
        __int128 grand1 = 0;
        
//         cout<<"   === "<<endl;
        
        for (int b=0; b<M; b++) {
            int a = 0;
            while (a+1<M && IN[a+1].first <= OUT[b].first)
                a++;
            while (OUT[b].second > 0) {
                assert(a>=0);
                int x = min(IN[a].second, OUT[b].second);
                grand1 += cost(OUT[b].first - IN[a].first, x);
//                 cout<<IN[a].first<<" -> "<<OUT[b].first<<"  "<<x<<"  "<<cost(OUT[b].first - IN[a].first, x)<<endl;
                IN[a].second -= x;
                OUT[b].second -= x;
                a--;
            }
        }
        
        int result = (grand0-grand1)%MOD;
//         cout<<grand0<<" "<<grand1<<endl;
        cout<<"Case #"<<t<<": "<<result<<endl;
    }
    
    return 0;    
}
