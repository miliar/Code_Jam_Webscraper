#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef long long LL;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;

#ifdef DEBUG
    #define cek(x) cout<<x
#else
    #define cek(x) if(false){}
#endif // DEBUG

#define fi first
#define se second
#define INF 1000000000
#define INFLL 1000000000000000000LL
#define EPS 1e-9
#define PI acos(-1.0)
#define pb push_back
#define TC() while(tc--)
#define FOR(i,n) for(int i=0;i<n;i++)
#define FORN(i,n) for(int i=0;i<=n;i++)
#define REP(i,a,b) for(int i=a;i<b;i++)
#define REPN(i,a,b) for(int i=a;i<=b;i++)
#define reset(a,b) memset(a,b,sizeof(a))
#define sci(x) scanf("%d",&x)
#define scs(x) scanf("%s",&x)

int main(void){
    freopen("D:/Code/D-small-attempt0.in","r",stdin);
    freopen("D:/Code/out.txt","w",stdout);

    int tc;
    sci(tc);

    FOR(i,tc)
    {
        string ans = "";
        int k,c,s;
        sci(k);
        sci(c);
        sci(s);

        cout << "Case #" << i+1 << ":";

        if(c==1) {
            if(s<k) {
                cout << " IMPOSSIBLE" << endl;
            } else {
                for(int ii=0;ii<k;ii++){
                    cout<<" "<<ii+1;
                }
                cout<<endl;
            }
        } else {
            if((s*2)<k) {
                cout << " IMPOSSIBLE" << endl;
            } else {
                ll kpow = k;
                for(int ii=1;ii<c-1;ii++) {
                    kpow *= k;
                }
                for(int ii=0;ii<((k+1)/2);ii++) {
                    ll ansval = ((ii*2*kpow)+(ii+1)*2);
                    if((ii+1)*2 > k) ansval--;
                    cout << " " << ansval;
                }
                cout << endl;
            }
        }
    }


    return 0;
}
