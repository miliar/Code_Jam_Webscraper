#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <algorithm>
#include <map>
#include <cmath>
#include <queue>
#include <stack>
#include <set>

using namespace std;

#define FOR(i, A, B) for(int i=(A); i<(B); i++)
#define REP(i, N) for(int i=0; i<(N); i++)
#define SZ(v) ((int)(v).size())
#define ALL(v) (v).begin(), (v).end()
#define SORT(v) sort(ALL(v))
#define CLEAR(v) memset((v), 0, sizeof(v))
#define MP make_pair
#define PB push_back
#define PII pair<int, int>
#define LL long long

vector<int> primes;
bool _isprime[1<<16];
LL N, J;

void criba() {
    primes.clear();

    REP(i, (1<<16)) _isprime[i] = true;
    _isprime[0] = false;
    _isprime[1] = false;
    FOR(i, 2, (1<<16)) {
        if(!_isprime[i]) continue;
        primes.PB(i);
        int j=2;
        while(i*j < (1<<16)) {
            _isprime[i*j] = false;
            j++;
        }
    }
}

int divs[11];
int nums[11];

bool go(LL n) {
    FOR(b, 2, 11) {
        LL num = 0;
        LL aux = n;
        LL curr = 1;
        while(aux > 0) {
            if(aux&1) num += curr;
            curr *= b;
            aux >>= 1;
        }

        nums[b] = num;

        bool ok = false;
        for(int i=0; i<SZ(primes); i++) {
            if(primes[i] >= num) break;
            if(num % primes[i] == 0) {
                ok = true;
                divs[b] = primes[i];
                break;
            }
        }
        if(!ok) return false;
    }
    return true;
}

int main()
{

    criba();

    int T;
    cin >> T;
    REP(caso, T) {
        
        cout << "Case #" << caso+1 << ":\n";

        cin >> N >> J;

        int found = 0;
        for(int i=0; i<(1<<(N-2)); i++) {
            LL curr = (1<<(N-1)) | (i<<1) | 1;
            if(go(curr)) {
                found++;

                for(int j=N-1; j>=0; j--) cout << ((curr>>j)&1);

                FOR(b, 2, 11) {
                    cout << " " << divs[b];
                    // cout << "(" << nums[b] << ")";
                }
                cout << endl;

                if(found == J) break;
            }
        }
    }
}
