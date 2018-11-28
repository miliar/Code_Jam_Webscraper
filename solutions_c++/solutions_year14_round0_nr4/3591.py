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
template<class X>void debug(vector<X>v){cerr<<endl;for(int i=0;i<v.size();i++)cerr<<v[i]<<" ";cerr<<endl;}




int main()
{

    freopen("D-large.in","r",stdin);
    freopen("od2.txt","w",stdout);
    int T,i,j,k,n;
    cin>>T;


    for( int cs=1;cs<=T;cs++ )
    {
        printf("Case #%d: ",cs);
        cin>>n;
       // cout<<n<<endl;
        vector<double>a(n),b(n);
        for(i=0;i<n;i++)cin>>a[i];
        for(i=0;i<n;i++)cin>>b[i];

        SORT(a);
        SORT(b);
    //    reverse(ALL(b));


       // debug(a);
      //  debug(b);
        k=0;
        j=n-1;
        for( i=n-1;i>=0;i-- )
        {
            if(a[j]>b[i] )
            {
                j--;
                k++;
            }

        }
        cout<<k<<" ";
        vi vst(n,0);
      //  reverse(ALL(b));
        for( i=0;i<n;i++ )
        {
            for(j=0;j<n;j++)
            {
                if( vst[j] )continue;
                if( b[j]>a[i] )
                {
                    vst[j]=1;
                    break;
                }
            }
            if(j==n)break;
        }
        cout<<n-i<<endl;

    }
    return 0;
}














