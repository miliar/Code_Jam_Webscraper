#include <bits/stdc++.h>

using namespace std;

#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define rep(i,n) for(int i = 0;i < (int) n ; ++i)
#define repd(i,n) for(int i= (int) n; i>=0 ; --i)
#define For(i,a,b) for(int i= (int) a; i<= (int) b; ++i)
#define Ford(i,a,b) for(int i = (int) b; i>= int (a); --i)

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;

#define mod 20122007

bool compare(ii x,ii y){
    if (x.fi<y.fi) return true;
    else
    if( x.fi==y.fi && x.se>y.se)
        return true;
    else
        return false;
}

ll gcd(ll a,ll b){
    return (b==0) ? a:gcd(b,a%b);
}

ll lcm(ll a, ll b){
    return (a*b)/gcd(a,b);
}

string nhan(string s, int k){
    string x;

}

char s[1234];

int main()
{
    //freopen("A-large.in","r",stdin);
    //freopen("A-large.out","w",stdout);
    int test;
    cin>>test;
    int tt=0;
    while (test--){
        ++tt;
        int n,sd=0,res=0;
        scanf("%d %s",&n,s);
        for(int i=0;i<=n;++i)
            {
                if (sd>=i)
                {
                    sd+=s[i]-'0';
                }
                else
                {
                    res+=i-sd;
                    sd+=(i-sd)+(s[i]-'0');
                }
            }
        printf("Case #%d: %d\n",tt,res);
    }
    return 0;
}
