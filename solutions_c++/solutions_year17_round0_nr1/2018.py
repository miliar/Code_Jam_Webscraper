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
    freopen("D:/Code/A-large.in","r",stdin);
    freopen("D:/Code/out.txt","w",stdout);

    int tc;
    sci(tc);

    FOR(x,tc)
    {
        string pCake;
        int flip, ans;
        bool impossible = false;
        cin >> pCake;
        cin >> flip;
        ans = 0;

        for(int i=0;i<pCake.length();i++){
            if(pCake[i]=='-'){
                if(i+flip<=pCake.length()) {
                    ans++;
                    for(int ii=0;ii<flip;ii++){
                        if(pCake[i+ii]=='-'){
                            pCake[i+ii] = '+';
                        } else {
                            pCake[i+ii] = '-';
                        }
                    }
                } else {
                    impossible = true;
                }
            }
        }

        if(impossible) {
            cout << "Case #" << x+1 << ": IMPOSSIBLE" << endl;
        } else {
            cout << "Case #" << x+1 << ": " << ans << endl;
        }

    }


    return 0;
}
