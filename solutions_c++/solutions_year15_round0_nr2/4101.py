//BISMILLAHIRRAHMANIRRAHIM
/*
 manus tar shopner soman boro
 Author :: Shakil Ahmed
.............AUST_CSE27.........
 prob   ::
 Type   ::
 verdict::
 */

#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define pi acos(-1.0)
#define ff first
#define ss second
#define re return
#define QI queue<int>
#define SI stack<int>
#define SZ(x) ((int) (x).size())
#define all(x) (x).begin(), (x).end()
#define sqr(x) ((x) * (x))
#define ms(a,b) memset((a),(b),sizeof(a))
#define G() getchar()
#define MAX3(a,b,c) max(a,max(b,c))
#define II ( { int a ; read(a) ; a; } )
#define LL ( { Long a ; read(a) ; a; } )
#define DD ({double a; scanf("%lf", &a); a;})

double const EPS=3e-8;
using namespace std;

#define FI freopen ("input.txt", "r", stdin)
#define FO freopen ("1.txt", "w", stdout)

typedef long long Long;
typedef long long int64;
typedef unsigned long long ull;
typedef vector<int> vi ;
typedef set<int> si;
typedef vector<Long>vl;
typedef pair<int,int>pii;
typedef pair<string,int>psi;
typedef pair<Long,Long>pll;
typedef pair<double,double>pdd;
typedef vector<pii> vpii;

// For loop

#define forab(i, a, b)	for (__typeof (b) i = (a) ; i <= b ; ++i)
#define rep(i, n)		forab (i, 0, (n) - 1)
#define For(i, n)		forab (i, 1, n)
#define rofba(i, a, b)	for (__typeof (b)i = (b) ; i >= a ; --i)
#define per(i, n)		rofba (i, 0, (n) - 1)
#define rof(i, n)		rofba (i, 1, n)
#define forstl(i, s)	for (__typeof ((s).end ()) i = (s).begin (); i != (s).end (); ++i)

template< class T > T gcd(T a, T b) { return (b != 0 ? gcd<T>(b, a%b) : a); }
template< class T > T lcm(T a, T b) { return (a / gcd<T>(a, b) * b); }

//Fast Reader
template<class T>inline bool read(T &x){int c=getchar();int sgn=1;while(~c&&c<'0'||c>'9'){if(c=='-')sgn=-1;c=getchar();}for(x=0;~c&&'0'<=c&&c<='9';c=getchar())x=x*10+c-'0'; x*=sgn; return ~c;}

//int dx[]={1,0,-1,0};int dy[]={0,1,0,-1}; //4 Direction
//int dx[]={1,1,0,-1,-1,-1,0,1};int dy[]={0,1,1,1,0,-1,-1,-1};//8 direction
//int dx[]={2,1,-1,-2,-2,-1,1,2};int dy[]={1,2,2,1,-1,-2,-2,-1};//Knight Direction
//int dx[]={2,1,-1,-2,-1,1};int dy[]={0,1,1,0,-1,-1}; //Hexagonal Direction

/* **************************************  My code start here ****************************************** */

const int INF =  1 << 29 ;
const int MX = 11 ;
struct abc
{
    int freq[MX] = {0};
   // int ad = 0 ;
};
abc prv , now ;
queue < abc > q ;
int n  , inp[MX] ;
int main()
{
   // I will always use scanf and printf
   // May be i won't be a good programmer but i will be a good human being
   // /*
       FI ;
       FO ;
   // */
    int cs , t = II ;
    for ( cs = 1 ; cs <= t ; cs++ )
    {
        n = II ;
        int ans = INF , i , j , fst = 1 ;
        while( !q.empty() ) q.pop();
        queue < int > additional ;
        additional.push(0);
        for ( i = 0 ; i <= MX ; i++ ) now.freq[i] = 0 ;
        int mx = -1 ;
        rep ( i , n )
        {
            inp[i] = II ;
            if( mx < inp[i] ) mx = inp[i];
            now.freq[inp[i]]++;
        }
        //now.ad = 0 ;
        q.push(now);

        while(!q.empty())
        {
            if( fst >= 1000 ) break ;
            prv = q.front();
            q.pop();
            int addi = additional.front() ;
            int ekhon = 0 ;
            additional.pop();
            for ( i = mx ; i >= 1 ; i-- ) if( prv.freq[i] )
            {
                ekhon = i ;
                break ;
            }
            //printf("now :: %d ekhon + addi = %d + %d : %d\n",fst , ekhon , addi , ekhon + addi );
            ans = min( ans , ekhon + addi );

            fst++;

            if( i > 2 )
            for ( j = 1 ; j <= i / 2 ; j++ )
            {
                int a = j ;
                int b = i - j ;
                //printf("i :: %d j :: %d i - j :: %d\n",i,j,i-j);
                prv.freq[i]--;
                prv.freq[a]++;
                prv.freq[b]++;
                q.push(prv);
                additional.push( addi + 1 );
               // printf("i is %d a :: %d b :: %d addi :: %d\n",i , a , b , addi );
                prv.freq[i]++;
                prv.freq[a]--;
                prv.freq[b]--;

            }

        }

        printf("Case #%d: %d\n",cs,ans);
    }


    return 0;
}
