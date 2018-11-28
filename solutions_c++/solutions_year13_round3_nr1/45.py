#define ll __int64
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


#define NN 1000006

char s[ NN ];
int a[NN];

int main()
{
    int i,j,k,ks,T,n,l;


    //filer();


    freopen("A-large.in","r",stdin);
    freopen("A-large.txt","w",stdout);


    scanf("%d",&T);


    map<char,bool>Map;

    Map['a']=1;
    Map['e']=1;
    Map['i']=1;
    Map['o']=1;
    Map['u']=1;



    FOR(ks,1,T)
    {


        scanf("%s",s+1);
        scanf("%d",&n);

       // cout<<s+1<<endl;


        l=strlen(s+1);

        for( i=1;i<=l;i++ )
        {
            if( !Map[ s[i] ] )a[i]=a[i-1]+1;
            else a[i]=0;


            //cout<<a[i]<<" ";
        }
      //  cout<<endl;while(1);


        ll ans=0;

        j=1;

        for( i=1;i<=l;i++ )
        {
            for(;j<=l;j++)if( MIN( a[j] , j-i+1 )>=n )break;
            ans+=( l-j+1 );
        }




        printf("Case #%d: ",ks);
        printf("%I64d\n",ans);
    }


    return 0;

}
