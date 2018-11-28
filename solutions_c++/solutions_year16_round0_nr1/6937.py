#include <cstdio>
#include <sstream>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <algorithm>
#include <set>
#include <queue>
#include <stack>
#include <list>
#include <iostream>
#include <fstream>
#include <numeric>
#include <string>
#include <vector>
#include <cstring>
#include <map>
#include <iterator>

using namespace std;

#define MXN
#define MXE
#define MXQ
#define SZE 50
#define MOD
#define EPS
#define INF 1000000009
#define HI printf("HI\n")
#define sf scanf
#define pf printf
#define sf1(a) scanf("%d",&a)
#define sf2(a,b) scanf("%d %d",&a,&b)
#define sf1ll(a) scanf("%lld",&a)
#define sf2ll(a,b) scanf("%lld %lld",&a,&b)
#define takei(a)                                 scanf("%d", &a)
#define takell(a)                                scanf("%I64d", &a)
#define takellu(a)                               scanf("%I64uu",
#define forln(i,a,n) for(int i=a ; i<n ; i++)
#define foren(i,a,n) for(int i=a ; i<=n ; i++)
#define forg0(i,a,n) for(int i=a ; i>n ; i--)
#define fore0(i,a,n) for(int i=a ; i>=n ; i--)
#define pb push_back
#define ppb pop_back
#define ll long long int
#define ul unsigned long
#define ull unsigned long long
#define fs first
#define sc second
#define clr( a, b ) memset((a),b,sizeof(a))
#define jora pair<int, int>
#define jora_d pair<double, double>
#define jora_ll pair<long long int, long long int>
#define mp make_pair
#define max3(a,b,c) max(a,max(b,c))
#define min3(a,b,c) min(a,min(b,c))
#define PI acos(0.0)

template<class T1> void deb(T1 e1)
{
    cout<<e1<<endl;
}
template<class T1,class T2> void deb(T1 e1,T2 e2)
{
    cout<<e1<<" "<<e2<<endl;
}
template<class T1,class T2,class T3> void deb(T1 e1,T2 e2,T3 e3)
{
    cout<<e1<<" "<<e2<<" "<<e3<<endl;
}
template<class T1,class T2,class T3,class T4> void deb(T1 e1,T2 e2,T3 e3,T4 e4)
{
    cout<<e1<<" "<<e2<<" "<<e3<<" "<<e4<<endl;
}
template<class T1,class T2,class T3,class T4,class T5> void deb(T1 e1,T2 e2,T3 e3,T4 e4,T5 e5)
{
    cout<<e1<<" "<<e2<<" "<<e3<<" "<<e4<<" "<<e5<<endl;
}
template<class T1,class T2,class T3,class T4,class T5,class T6> void deb(T1 e1,T2 e2,T3 e3,T4 e4,T5 e5,T6 e6)
{
    cout<<e1<<" "<<e2<<" "<<e3<<" "<<e4<<" "<<e5<<" "<<e6<<endl;
}

// bitmask setting

//int set_e( int n, int pos ){
//    return n = n|( 1<<pos );
//}
//bool check( int n, int pos ){
//    return (bool)( n&( 1<<pos ) );
//}
//int reset_e( int n, int pos ){
//    return n = n&~( 1<<pos );
//}


// moves

//int dx[]= {-1,-1,0,0,1,1};
//int dy[]= {-1,0,-1,1,0,1};
//int dx[]= {0,0,1,-1};/*4 side move*/
//int dy[]= {-1,1,0,0};/*4 side move*/
//int dx[]= {1,1,0,-1,-1,-1,0,1};/*8 side move*/
//int dy[]= {0,1,1,1,0,-1,-1,-1};/*8 side move*/
//int dx[]={1,1,2,2,-1,-1,-2,-2};/*night move*/
//int dy[]={2,-2,1,-1,2,-2,1,-1};/*night move*/

ll n;
bool visit[20];
void reset();
bool is_found( ll num );

int main(){
//    freopen("A-large.in", "r", stdin);
//    freopen("output.txt", "w", stdout);
    int t, cas, i, j, k;
    ll num;
    sf("%d", &t);

    for( cas = 1; cas<=t; cas++ ){
        reset();
        sf("%lld", &n);
        if( !n ){
            pf("Case #%d: INSOMNIA\n", cas);
            continue;
        }
        num = n;
        while( !is_found(num) ){
            num += n;
        }
        pf("Case #%d: %lld\n", cas, num);
    }

    return 0;
}
void reset(){
    clr( visit, 0 );
}
bool is_found( ll num ){
    char str[SZE+7];
    int len, i, j, k;
    sprintf( str, "%lld", num);
    len = strlen( str );
    for( i = 0; i<len; i++ ){
        visit[ str[i]-'0' ] = 1;
    }
    for( i = 0; i<=9; i++ ){
        if( !visit[i] ){
            return 0;
        }
    }
    return 1;
}


























