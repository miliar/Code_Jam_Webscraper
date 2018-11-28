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



int X, R, C;

bool solve() {
    cin >> X >> R >> C;
    
    if (X == 1) return true;
    else if (X == 2) {
        if ( (R*C) % 2 == 0 ) return true;
        return false;
    }
    else if (X == 3) {
        if (C % 3 == 0) swap(R, C);
        
        if (R % 3 == 0 && C >= 2) return true;
        return false;
    }
    else if (X == 4) {
        if (C % 2 == 0) swap(R, C);
        
        if (R % 4 == 0 && C >= 3) return true;
        if (R % 2 == 0 && C % 2 == 0 && R >= 4 && C >= 4) return true;
        return false;
    }
    else if (X == 5) {
        if (C % 5 == 0) swap(R, C);
        
        if (R == 5 && C >= 4) return true;
        if (R % 5 == 0 && R >= 10 && C >= 3) return true;
        return false;
    }
    else if (X == 6) {
        if (C % 3 == 0) swap(R, C);
        
        if (R % 6 == 0 && C >= 4) return true;
        if (R % 3 == 0 && C % 2 == 0 && R >= 6 && C >= 4) return true;
        return false;
    }
    else return false;
}

int main() {
    freopen( "/Users/macuser/Dropbox/Contest/D-large.in", "r", stdin );
    freopen( "/Users/macuser/Dropbox/Contest/D-large.out", "w", stdout );
    
    int T;
    scanf("%d", &T);
    for (int XXX = 0; XXX < T; ++XXX) {
        printf("Case #%d: ", XXX+1);
        if (solve()) cout << "GABRIEL" << endl;
        else cout << "RICHARD" << endl;
    }
    
    
    return 0;
}




