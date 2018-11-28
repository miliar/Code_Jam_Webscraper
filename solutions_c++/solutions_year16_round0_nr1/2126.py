#include <bits/stdc++.h>
using namespace std;
typedef long double ld;
typedef complex<ld> pt;
typedef vector<pt> pol;
typedef vector<int> vi;
typedef long long ll;

int main() {
    ios::sync_with_stdio(0);
    int N;
    cin >> N;
    for(int kase=1; kase<=N; kase++) {
        cout << "Case #" << kase << ": ";
        ll m, n, seen=0; cin >> n;
        bool zxcv = false;
        for(ll k=1; k<1000; k++) {
            // pretty sure k just needs to iterate to 10
            m = n*k;
            while(m) {
                seen |= (1LL<<(m%10));
                m/=10;
            }
            //cerr << bitset<9>(seen) << endl;
            if(seen == 1023) {
                if(k >100) {
                    cerr << "WTFFFFFFF" << endl;
                }
                cout << n*k << endl;
                zxcv = true;
                break;
            }
        }
        if(!zxcv) {
            cout << "INSOMNIA" << endl;
        }
        
    }

    return 0;    
}
