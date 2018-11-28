#include    <bits/stdc++.h>

#define     M_PI            3.14159265358979323846
#define     mod             1000000007
#define     inf             1000000000000000000
#define     mp              make_pair
#define     pb              push_back
#define     F               first
#define     S               second
#define     ll              long long
#define     pii             pair<int,int>
#define     pli             pair<ll,int>
#define     pil             pair<int,ll>
#define     pll             pair<ll,ll>
#define     si(t)           scanf("%d",&t)
#define     sii(m,n)        scanf("%d %d",&m,&n);
#define     sl(t)           scanf("%lld",&t)
#define     rep(i,n)        for(int i=0;i<n;i++)
#define     REP(i,a,b)      for(int i=a;i<=b;i++)
#define     RREP(i,a,b)     for(int i=a;i>=b;i--)
#define     N               100050

using namespace std;

string s;

int fun(int a,int k){
    if(a < 0) return 0;
    int p;
    if(s[a] == '+') p = 1;
    else p = 0;
    int ans;
    if(p == k) ans = fun(a-1,p);
    else ans = fun(a-1,p)+1;
    return ans;
}

int main(){
    int t;
    si(t);
    REP(j,1,t){
        cin>>s;
        int n = s.length();
        int ans = fun(n-1,1);
        printf("Case #%d: %d\n",j,ans);
    }
    return 0;
}