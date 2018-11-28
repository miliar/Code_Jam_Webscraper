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
    sc(tc);
    for(int tt = 1 ; tt <= tc ; tt++){
        int m[4][4] , a , b , ans = 0;
        sc(a); a--;
        for(int i = 0 ; i < 4 ; i++)
            for(int j = 0 ; j < 4 ; j++)
                sc(m[i][j]);
        
        vector<int> v(17,0);
        for(int i = 0 ; i < 4 ; i++)
            v[ m[a][i] ]++;
        
        sc(b); b--;
        for(int i = 0 ; i < 4 ; i++)
            for(int j = 0 ; j < 4 ; j++)
                sc(m[i][j]);
        
        for(int i = 0 ; i < 4 ; i++)
            v[ m[b][i] ]++;
        
        int r = -1;
        for(int i = 1 ; i <= 16 ; i++)
            if( v[i] == 2 ) ans++ , r = i;
        
        printf("Case #%d: ",tt);
        if( ans == 0 ) printf("Volunteer cheated!\n");
        else if( ans == 1 ) printf("%d\n",r);
        else printf("Bad magician!\n");
            
    }
    return 0;
}
