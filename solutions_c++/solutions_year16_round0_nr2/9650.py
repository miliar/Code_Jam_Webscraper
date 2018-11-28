#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int t;
char st[105];

int main()
{
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);

    scanf("%d",&t);
    for (int cs = 1; cs <= t; ++cs) {
        scanf("%s",&st);
        int l = strlen(st) , ans = 0;
        while (l > 0 && st[l - 1] == '+') --l;
        char cur;
        for (int i = 0; i < l; ++i) {
            if (i == 0) {
                cur = st[i];
            }
            else if (cur != st[i]) {
                ++ans;
                cur = st[i];
            }
        }
        if (l > 0)
            ++ans;
        printf("Case #%d: %d\n",cs,ans);
    }

    return 0;
}
