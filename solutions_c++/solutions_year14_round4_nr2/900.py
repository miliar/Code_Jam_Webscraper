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
int n;
bool good(vi v){
    int p1 = 1;
    while( p1 < n and v[p1-1] < v[p1] ) p1++;
    while( p1 < n and v[p1-1] > v[p1] ) p1++;
    return p1 == n;
}

int get(vi a,vi v){
    int x = 0;
    for(int i = 0 ; i < n ; i++){
        for(int j = 0 ; j < n ; j++){
            if( a[i] == v[j] ){
                if( i == j ) continue;
                if( i < j ){
                    for(int k = j ; k > i ; k--)
                        swap( v[k] , v[k-1] ), x++;
                }
                else{
                    for(int k = i ; k < j ; k++)
                        swap( v[k] , v[k+1] ), x++;
                }
                break;
            }
        }
    }
    
    return x;
}

int main(){
    int tc;
    int x = sc(tc);
    for(int tt = 1 ; tt <= tc ; tt++){
        printf("Case #%d: ",tt);
        x = sc(n);
        vi v(n);
        for(int i = 0 ; i < n ; i++)
            x = sc(v[i]);
        
        if( n <= 2 ){
            printf("0\n");
            continue;
        }
        vi a = v;
        sort( all(a) );
        int ans = inf;
        do{
            if( !good( a ) ) continue;
            ans = min( ans , get( a , v ) );
        }while( next_permutation( all(a) ) );
        printf("%d\n",ans);
    }
    return 0;
}
