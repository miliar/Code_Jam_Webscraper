#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>

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

double sq(double x) {
    return x*x;
}

int main() {
    int np; cin>>np;
    rep(i, np){
        cout << "Case #"<<(i+1)<<": ";

        int garbage;
        int n; cin>>n >> garbage;
        double X[n], Y[n], Z[n];

        rep(i, n){
            cin >> X[i] >> Y[i] >> Z[i];
            cin >> garbage >> garbage >> garbage;
        }

        double D[1000][1000];

        rep(i, n) {
            rep(k,n) {
                D[i][k] = sqrt(sq(X[i] - X[k]) + sq(Y[i] - Y[k]) + sq(Z[i] - Z[k]));
            }
        }

        vector<double> A(n, 1e6);
        vector<bool> V(n, false);

        A[0] = 0.0;

        set<pair<double, int> > s;
        s.insert(make_pair(0.0, 0));
        while(!s.empty()) {
            pair<double, int> bla = *s.begin();
            s.erase(bla);
            int at = bla.second;
            if(V[at]) {
                continue;
            }
            V[at] = true;
            rep(i, n) if(std::max(A[at], D[at][i]) < A[i]) {
                A[i] = std::max(A[at], D[at][i]);
                s.insert(make_pair(A[i], i));
            }
        }

        cout << A[1];
        
        cout << endl;
    }
}
