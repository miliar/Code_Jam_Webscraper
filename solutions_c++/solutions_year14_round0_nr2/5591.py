#include<bits/stdc++.h>
using namespace std;
#define pi (2.0*acos(0.0))
#define eps 1e-6
#define ll long long
#define inf (1<<29)
#define vi vector<int>
#define vll vector<ll>
#define sc(x) scanf("%d",&x)
#define scl(x) scanf("%lld",&x)
#define all(v) v.begin() , v.end()
#define me(a,val) memset( a , val ,sizeof(a) )
#define pb(x) push_back(x)
#define pii pair<int,int> 
#define mp(a,b) make_pair(a,b)
#define Q(x) (x) * (x)
#define L(x) ((x<<1) + 1)
#define R(x) ((x<<1) + 2)
#define M(x,y) ((x+y)>>1)
#define fi first
#define se second
#define MOD 1000000007
#define checkmin( a , b ) a = min( a , b )
#define ios ios::sync_with_stdio(0);
#define N 100001

int main(){
    int tc;
    sc(tc);
    for(int tt = 1 ; tt <= tc ; tt++){
        double C , X , F;
        cin >> C >> F >> X;
        double ans = X / 2 , prod = 2;
        double need = 0;
        for(int i = 1 ; i <= 100000 ; i++){
            //cout << need << " " << C / prod  << endl;
            need += C / prod;
            prod += F;
            checkmin( ans , need + X / prod );
        }
        printf("Case #%d: %.7lf\n", tt , ans );
    }
    return 0;
}
