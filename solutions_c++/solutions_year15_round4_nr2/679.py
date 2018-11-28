#include<bits/stdc++.h>
#define two(a) (1<<(a))
#define LINF (1ll<<61)
#define EPS (1e-14)
#define Lshift(a,b) (a<<b)
#define Rshift(a,b) (a>>b)
#define rep(a,b) for(a=0 ; a<b ; a++)
#define xrep(a,b,c) for(a=b ; a<c ; a++)
#define INF (1<<29)
#define min(a,b) ( a < b ? a : b )
#define max(a,b) ( a > b ? a : b )
#define GET(x) (mark[x>>5]>>(x&31)&1)
#define SET(x) (mark[x>>5]|=1<<(x&31))
#define maxL (10000000>>5)+1
#define mod 1000000007
typedef long long ll;
using namespace std;

vector<pair<double, double> > in;

int main() {
    int t, tt, i, j, k, n;
    double v, x;

    cin >> tt;
    for (t = 1; t <= tt; t++) {
        in.clear();
        cin >> n >> v >> x;
        rep(i, n) {
            double tx, ty;
            cin >> tx >> ty;
            in.push_back({tx, ty});
        }
        if (n == 1) {
            if (abs(x - in[0].second) > 1e-6) { cout << "Case #" << t << ": IMPOSSIBLE" << endl; }
            else { cout << setprecision(20) << "Case #" << t << ": " << v / in[0].first << endl; }
            continue;
        }
        else { 
            if (in[0].second > x && in[1].second > x || in[0].second < x && in[1].second < x) {
                cout << setprecision(20) << "Case #" << t << ": IMPOSSIBLE" << endl;
            }
            else {
                if (abs(x - in[0].second) < 1e-6 && abs(x - in[1].second) < 1e-6) {
                    cout << setprecision(20) << "Case #" << t << ": " << v / (in[0].first + in[1].first) << endl;
                }
                else if (abs(x - in[0].second) < 1e-6) {
                    cout << setprecision(20) <<  "Case #" << t << ": " << v / in[0].first << endl;
                }
                else if (abs(x - in[1].second) < 1e-6) {
                    cout << setprecision(20) << "Case #" << t << ": " << v / in[1].first << endl;
                }
                else {
                    if ( in[0].second > in[1].second) { swap(in[0], in[1]); }
                    double a = x - in[0].second;
                    double b = in[1].second - x;
                    double va, vb;
                    va = v * b / (a+b);
                    vb = v * a / (a+b);
                    cout << setprecision(20) <<  "Case #" << t << ": " << max(va / in[0].first, vb/in[1].first) << endl;
                }
            }
        }
    }
}
