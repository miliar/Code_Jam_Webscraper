#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <iostream>
#include <list>
#include <ctime>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>
using namespace std;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef map<string,int> msi;
typedef map<int,int>mii;
typedef long long ll;
#define INF 2147483647
#define sqr(x) ((x)*(x))
#define pi acos(-1.0)
#define all(x) x.begin(),x.end()
#define pb push_back
#define gcd(a,b) __gcd(a,b)
#define lcm(a,b) ((a)*((b)/gcd(a,b)))
#define one_bits(a) __builtin_popcount(a)
#define MEM(a,b) memset(a,b,sizeof(a))
#define rep(i,n) for(int i=0;i<n;i++)
#define repi(i,m,n) for(int i=m;i<=n;i++)
#define repr(i,m,n) for(int i=m;i>=n;i--)
int dx[]={-1,0,1,0,-1,1,1,-1},dy[]={0,-1,0,1,-1,-1,1,1};
int kx[]={2,1,-1,-2,-2,-1,1,2},ky[]={1,2,2,1,-1,-2,-2,-1};
int POW(int b,int p){int r=1;repi(i,1,p)r*=b;return r;}
string toString(int n){stringstream ss;ss<<n;return ss.str();}
int toInt(string s){int r=0;istringstream sin(s);sin>>r;return r;}
bool isVowel(char ch){ch=tolower(ch);return ch=='a'||ch=='e'||ch=='i'||ch=='o'||ch=='u';}
int bigmod(ll B,ll P,ll M){ll R=1;while(P>0){if(P%2){R=(R*B)%M;}P/=2;B=(B*B)%M;}return (int)R;}
ll nCr(double n,double r){double ans=1;if(r>n-r)r=n-r;repi(i,1,r){ans*=(n-i+1);ans/=i;}return (ll)ans;}
//void sieve(int n){MEM(prime,1);for(int i=2;i*i<=n;i++)for(int j=i*i;j<=n;j+=i)prime[j]=0;}
char g[7][7];
int main()
{
    freopen("in","r",stdin);
    freopen("out","w",stdout);

    int t;
    cin>>t;

    rep(cs,t)
    {
        bool full=1;
        rep(i,4){
            cin>>g[i];
            rep(j,4) if(g[i][j]=='.')full=0;
        }

        bool xwin=0, owin=0;
        int T,X,O;

        rep(i,4) {
            T=0,X=0,O=0;
            rep(j,4) {
                if(g[i][j]=='T') T++;
                else if(g[i][j]=='O') O++;
                else if(g[i][j]=='X') X++;
            }
            if(X==4||(X==3&&T==1)) xwin = 1;
            if(O==4||(O==3&&T==1)) owin = 1;

            T=0,X=0,O=0;
            rep(j,4) {
                if(g[j][i]=='T') T++;
                else if(g[j][i]=='O') O++;
                else if(g[j][i]=='X') X++;
            }
            if(X==4||(X==3&&T==1)) xwin = 1;
            if(O==4||(O==3&&T==1)) owin = 1;
        }

        T=0,X=0,O=0;
        rep(i,4) {
            if(g[i][i]=='T') T++;
            else if(g[i][i]=='O') O++;
            else if(g[i][i]=='X') X++;
        }
        if(X==4||(X==3&&T==1)) xwin = 1;
        if(O==4||(O==3&&T==1)) owin = 1;


        T=0,X=0,O=0;
        rep(i,4) {
            if(g[i][3-i]=='T') T++;
            else if(g[i][3-i]=='O') O++;
            else if(g[i][3-i]=='X') X++;
        }
        if(X==4||(X==3&&T==1)) xwin = 1;
        if(O==4||(O==3&&T==1)) owin = 1;


        cout<<"Case #"<<cs+1<<": ";
        if(xwin) cout<<"X won";
        else if(owin) cout<<"O won";
        else if(!full) cout<<"Game has not completed";
        else cout<<"Draw";
        cout<<endl;
    }

    return 0;
}
