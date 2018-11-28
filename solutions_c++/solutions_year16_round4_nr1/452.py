
#include<bits/stdc++.h>
using namespace std;
//long long arrr[1000005];
// inhortcuts for "common" data types in contests
typedef long long li;
typedef vector<long long> vi;
typedef pair<long long, long long> ii;
typedef vector<ii> vii;
typedef set<long long> si;
typedef map<string, long long> msi;
#define rep(i, a, b) for(li i=a; i<b; i++)
#define ALL(c) c.begin(), c.end()
#define rloop(i, a, b) for(long long i=b-1; i>=a; i--)
#define loopinc(i, a, b, inc) for(long long i=a; i<b; i+=inc)
/*Use like- 
rep(i,0,n - 1)
*/

template<class T> T pwr(T b, T p){T r=1,x=b;while(p){if(p&1)r*=x;x*=x;p=(p>>1);}return r;}
 
#define     inf             (0x7f7f7f7f)
#define     inf1             -(0x7f7f7f7f)
const long long MAXN = 2e2+5;
#define MOD 1000000007

li modPow(li a, li x, li p) {
    //calculates a^x mod p in logarithmic time.
    li ansrt = 1;
    while(x > 0) {
        if( x % 2 != 0) {
            ansrt = (ansrt * a) % p;
        }
        a = (a * a) % p;
        x /= 2;
    }

    return ansrt;
}
class CompareDist
{
public:
    bool operator()(pair<long long,long long> n1,pair<long long,long long> n2) {
        return n1.second>n2.second;
    }
};
class CompareDist1
{
public:
    bool operator()(pair<long long,long long> n1,pair<long long,long long> n2) {
        return n1.second<n2.second;
    }
};

int P, R, S;

string ans;
string x[3];

void Solve1(int n,int p,int r,int s){
    if(n == 0){
        if(p)printf("%s\n", x[0].c_str());
        if(r)printf("%s\n", x[1].c_str());
        if(s)printf("%s\n", x[2].c_str());
        return;
    }
    
    string t[3];
    if(x[0] > x[1])t[0] = x[1] + x[0];
    else t[0] = x[0] + x[1];
    if(x[1] > x[2])t[1] = x[2] + x[1];
    else t[1] = x[1] + x[2];
    if(x[2] > x[0])t[2] = x[0] + x[2];
    else t[2] = x[2] + x[0];
    for(int i=0;i<3;i++)x[i] = t[i];
    int tp = (r+p-s)/2;
    int ts = (s+p-r)/2;
    int tr = (r+s-p)/2;
    Solve1(n-1, tp, tr, ts);
}

void solve(int tc){
    printf("Case #%d: ", tc);
    int n, r, p, s;
    scanf("%d%d%d%d", &n, &r, &p, &s);
    P = p; R = r; S = s;
    for(int i=1;i<=n;i++){
        int tp = (r+p-s)/2;
        int ts = (s+p-r)/2;
        int tr = (r+s-p)/2;
        if(tp < 0 || ts < 0 || tr < 0){
            printf("IMPOSSIBLE\n");
            return;
        }
        p = tp, r = tr, s = ts;
    }
    x[0] = "P";
    x[1] = "R";
    x[2] = "S";
    Solve1(n, P, R, S);
}

int main() {
    freopen("inp11.txt","r",stdin);
    freopen("output11.txt","w",stdout);
    int Tc; scanf("%d", &Tc);
    for(int tc=1;tc<=Tc;tc++){
        solve(tc);
    }
    return 0;
}