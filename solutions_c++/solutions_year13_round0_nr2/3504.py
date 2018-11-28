#include <iostream> 
#include <sstream> 
#include <cstring>
#include <string> 
#include <vector> 
#include <queue> 
#include <stack>
#include <deque> 
#include <set> 
#include <map> 
#include <algorithm> 
#include <utility> 
#include <functional> 
#include <cstdio> 
#include <cstdlib> 
#include <cmath> 
#include <ctime> 

using namespace std; 

const double pi = acos(-1.); 
typedef long long ll;
typedef pair<int,int> pii;
template<typename T> inline string Str(const T &a) {stringstream s;s<<a;return s.str();} 
template<typename T> inline int Int(const T &a) {stringstream s;s<<a;int r;s>>r;return r;} 
template<typename T> inline ll Long(const T &a) {stringstream s;s<<a;ll r;s>>r;return r;} 
template<typename T> inline double Double(const T &a) {stringstream s;s<<a;double r;s>>r;return r;}  

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define rep(i,a) FOR(i,0,a)
#define all(a) a.begin(),a.end()
#define clr(a) memset(a, 0, sizeof(a))
#define debug(a) cerr << #a << ":" << (a) << endl;
#define len(a) ((int) a.size())
#define foreach(itr,c) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();++itr) 
#define X first
#define Y second
#define PB push_back
#define MP make_pair
int G[100][100];
int x, y, best;
int main() {
    int T, n, m;
    cin >> T;
    rep(z,T) {
        string res = "YES";
        cin >> n >> m;
        rep(i,n) rep(j,m) cin >> G[i][j];
        rep(t,n+m) {
            best = 1000;
            rep(i,n) rep(j,m) {
                if (G[i][j] == -1) continue;
                if (best > G[i][j]) {
                    best = G[i][j];
                    x = i, y = j;
                }
            }
            bool flag = true;
            rep(i,n) {
                if (G[i][y] != -1 && G[i][y] != best) {
                    flag = false; break;
                }
            }
            if (flag) rep(i,n) G[i][y] = -1;
            else {
                flag = true;
                rep(i,m) {
                    if (G[x][i] != -1 && G[x][i] != best) {
                        flag = false; break;
                    }
                }
                if (flag) rep(i,m) G[x][i] = -1;
                else {res = "NO"; goto LOOP;}
            }
        }
LOOP:   printf("Case #%d: %s\n", z+1, res.c_str());
    }
	return 0;
}