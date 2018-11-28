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

char arr[N];

int main(){
    int t ; si(t);
    REP(j,1,t){
        int p,q;
        p = q = 1005;
        string s; cin>>s;
        int k = s.length();
        arr[p] = s[0];
        REP(i,1,k-1){
            if(s[i] >= arr[p]){
                arr[--p] = s[i];
            }
            else arr[++q] = s[i];
        }
        printf("Case #%d: ",j );
        REP(i,p,q) printf("%c",arr[i]);
        printf("\n");
    }
    return 0;   
}
