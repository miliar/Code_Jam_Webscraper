#include <cstdio>
#include <set>
#include <algorithm>
#include <vector>
using namespace std;
const int RN = 4;
int tn, ti, a1, a2, x;

int main()
{
    scanf("%d", &tn);
    for (ti=1; ti<=tn; ++ti) {
        scanf("%d", &a1);
        set<int> rs[RN], cs[RN];
        vector<int> res;
        for (int i=0; i<RN*RN; ++i) {
            scanf("%d", &x);
            rs[i/RN].insert(x);
        }
        scanf("%d", &a2);
        for (int i=0; i<RN*RN; ++i) {
            scanf("%d", &x);
            cs[i/RN].insert(x);
        }
        --a1; --a2;
        res.resize(RN);
        res.resize(set_intersection(
                    rs[a1].begin(), rs[a1].end(), cs[a2].begin(), cs[a2].end(), res.begin()
                    ) - res.begin());
        switch(res.size()) {
            case 0: printf("Case #%d: Volunteer cheated!\n", ti); break;
            case 1: printf("Case #%d: %d\n", ti, *res.begin()); break;
            default: printf("Case #%d: Bad magician!\n", ti); break;
        }
    }
}
