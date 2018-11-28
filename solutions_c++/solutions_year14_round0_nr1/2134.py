#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#include<algorithm>
#include<set>
#include<map>
#include<utility>
#include<vector>
#include<string>
#include<stack>
#include<queue>
using namespace std;
int cnt[17];
vector < int > ans;
int main()
{
    //freopen("data.txt", "r", stdin);
    freopen("Ain.txt", "r", stdin);
    freopen("Aout.txt", "w", stdout);
    int t,T;
    int r1,r2,i,j,x;
    scanf("%d", &T);
    for (t=1; t<=T; ++t)
    {
        memset(cnt, 0, sizeof(cnt));
        ans.clear();
        scanf("%d", &r1);
        for (i=1; i<=4; ++i)
        {
            for (j=1; j<=4; ++j)
            {
                scanf("%d", &x);
                if (i == r1) ++cnt[x];
            }
        }
        scanf("%d", &r2);
        for (i=1; i<=4; ++i)
        {
            for (j=1; j<=4; ++j)
            {
                scanf("%d", &x);
                if (i == r2) ++cnt[x];
            }
        }
        for (i=1; i<=16; ++i)
        {
            if (cnt[i] == 2) ans.push_back(i);
        }
        printf("Case #%d: ", t);
        if (ans.size() == 0) puts("Volunteer cheated!");
        else if (ans.size() > 1) puts("Bad magician!");
        else printf("%d\n", ans[0]);
    }
    return 0;
}
