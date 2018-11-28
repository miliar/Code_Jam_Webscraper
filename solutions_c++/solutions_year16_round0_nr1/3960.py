#include <bits/stdc++.h>

using namespace std;

#define endl '\n'
#define SZ(c) ((int)(c).size())
#define sqr(x) ((x)*(x))
#define REP(i, c) for(int i=0; i<c; i++)
#ifdef ONLINE_JUDGE
    #define WAIT
#else
    #define WAIT cout<<flush, system("PAUSE")
#endif

typedef long long ll;
typedef pair<int, int> pii;

const int MAXK = 111;
ll tc, n;
bool mk[11];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    
    
    cin >> tc;
    for (int ti = 1; ti <= tc; ti++) {
        cin >> n;
        
        cout << "Case #" << ti << ": ";
        if (n == 0) {
            cout << "INSOMNIA" << endl;
            continue;
        }
            
        memset(mk, false, sizeof mk);
        int cnt = 0;
        for (int k = 1; k < MAXK; k++) {
            ll x = k*n;
            while (x > 0) {
                int d = x % 10;
                x /= 10;
                if (!mk[d]) {
                    mk[d] = true;
                    cnt++;
                }
            }
            if (cnt == 10) {
                cout << k*n << endl;
                break;
            }
        }
        assert(cnt == 10);
    }

//    WAIT;
}
