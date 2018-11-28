#include<stdio.h>
#include<algorithm>
#include<string.h>
using namespace std;

int n,m;
char s[10010];
const int T[4][4] = {{0,1,2,3},
                     {1,4,3,6},
                     {2,7,4,1},
                     {3,2,5,4}};

int a[10010], b[10010];

int mul(int id1, int id2) {
    int x = T[id1 % 4][id2 % 4];
    if ((id1>=4) != (id2>=4)) 
        x = (x >= 4) ? (x - 4) : (x + 4);
    return x;
}

int main() {
    int tca; scanf("%d", &tca);
    for (int ca=0; ca<tca; ca++){
        scanf("%d%d", &n, &m);
        scanf("%s", s);
        int id = 0;
        for (int i = 0; i < n; i++) {
            int cid = (s[i]-'i'+1);
            id = mul(id, cid);
        }
        bool ans = false;

        int all = 0;
        if (m % 2 == 1) 
            all = mul(all, id);

        int r = mul(id, id);
        if ((m / 2) % 2 != 0 && (m / 2 > 0))
            all = mul(all, r);

        if (all == 4) {
            memset(a, -1, sizeof(a));
            memset(b, -1, sizeof(b));
            for (int i = 0, now = 0; i < n; i++) {
                int cid = (s[i]-'i'+1);
                now = mul(now, cid);
                if (now == 1)
                    a[i] = 0;
                int t = now;
                for (int j = 1; j <= 10 && a[i]==-1; j++) {
                    t = mul(id, t);
                    if (t == 1) 
                        a[i] = j;
                }
                if (i > 0) {
                    if (a[i]==-1) a[i]=a[i-1];
                    else if (a[i-1]!=-1) a[i]=min(a[i], a[i-1]);
                }
            }
            for (int i = n-1, now = 0; i >= 0; i--) {
                int cid = (s[i]-'i'+1);
                now = mul(now, cid);
                if (now == 3)
                    b[i] = 0;
                int t = now;
                for (int j = 1; j <= 10 && b[i]==-1; j++) {
                    t = mul(t, id);
                    if (t == 3) 
                        b[i] = j;
                }
                if (i < n-1) {
                    if (b[i]==-1) b[i]=b[i+1];
                    else if (b[i+1]!=-1) b[i]=min(b[i], b[i+1]);
                }
            }
            for (int i = 1; i < n; i++){
                if (a[i-1]!=-1 && b[i]!=-1 && a[i-1] + b[i] + 1 <= m) ans = true;
            }
            if (a[n-1]!=-1 && b[0]!=-1 && a[n-1] + b[0] + 2 <= m) ans = true;


//            for (int i =0 ; i < n; i++) printf("%d ", a[i]); puts("");
//            for (int i =0 ; i < n; i++) printf("%d ", b[i]); puts("");
        }
        printf("Case #%d: %s\n", ca+1, ans?"YES":"NO");
    }
    return 0;
}
