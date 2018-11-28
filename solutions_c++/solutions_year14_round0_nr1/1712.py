#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
#include <stack>
#include <queue>
#include <set>
#include <string>

using namespace std;

int tcase,mark[17],a[3],r[5];

int main() {
    freopen("A-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);

    scanf("%d",&tcase);

    for (int tid=1; tid<=tcase; ++tid) {
        for (int i=1; i<=16; ++i) mark[i]=0;

        for (int n=1; n<=2; ++n) {
            scanf("%d",&a[n]);

            for (int i=1; i<=4; ++i)
                for (int j=1; j<=4; ++j) {
                    scanf("%d",&r[j]);
                    if (i==a[n]) ++mark[r[j]];
                }
        }

        int res=-1;
        for (int i=1; i<=16; ++i)
            if (mark[i]==2) {
                if (res==-1)
                    res=i;
                else {
                    res=-2;
                    break;
                }
            }

        if (res==-2)
            printf("Case #%d: Bad magician!\n",tid);
        else if (res==-1)
            printf("Case #%d: Volunteer cheated!\n",tid);
        else printf("Case #%d: %d\n",tid,res);
    }

    return 0;
}
