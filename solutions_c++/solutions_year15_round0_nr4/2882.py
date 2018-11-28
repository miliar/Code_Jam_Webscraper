/*
   nitesh kumar ( codeshaker )
*/

/**********START HERE ************/

#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <fstream>
#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <deque>
#include <vector>
#include <string>
#include <bitset>
#include <climits>
#include <complex>
typedef long long ll;
using namespace std;

#define pb push_back
#define nl puts ("")
#define ff first
#define ss second
#define mp make_pair
#define FOR(i,x,y) for(int i = (x) ; i <= (y) ; ++i)
#define ROF(i,x,y) for(int i = (y) ; i >= (x) ; --i)
#define CLR(x,y) memset(x,y,sizeof(x))
#define UNIQUE(V) (V).erase(unique((V).begin(),(V).end()),(V).end())
#define MIN(a,b) ((a)<(b)?(a):(b))
#define MAX(a,b) ((a)>(b)?(a):(b))
#define NUMDIGIT(x,y) (((int)(log10((x))/log10((y))))+1)
#define SQ(x) ((x)*(x))
#define ABS(x) ((x)<0?-(x):(x))
#define FABS(x) ((x)+eps<0?-(x):(x))
#define ALL(x) (x).begin(),(x).end()
#define SZ(x) ((int)(x).size())

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef  vector<int> vi;
typedef  vector<ll> vl;
typedef  vector<string> vs;
typedef  pair<int,int> pii;
typedef  pair<pii,int> ppi;
typedef  vector<pii> vpii;

#define mx7   10000007
#define mx6   1000006
#define mx5   100005
#define inf   1<<30                                           //infinity value
#define eps   1e-9
#define mod   ll(1e9+7)

/********** END HERE ***********/


int main(void)
{
    #ifndef ONLINE_JUDGE
   // freopen("input.txt","r",stdin);
  // freopen("output.txt","w",stdout);
    #endif
         ios::sync_with_stdio(false);
         int tc;
         cin>>tc;
         int ct=0;
         while(tc--)
         {
             ++ct;
             int x,r,c;
             cin>>x>>r>>c;
             int f=0;
             if(x==1)
                f=1;
             else if(x==2)
             {
                 if(r%2==0 || c%2==0)
                    f=1;
             }
             else
                {
                    if(r>=(x-1) && c>=(x-1) && (r*c)%x==0)
                    f=1;
             }
             printf("Case #%d: ",ct);
             if(f)
                printf("GABRIEL\n");
                else
                    printf("RICHARD\n");
         }


           return 0;
}

