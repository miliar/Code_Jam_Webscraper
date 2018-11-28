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
               int c=0;
               while(tc--)
               {
                   ++c;
                   int n;
                   cin>>n;
                   string s;
                   cin>>s;
                   int l;

                     int ans=0,sum=0,val;

                   FOR(i,0,n)
                    {
                        if(sum<i)
                            {
                                val=i-sum;
                                ans+=val;
                                sum+=val;
                            }
                        sum+=(s[i]-'0');
                    }


                      printf("Case #%d: %d\n",c,ans);

               }

           return 0;
}

