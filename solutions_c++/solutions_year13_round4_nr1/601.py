#include <iostream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cctype>
#include <sstream>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <functional>
#include <numeric>
#include <utility>
#include <cstdlib>
#include <cstring>
#include <ctime>
using namespace std;

const int INF = 0X3F3F3F3F;
const double PI = acos(-1.0); //3.1415926535897932384626433832795;
const double EPS = 1e-11;
const int days[] = {31,28,31,30,31,30,31,31,30,31,30,31};
const int dx[] = {-1,0,1,0},dy[] = {0,1,0,-1}; //4 direction

#define PB push_back
#define MP make_pair
#define SZ size()
#define V vector
#define A first
#define B second
#define FOR(i,s,e) for(int i=(s);i<=(int)(e);++i)
#define FORD(i,s,e) for(int i=(s);i>=(int)(e);--i)
#define REP(i,n) for(int i=0;i<(int)(n);++i)
#define REPD(i,n) for(int i=(n)-1;i>=0;--i)
#define FIT(it,x) for(typeof((x).begin()) it = (x).begin();it != (x).end();it++)
#define FITD(it,x) for(typeof((x).rbegin()) it = (x).rbegin();it != (x).rend();it++)
#define ALL(x) (x).begin(),(x).end()
#define CLR(x) memset((x),0,sizeof(x))
#define MEM(a,b) memset((a),b,sizeof(a));
#define EXIST(a,b) (find(all(a),b)!=a.end())
#define DEBUG(x) cerr << #x << ":" << x << '@' << endl
#define PRV(v) REP(vi,v.size()) cout << v[vi] << ' ';cout << endl

inline int sgn(double x) { return x < -EPS ? -1 : x > EPS ? 1 : 0; }
inline string tolower(string s){ REP(i,s.SZ) s[i] = tolower(s[i]); return s; }
inline string toupper(string s){ REP(i,s.SZ) s[i] = toupper(s[i]); return s; }
template<class T> inline T sqr(const T& x) { return x * x; }
template<class T> inline int toint(const T& x){ stringstream ss; ss << x; int r; ss >> r; return r; } 
template<class T> inline int todouble(const T& x){ stringstream ss; ss << x; double r; ss >> r; return r; } 
template<class T> inline string tostr(const T& x) { ostringstream os(""); os << x; return os.str(); }
template<class T> void stov(string s,vector<T> &vi){vi.clear();istringstream sin(s);for(T v;sin>>v;vi.push_bakc(v));}//NOTES:stov(
template<class T> void vtos(vector<T> vi,string &s){ostringstream sout;for (int i=0;i<vi.size();i++){if(i>0)sout<<' ';sout<<vi[i];}s=sout.str();}

typedef long long LL;
typedef double DB;
typedef stringstream SS;
typedef set< int > SI;
typedef pair< int, int > PII;
typedef vector< int > VI;
typedef vector< VI > VVI;
typedef vector< string > VS;
typedef map< string, int > MSI;
typedef map< int, int > MII;
bool is(char c) {
    return c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u';
}
const int MAXN = 111;
const int MOD = 1000002013;
struct data {
    int o, e, p;
    friend bool operator <(const data& a, const data& b) {
        return a.e == b.e ? a.o < b.o : a.e < b.e;
    }
} d[MAXN];

struct data2 {
    int id, p;
};

int dp[MAXN];
int n, m;
LL calc(int a, int b) {
    return (LL)(n + (n - (b - a - 1))) * (b - a) / 2;
}

long long diff(int a, int b, int c, int d) {
    if (a > c) {
        swap(a, c);
        swap(b, d);
    }
    if (d < b || c > b) return -1;
    return calc(a, b) + calc(c, d) - calc(a, d) - calc(c, b);
}
bool vis[11111];
int main() {
    //freopen("A.in", "r", stdin);
    //freopen("A-large-practice.out", "w", stdout);
    int cas;
    scanf("%d", &cas);
    getchar();
    string s;
    for (int T = 1; T <= cas; T++) {
        scanf("%d %d", &n, &m);
        long long origans = 0;
        for (int i = 0; i < m; i++) {
            scanf("%d %d %d", &d[i].o, &d[i].e, &d[i].p);
            //d[i].o = rand() % n + 1;
            //d[i].e = rand() % (n - d[i].o + 1) + d[i].o;
            //d[i].p = rand() % 100;
            long long tmp = 0;
            for (int j = d[i].o; j < d[i].e; j++) {
                tmp += n - (j - d[i].o);
            }
            origans += tmp * d[i].p;
        }
        long long ans = 0;
        sort(d, d + m);
        //priority_queue<pair<int, LL> > p;
        vector<data> v;
        for (int i = 0; i < m; i++) {
            data t = d[i];
            t.p = 1;
            for (int j = 0; j < d[i].p; j++) {
                v.push_back(t);
            }
        }
        vector<data> vv;
        bool flag = true;
        vector<data> last;
        while (flag) {
            flag = false;
            memset(vis, 0, sizeof(vis));
            for (int i = 0; i < v.size(); i++) {
                vv.clear();
                int good = 0;
                int p = -1;
                for (int j = 0; j < v.size(); j++) {
                    if (i == j) continue;
                    long long tt = diff(v[i].o, v[i].e, v[j].o, v[j].e);
                    if (tt > good) {
                        good = tt;
                        p = j;
                    }
                }
                if (p == -1) {
                    continue;
                }
                flag = true;
                for (int j = 0; j < v.size(); j++) {
                    if (j == i || j == p || vis[j]) continue;
                    vv.push_back(v[j]);
                }
                data a = v[i];
                data b = v[p];
                swap(a.e, b.e);
                vv.push_back(a);
                vv.push_back(b);
                v = vv;
                break;
            }
        }
        for (int i = 0; i < last.size(); i++) {
            v.push_back(last[i]);
        }
        for (int i = 0; i < v.size(); i++) {
            ans += calc(v[i].o, v[i].e);
        }
        printf("Case #%d: ", T);
        printf("%lld\n", origans - ans);
    }
    return 0;
}
