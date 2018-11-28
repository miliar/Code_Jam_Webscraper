#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <iomanip>

#define For(i,a,b) for(int i = a; i < b; i++)
#define rep(i,x) For(i,0,x)
#define foreach(i,c) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define sz(x) ((int)(x).size())
#define F first
#define S second
#define pb push_back
#define mp make_pair
#define TWO(x) (1LL<<(x))

using namespace std;

double DP[205][205]; //[loc][heads]

double solve(vector<double>& vec) {
    int n = vec.size();

    rep(loc, n+1) {
        rep(heads, n+1){ 
            DP[loc][heads] = 0.0;
        }
    }
    DP[0][0] = 1.0;

    rep(loc, n) {
        rep(heads, n) {
            double cur = DP[loc][heads];
            DP[loc+1][heads+1] += cur * vec[loc];
            DP[loc+1][heads] += cur * (1.0 - vec[loc]);
        }
    }

    return DP[n][n/2];
}


int main() {
    int np; cin>>np;
    rep(i, np){

        int n,k; cin>>n>>k;
        
        vector<double> p(n);
        rep(i, n) {
            cin >> p[i];
        }

        sort(p.begin(), p.end());

        double ans = 0.0;
        rep(i, k+1) {
            vector<double> cur;
            rep(j, i) {
                cur.push_back(p[j]);
            }
            for(int j=n - (k - i); j<n; j++) {
                cur.push_back(p[j]);
            }

            ans = max(ans, solve(cur));
        }
                
        cout << "Case #"<<(i+1)<<": ";
        cout << fixed << setprecision(15) << ans << endl;
    }
}
