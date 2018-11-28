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
#define sc(x) scanf("%d",&x)

int main(void){
    #ifdef ccsnoopy
        freopen("C:/Users/SONY/Desktop/A-large.in","r",stdin);
        freopen("C:/Users/SONY/Desktop/out.txt","w",stdout);
    #endif
    //to compile: g++ -o foo filename.cpp -lm -Dccsnoopy for debug.
    int tc;
    sc(tc);
    char str[1020];
    int casecounter = 1;
    while(tc--){
        int n;
        sc(n);
        scanf("%s",str);
        int len = strlen(str);
        ll tot = 0;
        ll cur = str[0]-'0';
        REP(i,1,len){
            int angka = str[i]-'0';
            if(i>cur && angka){
                tot+=i-cur;
                cur+=i-cur;
            }
            cur += angka;
            //cout<<tot<<" "<<cur<<endl;
        }



        printf("Case #%d: ",casecounter++);
        cout<<tot<<endl;
    }

    return 0;
}



