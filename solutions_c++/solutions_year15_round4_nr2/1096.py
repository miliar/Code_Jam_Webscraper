#include <bits/stdc++.h>
#include <unistd.h>
using namespace std;
//TEMPLATE {{{
typedef long long lint;
typedef unsigned long long ulint;
typedef long double ldouble;

typedef vector<int> vint;
typedef vector<lint> vlint;
typedef vector<double> vdouble;

#define rep(i,n)         for(int i = 0; i < (int)(n); i++)
#define all(c)           (c).begin(), (c).end()
#define perm(c)          sort(all(c)); for(bool _b = true; _b; _b = next_permutation(all(c)))
#define uniquenize(v)    (v).erase(unique(all(v)), (v).end())

#ifdef HIBIKICHAN
#include <dumper.hpp>
#define dump(x) dumper::dumper(cerr, __LINE__, (#x), (x), 50, 1, 1)
#else
#define dump(x)
#endif

#if defined(_WIN32) || defined(__CYGWIN__)
inline int stoi(const string &s){return atoi(s.c_str());}
inline long long stoll(const string &s){return atoll(s.c_str());}
#endif

//}}}

const double EPS = 1e-9;

double calc(const vector<pair<double, double>> &p, double T, double V){
    double res = 0;
    int n = p.size();

    for(int i = 0; i < n && V > EPS; i++){
        double u = min(V, T*p[i].second);
        V -= u;
        res += u*p[i].first;
    }

    return res;
}

string solve(bool dbg){
    int n; double V, r;
    cin >> n >> V >> r;
    if(dbg) cerr << n << " "<< V <<" "<< r<<endl;
    vector<pair<double, double>> p, q;

    rep(i, n){
        double R, C; cin >> R >> C;
        if(dbg) cerr <<  R << " "  << C << endl;
        p.push_back({C, R});
    }

    sort(all(p));
    q = p; reverse(all(q));

    if(!(p[0].first -EPS < r && r < p[n-1].first + EPS)){
        return "IMPOSSIBLE";
    }

    double L = 0, R = 1e8;

    rep(hoge, 500){

        double M = (L+R)/2;
        //sufficient?
        double VV = 0;
        rep(i, n) VV += p[i].second * M;

        if(VV < V){ //insufficient
            L = M;
        } else {
            double LT = calc(p, M, V);
            double RT = calc(q, M, V);
            assert(LT < RT + EPS);
            if(LT-EPS < r*V && r*V < RT+EPS){ // OK
                R = M;
            } else {
                L = M;
            }
        }
    }

    char str[99];
    sprintf(str, "%.9f", (L+R)/2);
    return string(str);
}

int main(){
    int TEST_CASE; cin >> TEST_CASE;
    for(int i = 1; i <= TEST_CASE; i++){
        string ans = solve(i == 54);
        cout << "Case #" << i << ": " << ans << endl;
    }
}
