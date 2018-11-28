#include <iostream>
#include <cstdio>
#include <vector>
#include <ctime>
#include <cstdlib>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>


#define puba push_back
#define mapa make_pair
#define ff first
#define ss second
#define pii pair < int, int >
#define pdd pair < double, double >


using namespace std;


typedef long long LL;
typedef double DB;


const int INF = 1e9;
const double EPS = 1e-6;


bool eq(DB a, DB b) {
    return (a + EPS > b) && (a - EPS < b);
}


int main() {
    freopen("inp", "r", stdin);
    freopen("outp", "w", stdout);
    int t;
    cin >> t;
    for (int q = 1; q <= t; ++q) {
        int n;
        cin >> n;
        DB v, x;
        cin >> v >> x;

        vector < pdd > fl (n);

        for (int i = 0; i < n; ++i) {
            cin >> fl[i].ff >> fl[i].ss;
        }

       
        
        
        cout << "Case #" << q << ": ";
        if (n == 1) {
            if (!eq(x, fl[0].ss)) {
                cout << "IMPOSSIBLE" << endl;
                continue;
            }
            else {
                printf("%.13lf\n", v / fl[0].ff);
                continue;
            }
        }

        DB ob = 0;
        if (eq(fl[0].ss, x)) {
            ob += fl[0].ff;
        }
        //DB ob = 0;
        if (eq(fl[1].ss, x)) {
            ob += fl[1].ff;
        }

        if (!eq(ob, 0)) {
            printf("%.13lf\n", v / ob);
            continue;
        }

        if (fl[0].ss < fl[1].ss) {
            swap(fl[0], fl[1]);
        }
        if (fl[0].ss + EPS < x || fl[1].ss - EPS > x) {
            cout << "IMPOSSIBLE\n";
            continue;
        }
        DB tt = (fl[0].ss - fl[1].ss) / (x - fl[1].ss);
         
        DB t1 = (v / tt) / fl[0].ff;
        DB t2 = (v / tt) * (fl[0].ss - x) / (x - fl[1].ss) / fl[1].ff;
        printf("%.13lf\n", max(t1, t2));
    }
    return 0;
}