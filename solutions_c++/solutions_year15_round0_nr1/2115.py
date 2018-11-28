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
int sm;
char s[1003];
int main(){
    int tc;
    sc1(tc);
    FOR(itc,1,tc+1){
        sc1(sm);
        scanf("%s",s);
        int res = 0;
        int sum = 0;
        FN(i,sm+1){
            if( sum < i){
                res += (i-sum);
                sum = i;
            }
            sum+= s[i] - '0';
        }
        printf("Case #%d: %d\n",itc,res);
    }
}

