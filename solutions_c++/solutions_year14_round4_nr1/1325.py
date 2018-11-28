#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <vector>
using namespace std;

#define snuke(it,x) for (__typeof((x).begin()) it = (x).begin(); it != (x).end(); it ++)
#define mp make_pair
#define pb push_back
typedef long long lld;

const int M = 777;
int n,m,cnt[777];

int work() {
        int ret = cnt[m];
        for (int i = m-1; i >= 1; i --) {
                while (cnt[i]) {
                        cnt[i] --;
                        ret ++;
                        for (int j = min(i,m-i); j >= 1; j --) {
                                if (cnt[j]) {
                                        cnt[j] --;
                                        break;
                                }
                        }
                }
        }
        return ret;
}

int main() {
        freopen("in.txt","r",stdin);
        freopen("out.txt","w",stdout);

        int cas,ca = 0;
        scanf("%d",&cas);
        while (cas--) {
                scanf("%d%d",&n,&m);
                memset(cnt,0,sizeof(cnt));
                for (int i = 0; i < n; i ++) {
                        int x;
                        scanf("%d",&x);
                        cnt[x] ++;
                }
                printf("Case #%d: %d\n",++ca,work());
        }
        return 0;
}
