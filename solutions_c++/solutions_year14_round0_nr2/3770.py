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



#define EPS .000000009



bool canAchive( double t,double C,double F,double X)
{
    // reach X
    // needs C to get a firm
    // F per firm

    double tot=0;
    while( true )
    {

        double p=(2+tot*F)*t;
       // cout<<p<<" "<<X<<endl;
        if( fabs( p-X )<EPS || p>X )return true; //existing firms gula dia e reach kora gelo


        double nt=(double)C/( 2.0+tot*F ); //new firm add kora possible kina ?
        if( nt>t )return false;

        tot++;  //added new firm
        t-=nt;

    }

}

int main()
{

    freopen("B-large.in","r",stdin);
    freopen("ob2.txt","w",stdout);
    int T;
    double C,F,X;
    cin>>T;
    int i,j,k;
    for(int cs=1;cs<=T;cs++)
    {
        cin>>C>>F>>X;
       // for(i=0;i<=100;i++)
       // cout<<i<<" "<<canAchive( i,C,F,X )<<endl;

        double lo=EPS,mid,hi=X;
        while( fabs(hi-lo)>EPS )
        {
            mid=(hi+lo)*.5;

           // cout<<hi<<" "<<lo<<" "<<mid<<" "<<canAchive( mid,C,F,X )<<endl;

            if( canAchive( mid,C,F,X ) )hi=mid-EPS;
            else lo=mid+EPS;

        }
        cerr<<cs<<" "<<hi+EPS<<endl;
        printf("Case #%d: %.7lf\n",cs,hi+EPS);
    }

    return 0;
}










