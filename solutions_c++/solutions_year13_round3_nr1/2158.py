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

int sum(int n, int a){
    return (n*(2*a+n-1))/2;
}

int main()
{
    //freopen("ai.txt","r",stdin);
    //freopen("ao.txt","w",stdout);

    int t;
    cin>>t;

    rep(cs,t) {

        cout<<"Case #"<<cs+1<<": ";

        string str;
        int n;

        cin>>str>>n;
        int cnt=0,ans=0, last=-1;
        int len = str.length();
        for(int i = 0; i<len;i++)
        {
            if(!isVowel(str[i])) {
                cnt++;
            }
            else{
                if(cnt==n) {
                    if(last!=-1)ans += (len-i+1)*((i-cnt)-last+n-1);
                    else ans += ((len-i+1)*(i-cnt+1));
                    last = i-1;
                }
                else if(cnt>n){
                    if(last!=-1)ans += (len-i+1+(cnt-n))*((i-cnt)-last+n-1);
                    else ans += ((len-i+1+(cnt-n))*(i-cnt+1));
               //     cout<<len-i+1+(cnt-n)<<' '<<((i-cnt)-last+n-1)<<endl;
                    ans += sum(cnt-n,len-i+1);
                    last = i-1;
                }
               // cout<<ans<<endl;
                cnt=0;
            }
        }
        if(cnt>=n) {
            if(cnt==n){
                if(last!=-1)ans += ((len-cnt)-last+n-1);
                else ans += (len-cnt+1);
            }
            else if(cnt>n){
                if(last!=-1)ans += ((len-cnt)-last+n-1)*(cnt-n+1);
                else ans += (len-cnt+1)*(cnt-n+1);
                ans += sum(cnt-n,1);
            }
        }

        cout<<ans<<endl;
    }

    return 0;
}


// 1 aabbbaabbbaabbb 2
