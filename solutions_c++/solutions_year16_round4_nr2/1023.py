/*
 * =====================================================================================
 *
 *       Filename: B
 *
 *    Description:
 *
 *        Version:  1.0
 *        Created:  2016-05-28-21.10.16, Saturday
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:
 *
 *   ________                          ___.
 *  /  _____/_____   __ ______________ \_ |__
 * /   \  ___\__  \ |  |  \_  __ \__  \ | __ \
 * \    \_\  \/ __ \|  |  /|  | \// __ \| \_\ \
 *  \______  (____  /____/ |__|  (____  /___  /
 *         \/     \/                  \/    \/
 *
 *   Organization:  Shahjalal University of Science and Technology
 *
 * =====================================================================================
 */

#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <cstdio>
#include <climits>
#include <vector>
#include <cstring>
#include <cstdlib>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <iostream>
#include <algorithm>

using namespace std;

typedef long long Long;
typedef double DD;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int, int> PII;
typedef pair<Long, Long> PLL;
typedef vector<PII> VPII;
typedef vector<PLL> VPLL;
typedef vector<string> VS;
typedef vector<DD> VD;
typedef vector<Long> VL;
typedef vector<VL> VVL;

const int INF = 2000000000;
const int MOD = 1000000007;
const Long L_MAX = 9223372036854775807;
const int I_MAX = 2147483647;


#define sf scanf
#define pf printf
#define mem(a,b)          memset(a,b,sizeof(a))
#define pb push_back
#define REP(i,a,b)        for(int i=a; i<=b; ++i)
#define REPI(i,a,b,c)     for(int i=a; i<=b; i+=c)
#define REPR(i,a,b)       for(int i=b; i>=a; --i)
#define REPRD(i,a,b,c)    for(int i=b; i>=a; i-=c)
#define REPB(i,a)         for(int i=a; ;i++)
#define REPRB(i,a)        for(int i=a; ; i--)
#define mp(a,b)   make_pair(a,b)
#define fs        first
#define sc        second
#define SZ(s)     ((int)s.size())
#define PI        3.141592653589793
#define lim       1007
#define tlim      (1<<((int)ceil(log2(lim))+1))
#define unq(vec)  stable_sort(vec.begin(),vec.end());\
				  vec.resize(distance(vec.begin(),unique(vec.begin(),vec.end())));
#define BE(a)     a.begin(),a.end()
#define rev(a)    reverse(BE(a))
#define sorta(a)  stable_sort(BE(a))
#define sortc(a, comp)  sort(BE(a),comp)

//int X[]={1,1,2,2,-1,-1,-2,-2},Y[]={2,-2,1,-1,2,-2,1,-1};//knight move
//int X[]={0,-1,-1,-1,0,1,1,1},Y[]={-1,-1,0,1,1,1,0,-1};//8 move
//int X[]={-1,0,1,0},Y[]={0,1,0,-1};//4 move

int main(int argc, const char **argv) {
    //ios::sync_with_stdio(false);
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
    int Test;
    cin>>Test;
    REP(kase,1,Test) {
        int n,k;
        cin>>n>>k;
        DD p[n];
        REP(i,0,(n-1)) {
            cin>>p[i];
        }
        DD mx=0;
        REP(i,0,((1<<n)-1)) {
            if(__builtin_popcount(i)==k) {
                DD sum=0.0;
                VI v;
                REP(j,0,(n-1)) {
                    if(i&(1<<j)) {
                        v.pb(j);
                    }
                }
                REP(j,0,((1<<k)-1)) {
                    if(__builtin_popcount(j)==(k/2)) {
                        DD x=1.0;
                        REP(l,0,(k-1)) {
                            if(j&(1<<l))x*=p[v[l]];
                            else x*=(1.0-p[v[l]]);
                        }
                        sum+=x;
                    }
                }
                mx=max(mx,sum);
            }
        }
        cout<<"Case #"<<kase<<": "<<fixed<<setprecision(8)<<mx<<"\n";
    }
    //double st=clock(),en;
    //en=clock();
    //cerr<<(double)(en-st)/CLOCKS_PER_SEC<<endl;
    return 0;
}



