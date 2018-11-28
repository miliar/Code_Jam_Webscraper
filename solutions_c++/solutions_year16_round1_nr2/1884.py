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

typedef struct{
    int arr[55];
    bool used;
}x_t;

int main(void){
    freopen("C:/Users/SONY/Desktop/B-large.in","r",stdin);
    freopen("C:/Users/SONY/Desktop/out.txt","w",stdout);

    int tc, ctr = 1;

    sc(tc);
    int n;
    while(tc--){
        sc(n);
        x_t xx[2*n];
        FOR(i,2*n-1){
            FOR(j,n){
                sc(xx[i].arr[j]);
            }
            xx[i].used = false;
        }
        vector<ii> vz;
        int arr[55];
        int punya [55];
        int culprit = -1;
        FOR(i,n){
            int smallest = INF, ctr = 0;
            vector<int> v;
            FOR(j,2*n-1){
                if(xx[j].arr[i] < smallest && !xx[j].used){
                    smallest = xx[j].arr[i];v.clear();v.pb(j);ctr = 1;
                }else if(xx[j].arr[i] == smallest && !xx[j].used){
                    ctr++;v.pb(j);
                }
            }
            if(ctr == 1){
                vz.pb(ii(-1, v[0]));
                culprit = i;
                //printf("masuk");
                FOR(Q, n){
                    punya[Q] = xx[v[0]].arr[Q];
                }
            }else if(ctr == 2){
                vz.pb(ii(v[0],v[1]));
                //printf("used: %d %d\n", v[0], v[1]);
            }
            FOR(j,2*n-1){
                if(xx[j].arr[i] == smallest){
                    xx[j].used = true;
                }
            }
        }

        FOR(i, n){
            ii xy = vz[i];
            int x = xy.fi;
            int y = xy.se;
            if(x == -1){
                arr[i] = punya[i];
            }else{
                if(xx[x].arr[culprit] != punya[i])arr[i] = xx[x].arr[culprit];
                else arr[i] = xx[y].arr[culprit];
            }
        }



        printf("Case #%d: ", ctr++);
        FOR(zzz,n)printf("%d ", arr[zzz]);
        printf("\n");
    }





    return 0;
}



