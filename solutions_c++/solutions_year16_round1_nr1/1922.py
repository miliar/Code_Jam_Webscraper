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
    freopen("C:/Users/SONY/Desktop/A-large.in","r",stdin);
    freopen("C:/Users/SONY/Desktop/out.txt","w",stdout);

    int tc, ctr = 1;

    sc(tc);
    while(tc--){
        string x;
        cin>>x;
        deque<char> d;
        d.push_back(x.at(0));
        int len = x.length();
        REP(i,1,len){
            char z = d.front();
            if(z <= x.at(i)){
                d.push_front(x.at(i));
            }else{
                d.push_back(x.at(i));
            }
        }
        printf("Case #%d: ", ctr++);
        while(!d.empty()){
            cout<<d.front();
            d.pop_front();
        }
        cout<<endl;
    }





    return 0;
}



