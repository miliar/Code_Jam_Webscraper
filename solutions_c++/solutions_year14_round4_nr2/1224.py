#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <vector>
using namespace std;

#define snuke(it,x) for (__typeof((x).begin()) it = (x).begin(); it != (x).end(); it ++)
#define mp make_pair
#define pb push_back
typedef long long lld;

const int N = 11;
const int INF = 0x3f3f3f3f;
int n,a[N],p[N],b[N];


int work() {
        int ret = INF;
        for (int i = 0; i < n; i ++) p[i] = i;
        do {
                int cnt = 0;
                for (int i = 0; i < n; i ++) {
                        for (int j = 0; j < i; j ++) {
                                cnt += p[j]>p[i];
                        }
                }
                if (cnt>=ret) continue;
                for (int i = 0; i < n; i ++) {
                        b[p[i]] = a[i];
                }
                bool ok = true;
                bool down = false;
                for (int i = 0; i < n-1; i ++) {
                        if (b[i]<b[i+1]) {
                                if (down) ok = false;
                        } else {
                                down = true;
                        }
                }
                if (ok) ret = cnt;
        } while (next_permutation(p,p+n));
        return ret;
}

int main() {
        freopen("in.txt","r",stdin);
        freopen("out.txt","w",stdout);

        int cas,ca = 0;
        scanf("%d",&cas);
        while (cas--) {
                scanf("%d",&n);
                for (int i = 0; i < n; i ++) {
                        scanf("%d",a+i);
                }
                printf("Case #%d: %d\n",++ca,work());
        }
        return 0;
}
