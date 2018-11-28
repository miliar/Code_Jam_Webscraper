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
#define INF 2000000000 // 2 billion
#define EPS 1e-9
#define MOD 1000000007

int n , k ;
vector < pair < int , vi > > ans;
void recurse( int mask , int idx )
{
    if( idx == n - 1  )
    {
        vi tmp;
        REP( i , 2 , 10 )
        {
            ll j = 2;
            while( j <= 1000 )
            {
                ll val = 0 , powk = 1;
                REP( l , 0 , n - 1 )
                {
                    if( mask & ( 1 << l ) )
                    {
                        val += powk;
                        val %= j;
                    }
                    powk = powk * i ;
                    powk %= j ;
                }
                if( val == 0 )
                {
                    tmp.push_back( j );
                    break;
                }
                j++;
            }
        }
        if( tmp.size() == 9 )
            ans.push_back( make_pair( mask , tmp ) ) ;
        return ;
    }
    if( ans.size() < k )
        recurse( mask , idx + 1 );
    if( ans.size() < k )
        recurse( mask | ( 1 << idx) ,idx + 1 );
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
        s(n) ; s(k);
        ans.clear();
        printf("Case #%d:\n",T);
        recurse( 1 | ( 1 << ( n - 1 ) ) , 1  );
        REP( i , 0 , k - 1 )
        {
            NREP( j , n - 1 , 0 )
            {
                if( ans[i].first & ( 1<< j ) )
                    printf("1");
                else
                    printf("0");
            }
            REP( j , 0 , 8 )
            {
                printf(" %d",ans[i].second[j]);
            }
            printf("\n");
        }

    }
    return 0;
}


