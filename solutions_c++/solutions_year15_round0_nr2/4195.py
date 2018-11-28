#include <stdio.h>
#include <string>
#include <string.h>
using namespace std;

int T, d;
int p[1001];

int main()
{
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);

    int cas = 1;

    scanf("%d", &T);

    while(T--) {
        int mxn = 0;

        scanf("%d", &d);
        for(int i = 1; i <= d; i++) {
            scanf("%d", &p[i]);
            mxn = max(mxn, p[i]);
        }

        int ans = 2000;
        for(int i = 1; i <= mxn; i++) {
            int sum = 0;
            for(int j = 1; j <= d; j++) {
                if(p[j] > i) sum += (p[j] - 1) / i;
            }
            ans = min(ans, sum + i);
        }
        printf("Case #%d: %d\n", cas++, ans);

    }
    return 0;
}