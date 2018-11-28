#include <bits/stdc++.h>

using namespace std;

#define LOG(...) fprintf(stderr,__VA_ARGS__)
//#define LOG(...)
#define FOR(i,a,b) for(int i=(int)(a);i<(int)(b);++i)
#define REP(i,n) for(int i=0;i<(int)(n);++i)
#define ALL(a) (a).begin(),(a).end()
#define RALL(a) (a).rbegin(),(a).rend()
#define EXIST(s,e) ((s).find(e)!=(s).end())
#define SORT(c) sort(ALL(c))
#define RSORT(c) sort(RALL(c))

typedef long long ll;
typedef unsigned long long ull;
typedef vector<bool> vb;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<vb> vvb;
typedef vector<vi> vvi;
typedef vector<vll> vvll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;

int main() {
    int t;
    cin >> t;
    REP(i, t) {
        int n;
        cin >> n;
        if (n == 0) {
            printf("Case #%d: INSOMNIA\n", i+1);
            continue;
        }
        for (int j = 1, all = 0; ; j++) {
            int c;
            int m = n * j;
            while (m > 0) {
                c = m % 10;
                all |= (1 << c);
                m /= 10;
            }
            if (all == 1023) {
                printf("Case #%d: %d\n", i+1, n * j);
                break;
            }
        }
    }
}
