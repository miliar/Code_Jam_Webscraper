#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<vector>
using namespace std;

#define sc scanf
#define sc1(a) scanf( "%d", &a )
#define pr printf
#define pr1(a) printf( "%ld\n", a )
#define all(v) v.begin(),v.end()
#define fr( i, n ) for( __typeof(n) i=0; i<n; i++ )
#define rv( i, n ) for( __typeof(n) i=n-1; i>=0; i-- )
#define fo( i, m, n ) for( __typeof(n) i=m; i<=n; i++ )
#define ms( a, val ) memset( a, val, sizeof(a) )
#define pb push_back
#define mp make_pair
#define f1 first
#define s2 second
#define re return
#define g() getchar()
#define db double
#define ll long long

vector< pair< db, int > > N, K;

bool DeceitWar( db x )
{
    int i, n = K.size();
    rv( i, n )
    {
        if( K[i].s2 == 0 && K[i].f1 < x )
        {
            K[i].s2 = 1;
            re true;
        }
    }
    re false;
}
int main()
{
    freopen("D-large.in","r",stdin);
    freopen("out.txt","w",stdout);

    int l, c, t, n, i, j, k;
    db d;

    sc1(t);

    fr( i, t )
    {
        l = c = 0;
        N.clear();
        K.clear();

        sc1(n);
        fr( j, n )
        {
            sc( "%lf", &d );
            N.pb(mp( d,0 ));
        }
        fr( j, n )
        {
            sc( "%lf", &d );
            K.pb(mp( d,0 ));
        }
        sort( all(N) );
        sort( all(K) );

        fr( j, n )
        {
            fr( k, n )
            {
                if( K[k].s2 == 0 )
                {
                    if( K[k].f1 > N[j].f1)
                    {
                        l++;
                        N[j].s2 = 1;
                        K[k].s2 = 1;
                        break;
                    }
                }
            }
        }
        fr( j, n )
        {
            N[j].s2 = 0;
            K[j].s2 = 0;
        }
        rv( j, n )
        {
            if( DeceitWar( N[j].f1 ) )
            {
                c++;
                N[j].s2 = 1;
            }
        }
        pr( "Case #%d: %d %d\n", i+1, c, (n-l) );
    }
    return 0;
}
