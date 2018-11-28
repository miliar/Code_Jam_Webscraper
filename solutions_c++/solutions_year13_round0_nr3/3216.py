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
inline ll sq(ll x) {return x * x;}
inline bool check_p(string s) {
    int l = len(s);
    rep(i,l/2) if (s[i] != s[l - 1 - i]) return false;
    return true;
}
int main() {
    int n, a, b;
    cin >> n;
    rep(z,n) {
        cin >> a >> b;
        if (a == sq((ll)sqrt(a))) a = (int)sqrt(a);
        else a = (int)sqrt(a) + 1;
        if (b == sq((ll)sqrt(b))) b = (int)sqrt(b);
        else b = (int)sqrt(b);
        int res = 0;
        FOR(i,a,b+1) {
            if (check_p(Str(i)) && check_p(Str(i*i))) ++res;
        }
        printf("Case #%d: %d\n", z+1, res);
    }
	return 0;
}