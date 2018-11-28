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



struct Quat {
    int c;
    
    Quat() : c(1) {} 
    Quat(char c_) { this->c = c_; }
    Quat operator = (char c_) { this->c = c_; return *this; }
    inline const Quat& operator *= (const Quat &x);
};

ostream &operator << (ostream &os, Quat x) { return os << x.c;}
istream &operator >> (istream &is, Quat &x) { is >> x; return is; }
bool operator == (Quat x, Quat y) { return x.c == y.c; }
inline Quat operator * (Quat x, Quat y) { 
    int sign = 1;
    if (x.c < 0) sign *= -1, x.c = -x.c;
    if (y.c < 0) sign *= -1, y.c = -y.c;
    
    if (x.c == 1) return Quat(sign * y.c);
    if (x.c == 2) {
        if (y.c == 1) return Quat(sign * 2);
        if (y.c == 2) return Quat(sign * -1);
        if (y.c == 3) return Quat(sign * 4);
        if (y.c == 4) return Quat(sign * -3);
    }
    if (x.c == 3) {
        if (y.c == 1) return Quat(sign * 3);
        if (y.c == 2) return Quat(sign * -4);
        if (y.c == 3) return Quat(sign * -1);
        if (y.c == 4) return Quat(sign * 2);
    }
    if (x.c == 4) {
        if (y.c == 1) return Quat(sign * 4);
        if (y.c == 2) return Quat(sign * 3);
        if (y.c == 3) return Quat(sign * -2);
        if (y.c == 4) return Quat(sign * -1);
    }
    return Quat(1);
}
inline const Quat& Quat::operator *= (const Quat &x) {*this = *this * x; return *this;}


long long L, X;
string str;

bool solve() {
    vector<Quat> vec(L);
    for (long long i = 0; i < L; ++i) {
        if (str[i] == 'i') vec[i] = 2;
        if (str[i] == 'j') vec[i] = 3;
        if (str[i] == 'k') vec[i] = 4;
    }
    
    //COUT(vec);
    
    Quat all = 1, tall = 1;
    for (long long i = 0; i < vec.size(); ++i) {
        tall *= vec[i];
    }
    for (long long i = 0; i < (X%4); ++i) {
        all *= tall;
    }
    
    //COUT(all);
    
    if (all.c != -1) return false;
    
    int stage = 0;
    Quat tmp = 1;
    for (long long i = 0; i < min(100LL, X); ++i) {
        for (int j = 0; j < L; ++j) {
            if (stage == 0 && tmp.c == 2) {
                stage = 1;
                //COUT( pint(i,j) );
            }
            if (stage == 1 && tmp.c == 4) {
                stage = 2;
                //COUT( pint(i,j) );
            }
            tmp *= vec[j];
        }
    }
    
    if (stage == 2) return true;
    else return false;
}

int main() {
    freopen( "/Users/macuser/Dropbox/Contest/C-large.in", "r", stdin );
    freopen( "/Users/macuser/Dropbox/Contest/C-large.out", "w", stdout );
    
    int T;
    scanf("%d", &T);
    for (int XXX = 0; XXX < T; ++XXX) {
        cin >> L >> X >> str;
        printf("Case #%d: ", XXX+1);
        if (solve()) puts("YES");
        else puts("NO");
    }
    
    
    return 0;
}




