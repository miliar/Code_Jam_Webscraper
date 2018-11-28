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
#define N 15

int n , C , best , ct , nodes[N] , T[N][100][27];
int aux[100][27];
vi v[4];
string a[N];

void add(int id,string s){
    int ac = 0;
    int l = s.size();
    for(int i = 0 ; i < l ; i++){
        if( T[id][ac][s[i] - 'A'] == 0 ) T[id][ac][s[i] - 'A'] = nodes[id]++;
        ac = T[id][ac][s[i]- 'A'];
    }
}

void back(int x){
    if( x == n ){
        int ans = 0;
        for(int i = 0 ; i < C ; i++)
            if( v[i].size() == 0 ) return;
        
        for(int i = 0 ; i < C ; i++)
            nodes[i] = 1;
        me(T,0);
        for(int i = 0 ; i < C ; i++)
            for(int j = 0 ; j < v[i].size() ; j++)
                add( i , a[ v[i][j] ]  );
        
        for(int i = 0 ; i < C ; i++)
            ans += nodes[i];
        
        if( ans > best ) best = ans , ct = 1;
        else if( ans == best ) ct++;
        
        return;
    }
    for(int i = 0 ; i < C ; i++){
        v[i].pb( x );
        back( x + 1 );
        v[i].pop_back();
    }
}

int main(){
    int tc;
    int x = sc(tc);
    for(int tt = 1 ; tt <= tc ; tt++){
        printf("Case #%d: ",tt);
        x = scanf("%d%d",&n,&C);
        for(int i = 0 ; i < n ; i++)
            cin >> a[i];
        
        best = 0;
        ct = 0;
        back( 0 );
        printf("%d %d\n",best,ct);
    }
    return 0;
}
