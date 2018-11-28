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

    FOR(i,tc)
    {
        string base;
        cin >> base;
        string result = "";
        result = result + base.at(0);
        REP(ii,1,base.length()) {
            string re1 = result + base.at(ii);
            string re2 = base.at(ii) + result;
            result = re1.compare(re2) > 0 ? re1 : re2;
        }

        cout << "Case #" << i+1 << ": " << result << endl;
    }


    return 0;
}
