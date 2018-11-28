#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <cmath>
#include <ctime>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <functional>
#include <bitset>
#include <utility>

using namespace std;

#define REP(i,n) for(int(i)=0;(i)<(int)(n);(i)++)
#define SZ(c) ((int)(c).size())
#define ITER(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();it++)
#define FIND(x,c) ((c).find((x))!=(c).end())
#define MP(x,y) make_pair((x),(y))

typedef long long ll;
const int INF=2147483647;
const int MOD=(int)1e9+7;
//const int MAX=
bool isp(int x) {
    char s[32];
    sprintf(s,"%d",x);
    int len=strlen(s);
    REP(i,len/2)
        if (s[i]!=s[len-1-i]) return false;
    return true;
}

int solve(int x) {
    int ret=0;
    for (int i=1; i*i<=x; i++) {
        if (isp(i) && isp(i*i))
            ret++;
    }
    return ret;
}

int main() {
    int T;
    scanf("%d",&T);
    REP(t,T) {
        int a,b;
        scanf("%d%d",&a,&b);
        printf("Case #%d: %d\n",t+1,solve(b)-solve(a-1));
    }
    return 0;
}
