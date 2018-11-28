#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <iterator>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <sstream>

using namespace std;

#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define REP(i,n) FOR(i,0,n)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define INF 1000000000
#define X first
#define Y second
#define pb push_back

typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector<PII> VPII;
typedef vector<VI> VVI;

int main () {
    freopen ("input.txt", "r", stdin);
    freopen ("output.txt", "w+", stdout);

    int t;
    cin >> t;
    REP (tt, t) {
        std::cout << "Case #" << tt+1 << ": ";

        int n;
        long long p;
        cin >> n >> p;
        {
            long long X = 0;
            long long Y = (1LL << n)-1;

            while (X<Y) {
                long long x = (X+Y+1) / 2;

                long long  xx = x;
                long long pp = p;
                long long w  = (1<< (n-1));
                REP (i, n) {
                   // cout << x << " " << xx << " " << pp << endl;
                    if (xx == 0) {
                        w/=2;
                    } else {
                        long long wo = w*2 - xx - 1;
                        wo = (wo+1) / 2;
                        xx = w - wo - 1;
                        pp -= w;
                        w/=2;
                    }
                }

                if (pp> 0 )
                    X = x;
                else
                    Y = x-1;
            }
            cout << X << " ";
        }

        {
            long long X = 0;
            long long Y = (1LL << n)-1;

            while (X<Y) {
                long long x = (X+Y+1) / 2;

                long long  xx = x;
                long long pp = p;
                long long nn  = (1<< (n));
                REP (i, n) {
                    if (xx != nn-1) {
                        xx = (xx+1)/2;
                        nn/=2;
                    } else {
                        xx -= nn/2;
                        pp -= nn/2;
                        nn/=2;
                    }
                }

                if (pp > 0)
                    X = x;
                else
                    Y = x-1;
            }
            cout << X << endl;
        }
    }

    return 0;
}
