#include<bits/stdc++.h>

using namespace std;

// Shortcuts for "common" data types in contests
typedef long long int ll;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef set<int> si;
typedef map<string, int> msi;
// To simplify repetitions/loops, Note: define your loop style and stick with it!
#define s(i) scanf("%d",&i)
#define sl(i) scanf("%ld",&i)
#define sll(i) scanf("%lld",&i)
#define REP(i, a, b) \
for (int i = int(a); i <= int(b); i++) // a to b, and variable i is local!
#define NREP(i,a,b) \
for (int i = int(a); i >= int(b); i--)
#define TRvi(c, it) \
for (vi::iterator it = (c).begin(); it != (c).end(); it++)
#define TRvii(c, it) \
for (vii::iterator it = (c).begin(); it != (c).end(); it++)
#define TRmsi(c, it) \
for (msi::iterator it = (c).begin(); it != (c).end(); it++)
#define INF 1000000000 // 2 billion
#define EPS 1e-9
#define MOD 1000000007

int n , k ;
vector < double > myvec;
double pro[22] , ans , dp[22][22] ;

double calculate( )
{
    REP( i , 0 , k + 2 )
        REP( j , 0 , k + 2 )
            dp[i][j] = 0 ;
    dp[0][0] = 1;
    REP( i , 0 , k - 1 )
    {
        REP( j , 0 , k - 1 )
        {
            dp[i + 1][j + 1] += myvec[i] * dp[i][j];
            dp[i + 1][j] += ( 1.000 - myvec[i] ) * dp[i][j] ;
        }
    }
    return dp[k][k / 2];
}

void recurse( int idx , int chosen )
{
    if( idx == n )
    {
        if( chosen == k )
            ans = max( ans , calculate() ) ;
        return;
    }
    myvec.push_back( pro[idx] ) ;
    recurse( idx + 1 , chosen + 1 );
    myvec.pop_back();
    recurse( idx + 1 , chosen );
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    //freopen("input.in","r",stdin);
    //freopen("output.out","w",stdout);
    int t ; s(t) ;
    REP( T , 1 , t )
    {
        s(n) ; s(k ) ;
        REP( i , 0 , n - 1  )
        {
            scanf("%lf",&pro[i]);
        }
        ans = 0;
        recurse( 0 , 0  );
        printf("Case #%d: %0.7lf\n",T,ans);
    }
    return 0;
}
