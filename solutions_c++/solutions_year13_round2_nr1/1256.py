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


int count( ll &A,int val )
{

	if(A>val)return 0;
    int i;
    if( A==1 )return 10000;

    for( i=1;;i++ )
    {
        A+=(A-1);
        if( A>val )return i;
    }

}

int v[10004];

int main()
{
    freopen("A-large.in","r",stdin);
   // freopen("a2.txt","w",stdout);

    int T,ks,i,j,k;


    scanf("%d",&T);

    FOR(ks,1,T)
    {

        int n;
        ll A;


        cin>>A>>n;


        REP(i,n)
        {
            scanf("%d",&v[i]);
        }

        sort(v,v+n);


        int ans=0;
        i=0;

        while( i<n && A>v[i] )
        {
            A+=v[i];
            i++;
        }


        int out=10000,rest,need;

        if( i==n )out=0;
        //cout<<i<<endl;while(1);

     //   cout<<i<<endl;
       // while(1);

      // cout<<A<<endl;while(1);

        for( j=i;j<n;j++ )
        {

            rest=n-j;
            out=MIN( out,ans+rest );

            need=count(A,v[j]);

            if( rest<need )
            {
                out=MIN( out,ans+rest );
                break;
            }


            ans+=need;
            A+=v[j];

        //    cout<<ans<<" "<<need<<" "<<rest<<endl;

        }

        if(j==n)out=MIN( out,ans );

       // while(1);


        printf("Case #%d: ",ks);
        printf("%d\n",out);
    }


    return 0;
}

