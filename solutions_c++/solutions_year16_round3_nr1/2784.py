#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
int kase, n, cnt;
struct alpha {
    int id, p;
} al[66];
bool cmp(alpha a1, alpha a2) {
    return a1.p>a2.p;
}
int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &kase);
    for (int cas=1; cas<=kase; cas++) {
        cnt=0;
        memset(al, 0, sizeof(al));
        scanf("%d", &n);
        for (int i=0; i<n; i++) {
            al[i].id=i;
            scanf("%d", &al[i].p);
            cnt+=al[i].p;
        }
        printf("Case #%d:", cas);
        while (cnt>0) {
            sort(al, al+n, cmp);
            if (al[0].p==al[1].p&&al[2].p==0) {
                printf(" %c%c", al[0].id+'A', al[1].id+'A');
                cnt-=2;
                al[0].p--;
                al[1].p--;
            } else {
                printf(" %c", al[0].id+'A');
                al[0].p--;
                cnt--;
            }
        }
        puts("");
    }
    return 0;
}
