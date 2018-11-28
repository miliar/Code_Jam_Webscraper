#include <iostream>
#include <cstdio>
#include <memory.h>
#define MAX(a,b) ((a) > (b) ? (a) : (b))
using namespace std;
const int maxn = 50;
long long map[maxn] = {1,4,9,121,484,10201,12321,14641,40804,44944,1002001,
1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521,
400080004,404090404,10000200001,10221412201,12102420121,12345654321,
40000800004,1000002000001,1002003002001,1004006004001,1020304030201,1022325232201,
1024348434201,1210024200121,1212225222121,1214428244121,1232346432321,
1234567654321,4000008000004,4004009004004
};

long long a,b;

int bis(long long val) {
    int l = 0,r = 39;
    while(l <= r) {
        int mid = (l + r) >> 1;
        if (map[mid] > val) r = mid - 1;
        else l = mid + 1;
    }
    return r;
}

void solve() {
    scanf("%lld %lld",&a,&b);
    int cnt = bis(b);
    cnt -= bis(a-1);
    printf("%d\n",cnt);
    return;
}

int main() {
    //freopen("in.txt","r",stdin);
    //freopen("B-large.in","r",stdin);
    //freopen("out.txt","w",stdout);
    int cas;
    scanf("%d",&cas);
    for (int i=1;i<=cas;i++) {
        printf("Case #%d: ",i);
        solve();
    }
    return 0;
}
