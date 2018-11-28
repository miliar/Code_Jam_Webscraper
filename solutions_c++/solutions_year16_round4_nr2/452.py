
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
double ans[205][205];
double inp[205];
int main(){
    freopen("inp11.txt","r",stdin);
    freopen("output11.txt","w",stdout);
    int t;
    cin >> t;
    int idx=1;
    while(t--){
       int n,k;
       cin >> n >> k;
       for(int i=1;i<=n;++i)
        cin >> inp[i];
       sort(inp+1,inp+n+1);
       vector<double> vec;
       if(inp[n]>=0.5){
       for(int i=1;i<=k/2;++i)
        vec.push_back(inp[i]);
       for(int i=n;i>n-k/2;--i){
        vec.push_back(inp[i]);
       }
       }
       else{
            for(int i=n;i>n-k;--i)
                vec.push_back(inp[i]);
 
       }
 
 
       for(int i=0;i<=k;++i)
            for(int j=0;j<=k;++j)
                ans[i][j]=0;
       ans[0][0]=1.0;
       for(int i=1;i<=k;++i){
            double temp=vec[i-1];
            for(int j=0;j<min(i,k/2+1);++j){
                ans[i][j+1]+=temp*ans[i-1][j];
                ans[i][j]+=(1.0-temp)*ans[i-1][j];
            }
       }
 
      printf("Case #%d: %.12f\n",idx,ans[k][k/2]);
      ++idx;
 
    }
 
    return 0;
}
