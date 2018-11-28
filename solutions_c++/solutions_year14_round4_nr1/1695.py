#include <iostream>
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

int n,x;
int cnt[703];

int main() {
    freopen("A-large.in","r",stdin);
    freopen("A.out","w",stdout);

    int tcase,fs,res,v;

    scanf("%d",&tcase);

    for (int tid=1; tid<=tcase; ++tid) {
        scanf("%d%d",&n,&x);

        for (int i=1; i<=700; ++i) cnt[i]=0;

        for (int i=1; i<=n; ++i) {
            scanf("%d",&fs);
            ++cnt[fs];
        }

        res=0; v=700;
        for (int i=1; i<=700; ++i)
            while (cnt[i]>0) {
                while (v>0) {
                    if (i+v<=x && cnt[v]>0) break;
                    --v;
                }

                ++res;
                --cnt[i];
                if (cnt[v]>0) --cnt[v];
            }

        printf("Case #%d: %d\n",tid,res);
    }

    return 0;
}
