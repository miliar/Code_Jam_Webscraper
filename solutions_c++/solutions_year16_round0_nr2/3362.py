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

    bool ar[101];

    FOR(ii,tc)
    {
        string str;
        int ans = 0;

        cin >> str;
        int lgt = str.length();
        int newlgt = lgt;

        //cout << newlgt << endl;

        //false = +
        reset(ar,0);
        for(int i=0;i<lgt;i++)
        {
            if(str[i]=='-')ar[i] = true;
        }

        while(true) {
            for(int i=(lgt-1);i>=0;i--) {
                if(ar[i]) {newlgt = i;break;}
            }

            if(newlgt == lgt) break;
            if(!ar[0]) {
            //Flip First
                int midswap = 0;
                while(!ar[midswap]) midswap++;
                for(int i=0;i<midswap;i++) ar[i] = true;
                ans++;
            }

            //perform swap
            bool temp[newlgt+1];
            for(int i=0;i<(newlgt+1);i++)
            {
                temp[i] = !ar[newlgt - i];
            }
            for(int i=0;i<(newlgt+1);i++)
            {
                ar[i] = temp[i];
            }
            lgt = newlgt;
            ans++;
        }

        cout << "Case #" << ii+1 << ": " << ans << endl;
    }


    return 0;
}
