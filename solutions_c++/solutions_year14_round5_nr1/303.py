#include <bits/extc++.h>
#include <iostream>
#include <iomanip>

using namespace std;

//#define NDEBUG
#ifdef NDEBUG
#define DEBUG if (false)
#else
#define DEBUG if (true)
#endif
#define WRITE(x) DEBUG { cout << (x) << endl; }
#define WATCH(x) DEBUG { cout << #x << " = " << (x) << endl; }
//#define ALL(x) (x).begin(), (x).end()
//#define FORN(i, a, b) for(typeof(b) i = (a); i < (b); ++i)
//#define FOREACH(i, c) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)

typedef long long ll;

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	int ntc;
	cin >> ntc;
	for(int tc = 0; tc < ntc; tc++){
        int n;
        ll p, q, r, s;
        cin >> n >> p >> q >> r >> s;
        vector<ll> psum(n + 1);
        for(int i = 1; i <= n; i++){
            ll xi = ((i - 1) * p + q) % r + s;
            //cout << xi << endl;
            psum[i] = psum[i - 1] + xi;
        }

        ll sol = 0;
        
        for(int b = 0; b < n; b++){
            int lb = b;
            int ub = n - 1;
            ll left = psum[b];
            while(lb + 6 < ub){
                ll m1 = (ub - lb) / 3 + lb;
                ll m2 = ((ub - lb) / 3) * 2 + lb;
                //cout << '[' << lb << ", " <<  ub << "] - " << m1 << ' ' << m2 << endl;

                ll mid1 = psum[m1 + 1] - psum[b];
                ll right1 = psum[n] - psum[m1 + 1];
                ll f1 = max(left, max(mid1, right1));
                
                ll mid2 = psum[m2 + 1] - psum[b];
                ll right2 = psum[n] - psum[m2 + 1];
                ll f2 = max(left, max(mid2, right2));

                //cout << f1 << ' ' << f2 << endl;

                if(f1 < f2){
                    ub = m2 - 1;
                }else if(f1 > f2){
                    lb = m1 + 1;
                }else{
                    lb = m1;
                    ub = m1;
                }
                //cout << lb << ' ' << ub << endl;
            }

            while(lb <= ub){
                ll mid = psum[lb + 1] - psum[b];
                ll right = psum[n] - psum[lb + 1];
                ll f = max(left, max(mid, right));
                ll value = psum[n] - f;
                sol = max(sol, value);
                //cout << "*[" << b << ", " << lb << "] - " << value << endl;
                lb++;
            }
        }
        
        double prob = double(sol) / double(psum[n]);
        cout << "Case #" << (tc + 1) << ": " << fixed << setprecision(10) << prob << "\n";
	}
}
