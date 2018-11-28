#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <cstring>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <deque>
#include <map>
#include <set>
#include <bitset>
#include <numeric>
#include <utility>
#include <iomanip>
#include <algorithm>
#include <functional>
using namespace std;

typedef long long ll;
typedef vector<int> vint;
typedef vector<long long> vll;
typedef pair<int,int> pint;
typedef pair<long long, long long> pll;

#define MP make_pair
#define PB push_back
#define ALL(s) (s).begin(),(s).end()
#define EACH(i, s) for (__typeof__((s).begin()) i = (s).begin(); i != (s).end(); ++i)
#define COUT(x) cout << #x << " = " << (x) << " (L" << __LINE__ << ")" << endl

template<class T> inline bool chmax(T& a, T b) { if (a < b) { a = b; return 1; } return 0; }
template<class T> inline bool chmin(T& a, T b) { if (a > b) { a = b; return 1; } return 0; }
template<class T1, class T2> ostream& operator << (ostream &s, pair<T1,T2> P) 
{ return s << '<' << P.first << ", " << P.second << '>'; }
template<class T> ostream& operator << (ostream &s, vector<T> P) 
{ for (int i = 0; i < P.size(); ++i) { if (i > 0) { s << " "; } s << P[i]; } return s; }
template<class T> ostream& operator << (ostream &s, vector<vector<T> > P) 
{ for (int i = 0; i < P.size(); ++i) { s << endl << P[i]; } return s << endl; }
template<class T1, class T2> ostream& operator << (ostream &s, map<T1,T2> P) 
{ EACH(it, P) { s << "<" << it->first << "->" << it->second << "> "; } return s; }





const long double INF = 1LL<<60;
const long double EPS = 1e-9;

struct DD {
    long double val;
    
    DD() : val(0) {} 
    DD(long double val_) { this->val = val_; }
    DD operator = (long double val_) { this->val = val_; return *this; }
    inline DD operator - () { return -(this->val); }
    inline const DD& operator += (const DD &x);
    inline const DD& operator -= (const DD &x);
    inline const DD& operator *= (const DD &x);
    inline const DD& operator /= (const DD &x);
};

ostream &operator << (ostream &os, DD x) { return os << x.val;}
istream &operator >> (istream &is, DD &x) { is >> x.val; return is; }
bool operator < (DD x, DD y) { return y.val - x.val > EPS; }
bool operator > (DD x, DD y) { return x.val - y.val > EPS; }
bool operator == (DD x, DD y) { return abs(x.val - y.val) <= EPS; }

inline DD operator + (DD x, DD y) { return x.val + y.val; } 
inline DD operator - (DD x, DD y) { return x.val - y.val; } 
inline DD operator * (DD x, DD y) { return x.val * y.val; } 
inline DD operator / (DD x, DD y) { return x.val / y.val; }
inline const DD& DD::operator += (const DD &x) {*this = *this + x; return *this;}
inline const DD& DD::operator -= (const DD &x) {*this = *this - x; return *this;}
inline const DD& DD::operator *= (const DD &x) {*this = *this * x; return *this;}
inline const DD& DD::operator /= (const DD &x) {*this = *this / x; return *this;}


int n;
DD x[21000], y[21000];

void solve() {
    cin >> n;
    for (int i = 0; i < n; ++i) cin >> x[i] >> y[i];

    if (n <= 3) {
        for (int i = 0; i < n; ++i) cout << 0 << endl;
        return;
    }

    
    for (int i = 0; i < n; ++i) {
        int Min = 1<<29;
        
        int ue = 0, sh = 0, pu = 0, ps = 0;
        for (int j = 0; j < n; ++j) {
            if (j == i) continue;
            if (x[j] > x[i]) ++ue;
            if (x[j] < x[i]) ++sh;
            if (x[j] == x[i] && y[j] < y[i]) ++pu;
            if (x[j] == x[i] && y[j] > y[i]) ++ps;
        }
        chmin(Min, min(ue, sh));
        
        map<DD, pint> ma;
        for (int j = 0; j < n; ++j) {
            if (j == i) continue;
            if (x[j] == x[i]) continue;
            
            DD ang = (y[j] - y[i]) / (x[j] - x[i]);
            
            if (x[j] > x[i]) ma[ang].first++;
            else ma[ang].second++;
        }

//        cout << endl;
//        COUT(i);
//        COUT(ma);
//        cout << "syoki: " << pint(ue, sh) << ", " << pint(pu, ps) << endl;
        
        EACH(it, ma) {
            ue += ps; 
            ue -= it->second.first;
            sh += pu;
            sh -= it->second.second;
            
            pu = it->second.first;
            ps = it->second.second;
            
            //cout << *it << ": " << pint(ue, sh) << ", " << pint(pu, ps) << endl;
            
            chmin(Min, min(ue, sh));
        }
        
        cout << Min << endl;
    }
}

int main() {
    freopen( "/Users/macuser/Dropbox/Contest/C-large.in", "r", stdin );
    freopen( "/Users/macuser/Dropbox/Contest/C-large.out", "w", stdout );
    
    int T;
    scanf("%d", &T);
    for (int XXX = 0; XXX < T; ++XXX) {
        printf("Case #%d:\n", XXX+1);
        solve();
    }
    
    return 0;
}




