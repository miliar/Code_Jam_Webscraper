
#define ll long long
#define vi vector <int>
#define pii pair <int,int>
#define FOR(i, a, b) for (i = (a); i <= (b); i++)
#define REP(i, a) for (i = 0; i < (a); i++)
#define ALL(v) (v).begin(), (v).end()
#define SET(a, x) memset((a), (x), sizeof(a))
#define SZ(a) ((int)(a).size())
#define CL(a) ((a).clear())
#define SORT(x) sort(ALL(x))
#define mp make_pair
#define pb push_back
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))

#define filer() freopen("D-small-attempt1.in","r",stdin)
#define filew() freopen("DS.txt","w",stdout)

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
#include <cassert>
#include <queue>


using namespace std;




#define NN 21

int dp[ 1<<NN ];
bool pos;
int True, vst[ 1<<NN ];

int K,n;

int Key[202][500],pre[500];
int nKey[202],L[202];

void go(  int mask )
{

	if(pos)return;
    if(vst[mask]==True)return;

//    cout<<mask<<endl;

    vst[mask]=True;

    if( mask==((1<<n)-1) )
    {
        pos=true;
        return;
    }



    multiset<int>Set;




    int i,j;

    REP(i,K)Set.insert( pre[i] );

    REP(i,n)
    {

        if( mask & (1<<i) )
        {

            REP(j,nKey[i])
            {
                Set.insert( Key[i][j] );
            }

        }
    }

    REP(i,n)
	{
		if( mask & (1<<i) )Set.erase( Set.find( L[i] ) );
	}

    REP(i,n)
    {
		if(pos)return;
        if( mask & (1<<i) )continue;
        if( Set.find( L[i] )!=Set.end() )
        {
            go( mask | (1<<i) );
            if(pos)
            {
                dp[mask]=i;
                break;
            }
        }
    }


    return;

}

int main()
{

  //  filer();
   // filew();

    int T,ks,i,j;


    scanf("%d",&T);

  //  cout<<T<<endl;
   // while(1);


    FOR(ks,1,T)
    {



        scanf("%d%d",&K,&n);

       // cout<<K<<" "<<n<<endl;

        REP(i,K)scanf("%d",&pre[i]);


        REP(i,n)
        {
            scanf("%d%d",&L[i],&nKey[i]);
            REP(j,nKey[i])scanf("%d",&Key[i][j]);
        }



        True++;
        pos=false;

        go( 0 );

        printf("Case #%d:",ks);

        if(pos)
        {
			int mask=0;
			for(i=0;i<n;i++)
			{
				printf(" %d",dp[mask]+1);
				mask|=(1<<dp[mask]);
			}
			printf("\n");
        }
        else printf(" IMPOSSIBLE\n");




    }

    return 0;
}


