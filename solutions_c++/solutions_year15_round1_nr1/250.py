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




int N;
long long m[2100];

pll solve() {
    cin >> N;
    for (int i = 0; i < N; ++i) cin >> m[i];
    
    long long fi = 0, se = 0, mr = 0;
    for (int i = 0; i < N-1; ++i) {
        if (m[i] > m[i+1]) {
            fi += m[i] - m[i+1];
            chmax(mr, m[i] - m[i+1]);
        }
    }
    
    for (int i = 0; i < N-1; ++i) {
        se += min(m[i], mr);
    }
    
    return make_pair(fi, se);
}

int main() {
    freopen( "/Users/macuser/Dropbox/Contest/A-large.in", "r", stdin );
    freopen( "/Users/macuser/Dropbox/Contest/A-large.out", "w", stdout );
    
    int T;
    scanf("%d", &T);
    for (int XXX = 0; XXX < T; ++XXX) {
        printf("Case #%d: ", XXX+1);
        
        pll p = solve();
        cout << p.first << " " << p.second << endl;
    }
    
    
    return 0;
}




