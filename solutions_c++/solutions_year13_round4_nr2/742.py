/*
TASK: B
LANG: C++
*/
#include <iostream>
#include <cstdio>
#include <queue>
#include <stack>
#include <algorithm>
#include <cstring>
#include <numeric>
#include <ext/hash_map>
#include <ext/hash_set>
#include <cmath>
#include <cassert>
#include <map>
#include <vector>
#include <ctime>
#include <string>
#define foreach(_var,_container) for( typeof( (_container).begin() ) _var = (_container).begin() ; _var != (_container).end() ; ++_var )
#define now() double( double( clock() ) / double( CLOCKS_PER_SEC ) )
#if 1
#define eprintf(msg, ... ) fprintf(stderr," %s:%d in %s at %.4lf :: " msg "\xA" , strrchr( __FILE__ , '\\' )+1 , __LINE__ , __FUNCTION__ , now() , ##__VA_ARGS__ )
#else
#define eprintf(msg, ... ) 0
#endif
#define pprintf(msg, ... ) fprintf(stderr," %s:%d in %s at %.4lf :: " msg "\xA" , strrchr( __FILE__ , '\\' )+1 , __LINE__ , __FUNCTION__ , now() , ##__VA_ARGS__ )

using namespace std;
using namespace __gnu_cxx;

typedef long long ll;
typedef pair<int,int> PII;

#define PB push_back
#define MP make_pair
#define CLEAR0(x) memset( (x) , 0 , sizeof((x)) )
#define CLEAR1(x) memset( (x) , -1 , sizeof((x)) )

const double EPS = 1e-9;
const ll INF = 1LL << 60;

inline int epscmp( double a , double b ){
    if( fabs(a-b) < EPS )
        return 0;
    else if( a + EPS < b )
        return -1;
    else
        return 1;
}

const int MAXN = 10;

ll N, P;

void clear(){
    ///Warning: Clear everything used by a test!
}

void read(){
    /// Input read goes here
    //scanf("%d %lld", &N, &P);
    cin >> N >> P;
}

void solve( int testid ){
    /// Solution goes here
    
    ll best1 = 0;
    ll best2 = 0;
    /*
    for( int off = 0 ; off < (1 << N) ; off++ ){
        int bef = off;
        int after = (1 << N) - 1 - off;
        
        int a = 0, b = 0;
        
        for( int i = 0 ; i < N ; i++ ){
            if( bef >= (1LL << i) ){
                a += (1 << (N - 1 - i));
                bef -= (1LL << i);
            }
            
            if( after >= (1LL << i) ){
                b += (1 << (N - 1 - i));
                after -= (1LL << i);
            }
        }
        
        fprintf(stderr, "#%d -> %d, %d\n", off, a, b);
        
        if( a < P ){
            best1 = off;
        }
        
        if( (1 << N) - P <= b )
            best2 = off;
    }
    */
    
    ll la = 0, ra = (1LL << N) - 1;
    
    while( la <= ra ){
        ll ma = (la + ra) / 2;
        
        ll bef = ma;
        ll a = 0;
        
        for( int i = 0 ; i < N ; i++ ){
            if( bef >= (1LL << i) ){
                a += (1LL << (N - 1 - i));
                bef -= (1LL << i);
            }
        }
        
        if( a < P )
            best1 = ma, la = ma + 1;
        else
            ra = ma - 1;
    }
    
    ll lb = 0, rb = (1LL << N) - 1;
    
    while( lb <= rb ){
        ll mb = (lb + rb) / 2;
    
        ll after = (1LL << N) - 1 - mb;
        
        ll b = 0;
        
        for( int i = 0 ; i < N ; i++ ){
            if( after >= (1LL << i) ){
                b += (1LL << (N - 1 - i));
                after -= (1LL << i);
            }
        }
        
        if( (1LL << N) - P <= b )
            best2 = mb, lb = mb + 1;
        else
            rb = mb - 1;
    }
    
    /// Warning: The " " after : INCLUDED!!!
    printf("Case #%d: ", testid+1);
    /// Output goes here:
    
    //printf("%lld %lld", best1, best2);
    
    cout << best1 << " " << best2;
    
    /// I take care of the newline!
    printf("\xA");
}

int main(){
    freopen( "B.in" , "r" , stdin );
    freopen( "B.out" , "w" , stdout );
    
    int numtests;
    
    scanf("%d", &numtests);
    
    for( int i = 0 ; i < numtests ; i++ ){
        clear();
        read();
        solve( i );
    }
    
    return 0;
}
