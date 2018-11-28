#include<cstdio>
#include<cstring>
#include<algorithm>
#include<iostream>
#include<string>
#include<vector>
#include<stack>
#include<bitset>
#include<cstdlib>
#include<cmath>
#include<set>
#include<list>
#include<deque>
#include<map>
#include<queue>
#define Max(a,b) ((a)>(b)?(a):(b))
#define Min(a,b) ((a)<(b)?(a):(b))
using namespace std;
typedef long long ll;
typedef long double ld;
const ld eps = 1e-9, PI = 3.1415926535897932384626433832795;
const int mod = 1000000000 + 7;
const int INF = 0x3f3f3f3f;
// & 0x7FFFFFFF
const int seed = 131;
const ll INF64 = ll(1e18);
const int maxn = 100 + 30;
int T,n,m;
char s[maxn];
int len, kase = 0;
int v[maxn];

int main() {
    freopen("B-small-attempt0.in", "r", stdin);
     freopen("out.txt", "w", stdout);

    int T; scanf("%d", &T);
    while(T--) {
        scanf("%s",s);
        int len = strlen(s);
        for(int i=0;i<len;i++)
            v[i] = s[i] == '+';
              // cout<<ans<<' ' <<' ' <<b<<endl;
        int tot = 0, pre = 0;
          // cout<<ans<<' ' <<' ' <<b<<endl;
        for(int i = len-1; i >= 0; --i) {
            int cur = (v[i] + pre) % 2;
              // cout<<ans<<' ' <<' ' <<b<<endl;
            if(cur == 0) {
                int j = i;
                  // cout<<ans<<' ' <<' ' <<b<<endl;
                while(j >= 0 && (v[j]+pre)%2 == 0)
                    --j;
                      // cout<<ans<<' ' <<' ' <<b<<endl;
                ++pre;
                  // cout<<ans<<' ' <<' ' <<b<<endl;
                ++tot;
                  // cout<<ans<<' ' <<' ' <<b<<endl;
                i = j+1;
                  // cout<<ans<<' ' <<' ' <<b<<endl;
            }
           // cout<<ans<<' ' <<' ' <<b<<endl;
        }

        printf("Case #%d: %d\n",++kase,tot);
    }
    return 0;
}
