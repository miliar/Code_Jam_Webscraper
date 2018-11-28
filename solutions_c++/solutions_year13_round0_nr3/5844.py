#include<cstdio>
#include<iostream>
#include<cstring>
#include<vector>
#include<cmath>
#include<algorithm>
#include<climits>
#include<set>
#include<deque>
#include<queue>
#include<map>
#include<climits>
#include<string>
#include<stack>
#include<sstream>
using namespace std;
#define pi (2.0*acos(0.0))
#define eps 1e-6
#define ll long long
#define inf (1<<30)
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
#define MOD 10009
#define N 1000000

bool T[N+5];

bool pal(int x){
    int xx = x , r = 0;
    while( x ){
        r = r * 10 + x%10;
        x /= 10;
    }
    return xx == r;
}

void process(){
    for(int i = 1 ; i <= 1000000 ; i++)
        T[i] = pal( i );
    
}

int main(){
    process();
    int tc , A , B;
    sc(tc);
    for(int test = 1 ; test <= tc ; test++){
        sc(A),sc(B);
        int ans = 0;
        for(int i = 1 ; i <= 1000 ; i++)
            ans += T[i] && T[i*i] && (i*i<=B) && (i*i>=A);
        
        printf("Case #%d: %d\n",test,ans);
    }
    return 0;
}
