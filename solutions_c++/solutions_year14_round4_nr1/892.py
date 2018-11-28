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
#define ios ios::sync_with_stdio(0);
#define N 100001

int main(){
    int tc;
    int x = sc(tc);
    for(int tt = 1 ; tt <= tc ; tt++){
        printf("Case #%d: ",tt);    
        int n , C;
        x = scanf("%d%d",&n,&C);
        vi v(n);
        for(int i = 0 ; i < n ; i++)
            x = sc(v[i]);
        if( n == 1 ){
            printf("1\n");
            continue;
        }
        sort(all(v));
        vector<bool> used( n , 0 );
        int ans = 0;
        for(int i = n - 1 ; i >= 0 ; i--)if( !used[i] ){
            bool ok = 0;
            for(int j = i - 1 ; j >= 0 ; j--)if( !used[j] ){
                if( v[i] + v[j] <= C ){
                    used[i] = 1, used[j] = 1;
                    ans++;
                    ok = 1;
                    break;
                }
            }
            if( !ok ) used[i] = 1, ans++;
        }
        printf("%d\n",ans);
    }
    return 0;
}
