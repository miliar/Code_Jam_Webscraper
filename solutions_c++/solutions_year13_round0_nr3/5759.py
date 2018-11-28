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

bool pal[1007];
bool f(int n){
    string s = toString(n);
    int len =  s.length();
    rep(i,len) if(s[i]!=s[len-i-1]) return 0;
    return 1;
}
int main()
{
    freopen("in","r",stdin);
    freopen("out","w",stdout);

    for(int i = 1; i*i<=1000; i++)
    {
        if(f(i)&&f(i*i)) pal[i*i]=1;
    }

    int t;
    cin>>t;

    rep(cs,t) {
        int x,y,cnt=0;
        cin>>x>>y;
        repi(i,x,y) if(pal[i]) cnt++;
        cout<<"Case #"<<cs+1<<": "<<cnt<<endl;
    }


    return 0;
}
