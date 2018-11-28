#include <cstdio>
#include <algorithm>
using namespace std;

typedef unsigned long long ll;

ll possible(ll a, ll b, ll score, int n) {
    while (b-a > 1) {
        ll c = (a+b)/2;
        ll worse = ((ll)1 << n) - c;
        for (int i=0; i<n; ++i) {
            bool win = (score & ((ll)1 << (n-i-1))) > 0;
            if (win) {
                worse /= 2;
            } else {
                if (worse > 1) {
                    break;
                }
                ll better = ((ll)1 << (n-i)) - worse;
                worse = min(worse, better);
            }
        }
        if (worse) {
            a = c;
        } else {
            b = c;
        }   
    }
    return a;
}

ll must(ll a, ll b, ll score, int n) {
    while(b-a > 1) {
        ll c = (a+b)/2;
        ll better = c + 1;
//        printf("Start %lld, %lld\n", c, better);
        for (int i=0; i<n; ++i) {
            bool win = (score & ((ll)1 << (n-i-1))) > 0;
            if (win) {
          //      printf("Win %lld\n", better);
                if (better > 1) break; 
            } else {
            //    printf("Loose %lld\n", better);
                if (better == 1) break;
                better = better / 2;
 //               printf("%lld\n", better);
            }
        }
        if (better > 1) {
            b = c;
        } else {
            a = c;
        }
    }
    return a;
}

int counter = 0;
void make() {
    printf("Case #%d: ", ++counter);
   
    int n; ll p; scanf("%d %lld", &n, &p);
    ll big = (ll)1 << n;
    printf("%lld ", must(0, big, big-p, n));
    printf("%lld\n", possible(p-1, big, big-p, n));
}

int main() {
    int t; scanf("%d", &t);
    while(t--) {
        make();
    }
    return 0;
}
