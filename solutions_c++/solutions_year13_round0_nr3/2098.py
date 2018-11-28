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

#define filer() freopen("C-large-1.in","r",stdin)
#define filew() freopen("CL.txt","w",stdout)

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


ll A[]={0LL,1LL,4LL,9LL,121LL,484LL,10201LL,12321LL,14641LL,40804LL,44944LL,1002001LL,1234321LL,4008004LL,100020001LL,102030201LL,104060401LL,121242121LL,123454321LL,125686521LL,400080004LL,404090404LL,10000200001LL,10221412201LL,12102420121LL,12345654321LL,40000800004LL,1000002000001LL,1002003002001LL,1004006004001LL,1020304030201LL,1022325232201LL,1024348434201LL,1210024200121LL,1212225222121LL,1214428244121LL,1232346432321LL,1234567654321LL,4000008000004LL,4004009004004LL,100000020000001LL};


int find1(ll v)
{
    int lo=0;
    int hi=40;

    int ret,mid;

    while(hi>=lo)
    {

        mid=(hi+lo)>>1;

        if(A[mid]>=v)
        {
            ret=mid;
            hi=mid-1;
        }
        else lo=mid+1;

    }

    return ret;

}

int find2(ll v)
{
    int lo=0;
    int hi=40;

    int ret,mid;

    while(hi>=lo)
    {

        mid=(hi+lo)>>1;

        if(A[mid]<=v)
        {
            ret=mid;
            lo=mid+1;
        }
        else hi=mid-1;

    }

    return ret;

}

int main()
{

   // cout<<A[40]<<endl;
    //cout<<find2(10)<<endl;
    //filer();
   // filew();
    ll a ,b;

    int T,ks,l,r,i;

    scanf("%d",&T);



    FOR(ks,1,T)
    {
        scanf("%lld%lld",&a,&b);

        int out=0;
/*        REP(i,40)
        {
            if(A[i]>=a && A[i]<=b)
            {
                cout<<A[i]<<endl;
                out++;
            }
        }
*/
  //      cout<<out<<endl;
        //cout<<a<<" "<<b<<endl;


        l=find1(a);

        //cout<<l<<endl;

        r=find2(b);


//        cout<<l<<" "<<r<<endl;

        printf("Case #%d: %d\n",ks,r-l+1);

    }


    return 0;
}


