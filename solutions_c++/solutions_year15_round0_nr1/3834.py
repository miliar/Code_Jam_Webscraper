#include<bits/stdc++.h>
#define assn(n,a,b) assert(n<=b && n>=a)
using namespace std;
#define pb push_back
#define mp make_pair
#define clr(x) x.clear()
#define sz(x) ((int)(x).size())
#define F first
#define S second
#define REP(i,a,b) for(i=a;i<b;i++)
#define rep(i,b) for(i=0;i<b;i++)
#define rep1(i,b) for(i=1;i<=b;i++)
#define pdn(n) printf("%d\n",n)
#define sl(n) scanf("%lld",&n)
#define sd(n) scanf("%d",&n)
#define pn printf("\n")
typedef pair<int,int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long LL;
#define MOD 1000000007
LL mpow(LL a, LL n) 
{LL ret=1;LL b=a;while(n) {if(n&1) 
    ret=(ret*b)%MOD;b=(b*b)%MOD;n>>=1;}
return (LL)ret;}
int main()
{
    int t,p;
    sd(t);
    p=t;
    while(t--){
        string s;
        int n;
        sd(n); cin >> s;
        n++;
        int cur=0,ans=0;
        for(int i=0; i<n; i++){
            if(s[i]-'0' and cur<i)
                ans += i-cur, cur += i-cur;
            cur += s[i]-'0';
        }
        printf("Case #%d: %d\n",p-t,ans);
    }
    return 0;
}
