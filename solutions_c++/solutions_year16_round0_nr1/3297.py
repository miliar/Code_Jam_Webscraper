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

    bool ar[11];
    bool complete;

    FOR(i,tc)
    {
        int start;
        sci(start);

        if(start==0)
        {
            cout << "Case #" << i+1 << ": INSOMNIA"<< endl;
            continue;
        }

        reset(ar,0);
        complete = false;
        ll ans = 0;

        while(!complete)
        {
            complete = true;
            ans += start;
            int calc = ans;

            while(calc>0) {
                int num = calc%10;
                ar[num] = true;
                calc /= 10;
            }

            for(int i=0;i<10;i++) complete = complete && ar[i];
        }



        cout << "Case #" << i+1 << ": " << ans << endl;
    }


    return 0;
}
