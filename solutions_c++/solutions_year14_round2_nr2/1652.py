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
using namespace std;

#define FOR(i,a,b) for(int i=a;i<b;++i)
#define REP(i,n) FOR(i,0,n)
#define RFOR(i,a,b) for(int i=a;i>=b;i--)
#define RREP(i,n) RFOR(i,n-1,0)
#define ECH(it, v) for(auto it=v.begin();it!=v.end();++it)
#define ALL(x) (x).begin(),(x).end()
#define CLR(x) memset(x,0,sizeof(x))
#define SET(x) memset(x,-1,sizeof(x))
#define MOD 1000000007
typedef long long LL;
typedef unsigned int UI;
typedef unsigned long long UL;
typedef vector<int> VI;
typedef vector<vector<int>> VVI;
typedef vector<string> VS;

int main() {
    #ifdef raaja
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif
    int zz, qq= 0;
    scanf("%d", &zz);
    int a, b, k;
    while(qq++ < zz) {
        cin>>a>>b>>k;
        int mn = min(a, b), mx = max(a, b);
        int ret = 0;
        REP(i, a) REP(j, b) if((i&j) < k) ret++;
        cout<<"Case #"<<qq<<": "<<ret<<endl;
    }
    return 0;
    while(qq++ < zz) {
        cin>>a>>b>>k;
        int mn = min(a, b), mx = max(a, b);
        LL ret = 0;
        REP(i, k) {
            LL tt = 1;
            if(i>a || i>b) break;
            REP(j, 31) {
                if(k & (1<<j));
                else {
                    //if(a>>(j+1) == )
                    tt *= 3;
                }
            }
            ret += tt;
        }
        cout<<"Case #"<<qq<<": "<<ret<<endl;
    }
}
