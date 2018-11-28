//{  Author :: Mahir Asef Kabir
//   AUST CSE 28th Batch
//   ID :: 11.02.04.105
//   Problem :: Problem A. The Repeater
//   Verdict ::
//{***************[        Templates        ]***************
using namespace std ;
//{***************[        C Headers        ]***************
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <climits>
#include <cstdio>
#include <cctype>
#include <cfloat>
#include <ctime>
//}
//{***************[        C++ Headers      ]***************
#include <algorithm>
#include <iostream>
#include <utility>
#include <iomanip>
#include <sstream>
#include <fstream>
#include <numeric>
#include <complex>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
#include <map>
//}
//{***************[        Loops            ]***************
#define forab(i,a,b) for( __typeof (a) i = a ; i <= b ; i++ )
#define forba(i,a,b) for( __typeof (a) i = a ; i >= b ; i-- )
#define rep(i,n) forab(i,0,n-1)
#define repn(i,n) forab(i,1,n)
#define repr(i,n) forba(i,n-1,0)
#define repnr(i,n) forba(i,n,1)
#define forstl(i, s) for ( __typeof ((s).end ()) i = (s).begin (); i != (s).end (); i++ )
//}
//{***************[        Values           ]***************
#define pi              3.141592653589793
#define eps             2.718281828459045
#define euler           0.577215664901532
#define ln              log
#define LOG             log10
#define INF             1<<30
#define MAX             1000000
//}
//{***************[        Macros           ]***************
#define memo(a,b)       memset (a,b,sizeof(a))
#define all(a)          a.begin () , a. end ()
#define clr(a)          a.clear ()
#define sz(a)           a.size()
#define sf              scanf
#define pf              printf
#define si(a)           scanf("%d",&a)
#define pb              push_back
#define MP              make_pair
#define nl              puts("")
#define ll                 long long
#define ull             unsigned long long
#define vi              vector < int >
#define vll             vector < ll >
#define pii             pair < int , int >
template <class T, class U> inline T max (T &a, U &b) { return a > b ? a : b; }
template <class T, class U> inline T min (T &a, U &b) { return a < b ? a : b; }
template< class T > T gcd(T a, T b) { return (b != 0 ? gcd<T>(b, a%b) : a); }
template< class T > T lcm(T a, T b) { return (a / gcd<T>(a, b) * b); }
//static struct _ { ios_base :: Init Init; _ () { cin.sync_with_stdio (false); cin.tie (false); } } _;
//}
//{***************[        Directions       ]***************
//int dx[]={1,0,-1,0};int dy[]={0,1,0,-1}; //4 Direction
//int dx[]={1,1,0,-1,-1,-1,0,1};int dy[]={0,1,1,1,0,-1,-1,-1};//8 direction
//int dx[]={2,1,-1,-2,-2,-1,1,2};int dy[]={1,2,2,1,-1,-2,-2,-1};//Knight Direction
//int dx[6]={2,1,-1,-2,-1,1};int dy[6]={0,1,1,0,-1,-1}; //Hexagonal Direction
//}
//{***************[        IO               ]***************
#define rd              freopen ( "input.txt" , "r" , stdin )
#define wr              freopen ( "output.txt" , "w" , stdout )
//}
class CLASS_NAME {
    public :
    int method_NAME () {}
} ;
int main () {
    rd ;
    wr ;
    int t ;
    si(t) ;
    rep(cs,t) {
        //cout << "Case :: " << cs+1 << endl ;
        int n ;
        cin >> n ;
        vector < string > v ;
        int arr[102][102] ;
        memo(arr,0) ;
        bool check = false ;
        map < string , int > mp ;
        string tmp ;
        rep(i,n) {
            string str ;
            tmp.clear() ;
            cin >> str ;
            v.pb ( str ) ;
            tmp.pb ( str[0] ) ;
            arr[i][0] = 1 ;
            int k = 0 ;
            for ( int j = 1 ; j < str.length() ; ++j ) {
                if ( str[j] != str[j-1] ) {
                    tmp.pb ( str[j] ) ;
                    k++ ;
                    arr[i][k]++ ;
                }
                else arr[i][k]++ ;
            }
            //cout << tmp << endl ;
            if ( i == 0 ) mp[tmp] = 1 ;
            else {
                if ( mp[tmp] == 0 ) {
                    printf("Case #%d: Fegla Won\n",cs+1) ;
                    check = true ;
                    break ;
                } else mp[tmp] = 1 ;
            }
        }
        if ( check ) continue ;
        int sz = tmp.size() ;
        /*for ( int i = 0 ; i < n ; i++ ) {
            for ( int j = 0 ; j < sz ; ++j ) {
                cout << arr[i][j] << " " ;
            }
            nl ;
        }*/
        int ans = 0 ;
        for ( int i = 0 ; i < sz ; i++ ) {
            vi a ;
            for ( int j = 0 ; j < n ; j++ ) {
                a.pb (arr[j][i]) ;
            }
            sort(all(a)) ;
//            rep(x,a.size()) cout << a[x] << " " ;
//            nl ;
            if ( a.size() % 2 ) {
                int mid = a.size()/2 ;
                for ( int it = 0 ; it < a.size() ; it++ ) ans += abs(a[it]-a[mid]) ;
            }
            else {
                int tmp = 0 , tmp2 = 0 ;
                int mid1 = a.size()/2 ;
                int mid2 = mid1-1 ;
                for ( int it = 0 ; it < a.size() ; it++ ) tmp += abs(a[it]-a[mid1]) ;
                for ( int it = 0 ; it < a.size() ; it++ ) tmp2 += abs(a[it]-a[mid2]) ;
                ans += min( tmp , tmp2 ) ;
            }
        }
        printf("Case #%d: %d\n",cs+1,ans) ;
    }
    return 0 ;
}


