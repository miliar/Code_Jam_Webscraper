#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <memory.h>
#include <vector>

#define f first
#define s second
#define pb push_back

using namespace std;

int t;
vector<int> v , v2;

int main()
{
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);

    scanf("%d",&t);
    for (int k = 1; k <= t; k++) {
        int x , n , m;
        scanf("%d",&n);
        for (int i = 1; i <= 4; i++) {
            for (int j = 1; j <= 4; j++) {
                scanf("%d",&x);
                if (i == n)
                    v.pb(x);
            }
        }
        scanf("%d",&m);
        for (int i = 1; i <= 4; i++) {
            for (int j = 1; j <= 4; j++) {
                scanf("%d",&x);
                if (m == i) v2.pb(x);
            }
        }
        int cnt = 0 , ans;
        for (int i = 0; i < (int)v.size(); i++) {
            for (int j = 0; j < (int)v2.size(); j++) {
                if (v[i] == v2[j])
                    cnt++,
                    ans = v[i];
            }
        }
        printf("Case #%d: ",k);
        if (cnt > 1) printf("Bad magician!\n");
        else if (cnt == 0) printf("Volunteer cheated!\n");
        else printf("%d\n",ans);
        v.clear(); v2.clear();
    }

    return 0;
}
