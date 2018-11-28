#pragma warning(disable:4786)

#define ll __int64
#define vi vector <ll>
#define pii pair <ll,ll>
#define FOR(i, a, b) for (i = (a); i <= (b); i++)
#define REP(i, a) for (i = 0; i < (a); i++)
#define ALL(v) (v).begin(), (v).end()
#define SET(a, x) memset((a), (x), sizeof(a))
#define SZ(a) ((ll)(a).size())
#define CL(a) ((a).clear())
#define SORT(x) sort(ALL(x))
#define mp make_pair
#define pb push_back
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))

#define filer() freopen("in.txt","r",stdin)
#define filew() freopen("out.txt","w",stdout)

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <queue>
#include <cassert>


using namespace std;


map< ll , ll > S,E;

ll mod=1000002013;

int main()
{
    ll T,ks,i,j,k,n,m,p,s,e;

    ll ans;




  //  filer();


 //   freopen("A-small-attempt0.in","r",stdin);
   // freopen("A1.txt","w",stdout);
    freopen("A-large.in","r",stdin);
//    freopen("A2.txt","w",stdout);

    scanf("%I64d",&T);

    FOR( ks,1,T )
    {


        scanf("%I64d%I64d",&n,&m);



        CL(S);
        CL(E);

		ll ans1=0;




        REP( i,m )
        {
//            cin>>s>>e>>p;
			scanf("%I64d%I64d%I64d",&s,&e,&p);


            S[s]+=p;
            E[e]+=p;

			ans1+=((((( e-s )*( e-s-1 ))/2))%mod*p)%mod;

        }

        ll ans2=0;
        ll v;

        map< ll,ll > :: iterator it1,it2;



        it1=S.end();

        while( true )
        {

            if( it1==S.begin() )break;
            it1--;

            it2=E.begin();


            while(true)
            {



                if( it2->first>=it1->first && it2->second )
                {
                    v=MIN( it1->second , it2->second );



                    i=it1->first;
                    j=it2->first;

                    it2->second-=v;
                    it1->second-=v;

                    ans2+= ( (( ( j-i )*( j-i-1 )/2 ))%mod*v)%mod;
                }

                if( !it1->second )break;

				it2++;
				if( it2==E.end() )break;
            }

        }



        printf("Case #%I64d: %I64d\n",ks,(ans2-ans1+mod)%mod);
    }

    return 0;
}

