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
#define SZE
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

int main(){
//    freopen("A-large.in", "r", stdin);
//    freopen("output.txt", "w", stdout);
    int t, cas, n, len, cnt[30], arr[13], tmp, ch, i, j, k;
    char str[5000];
    sf("%d", &t);

    for( cas = 1; cas<=t; cas++ ){
        sf("%s", str);
        len = strlen( str );
        clr( cnt, 0 );
        clr( arr, 0 );
        for( i = 0; i<len; i++ ){
            tmp = str[i] - 'A';
            cnt[tmp]++;
        }
//        deb( cnt[13] );
        arr[0] = cnt[25];
        cnt[14] -= arr[0];
        cnt[17] -= arr[0];
        arr[2] = cnt[22];
        cnt[14] -= cnt[22];
        arr[4] = cnt[20];
        cnt[5] -= arr[4];
        cnt[14] -= arr[4];
        cnt[17] -= arr[4];
        arr[6] = cnt[23];
        cnt[18] -= arr[6];
        arr[8] = cnt[6];
        arr[7] = cnt[18];
        cnt[13] -= arr[7];
        cnt[21] -= arr[7];
        arr[1] = cnt[14];
        cnt[13] -= arr[1];
        arr[9] = cnt[13]/2;
        arr[5] = cnt[21];
        arr[3] = cnt[17];
        pf("Case #%d: ", cas);
        for( i = 0; i<=9; i++ ){
            for( j = 0; j<arr[i]; j++ ){
                pf("%d", i);
            }
        }
        pf("\n");
    }

    return 0;
}







































