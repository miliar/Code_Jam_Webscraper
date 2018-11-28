#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
#include <string>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <climits>
#include <cctype>
#define SZ(x) ( (int) (x).size() )
#define me(x,a) memset(x,a,sizeof(x))
#define FN(a,n) for(int a=0;a<n;a++)
#define FOR(a,ini,fin) for(int a=(ini);a<(fin);a++)
#define sc1(x) scanf("%d",&x)
#define sc2(x,y) scanf("%d %d",&x,&y)
#define sc3(x,y,z) scanf("%d %d %d",&x,&y,&z)
#define all(v) v.begin(),v.end()
#define pb push_back
#define mp make_pair
#define pii pair<int,int>
#define F first
#define S second
#define endl "\n"
#define MOD 1000000007
#define MAXN 100005
typedef long long LL;
typedef unsigned long long ULL;
using namespace std;
int D;
int p[1003];
bool isP(int m){
    for( int c = 0; c<m; c++){
        int sum = 0;
        FN(i,D){
            sum+=(p[i]-1)/(m-c);
        }
        if( sum <= c) return true;
    }
    return false;
}
int main(){
    int tc;
    sc1(tc);
    FOR(itc,1,tc+1){
        sc1(D);
        FN(i,D) sc1(p[i]);
        int lo = 0, hi = 1000;
        while( lo != hi-1){
            int med = (lo+hi)>>1;
            if( isP(med) ) hi = med;
            else lo = med;
        }        
        printf("Case #%d: %d\n",itc,hi);
    }
}

