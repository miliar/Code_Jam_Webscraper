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
    freopen("D:/Code/B-large.in","r",stdin);
    freopen("D:/Code/out.txt","w",stdout);

    int tc;
    sci(tc);
    int ar[55][3];
    int raw[110][55];
    int ans;
    bool ansOrient;
    bool used[110];

    FOR(i,tc)
    {
        int n;
        sci(n);
        reset(ar,0);
        reset(raw,0);
        reset(used,0);

        FOR(ii,(n*2)-1) {
            FOR(iii,n) {
                sci(raw[ii][iii]);
            }
        }

        FOR(ii,n) {
            int minValue = 2501;
            int minPos1 = -1;
            int minPos2 = -1;

            FOR(iii,(n*2)-1) {
                if(used[iii]) continue;

                if(raw[iii][ii] < minValue) {
                    minValue = raw[iii][ii];
                    minPos1 = iii;
                    minPos2 = -1;
                } else if(raw[iii][ii] == minValue) {

                    minPos2 = iii;
                }
            }

            ar[ii][0] = minPos1;
            ar[ii][1] = minPos2;
            used[minPos1] = true;

            //cout << ii << " " << minPos1 << " " << minPos2 << endl;
            if(minPos2 < 0){
                ans = ii;
                ar[ii][1] = minPos1;
            } else {
                used[minPos2] = true;
            }
        }

        cout << "Case #" << i+1 << ":";
        FOR(ii,n) {
                //cout << ar[ii][0] << " " << ar[ii][1] << endl;
                if(raw[ar[ans][0]][ii]==raw[ar[ii][0]][ans])
                {
                    cout << " " << raw[ar[ii][1]][ans];
                } else {
                    cout << " " << raw[ar[ii][0]][ans];
                }

                //cout << " " << ar[ans][ii];
        }

        cout << endl;
    }


    return 0;
}
