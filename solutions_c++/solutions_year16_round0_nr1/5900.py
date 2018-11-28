#include <set>
#include <map>
#include <cstdio>
#include <vector>
#include <cstring>
#include <algorithm>
using namespace std;
#define mp make_pair
#define pb push_back
#define INF 0x3f3f3f3f
#define ABS(x) ((x)>0?(x):(-(x)))
#define sqr(x) ((x)*(x))
#define rep(i,n) for (lld i=1; i<=(n); i++)
#define For(i,s,t) for (lld i=(s); i<=(t); i++)
#define FOR(i,s,t) for (lld i=(s); i>=(t); i--)
#define foreach(it,v) for (__typeof((v).begin()) it=(v).begin(); it!=(v).end(); it++)
typedef long long lld;
typedef pair<int,int> pii;

lld n,digits;
bool a[20];

void CountDigit(lld x) {
    while (x) {
        if (!a[x%10]) {
            a[x%10]=true;
            digits++;
        }
        x/=10;
    }
}

int main() {
#ifndef ONLINE_JUDGE
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
#endif
    lld cas; scanf("%lld",&cas);
    rep(cs,cas) {
        scanf("%lld",&n);
        printf("Case #%lld: ",cs);
        if (n==0) {
            printf("INSOMNIA\n");
        }
        else {
            lld x=0;
            digits=0;
            memset(a,false,sizeof(a));
            while (digits<10) {
                x+=n;
                CountDigit(x);
            }
            printf("%lld\n",x);
        }
    }
    return 0;
}
