#include <cmath>
#include <ctime>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <functional>
#include <algorithm>
#include <iostream>
#include <numeric>
#include <iomanip>
#include <sstream>
#include <bitset>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <list>
#include <set>
#include <map>
using namespace std;

#define debug(args...) fprintf(stderr,args)
#define foreach(_it,_v) for(typeof(_v.begin()) _it = _v.begin(); _it != _v.end(); ++_it)

typedef long long lint;
typedef pair<int,int> pii;
typedef pair<lint,lint> pll;

const int INF = 0x3f3f3f3f;
const lint LINF = 0x3f3f3f3f3f3f3f3fll;

lint n,p;

lint maxpos(lint i) {
    lint mask = 0;
    int at = n-1;
    lint q = i;
    while(q) {
        q = (q-1)/2;
        mask ^= (1ll<<at);
        --at;
    }
    return mask+1;
}        

int main() {
    int T;
    scanf("%d",&T);
    for(int _t = 1;_t <= T;++_t) {
        printf("Case #%d: ",_t);
        scanf("%lld%lld",&n,&p);
        lint total = (1ll<<n);
        lint i = 0;
        while((1ll<<(i+1)) <= p) ++i;
        lint ans2 = (1ll<<n) - (1ll<<(n-i));
        lint l=0,r=(1ll<<n)-1;
        while(l<r) {
            lint mid = (l+r+1)/2;
            if(maxpos(mid) <= p) l = mid;
            else r = mid-1;
        }
        printf("%lld %lld\n",l,ans2);
    }
    return 0;
}
