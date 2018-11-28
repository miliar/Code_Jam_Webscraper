#include <set>
#include <algorithm>
#include <cstdio>
#include <vector>

using namespace std;

int main()
{
    freopen("magician.in", "r", stdin);
    freopen("magician.out", "w", stdout);
    int t;
    scanf("%d", &t);
    for(int x = 1; x <= t; x++) {
        int ans1, ans2;
        int* m1 = new int[4];
        int* m2 = new int[4];
        int tmp_l;
        scanf("%d", &ans1);
        for(int i = 0; i < 4; i++)
            for(int j = 0; j < 4; j++) {
                scanf("%d", &tmp_l);
                if(i == ans1 - 1) m1[j] = tmp_l;
            }
        scanf("%d", &ans2);
        for(int i = 0; i < 4; i++)
            for(int j = 0; j < 4; j++) {
                scanf("%d", &tmp_l);
                if(i == ans2 - 1) m2[j] = tmp_l;
            }
        vector<int> sol;
        for(int i = 0; i < 4; i++)
            for(int j = 0; j < 4; j++)
                if(m1[i] == m2[j]) sol.push_back(m1[i]);
        if(sol.size() == 1) printf("Case #%d: %d\n", x, sol[0]);
        else if(sol.size() == 0) printf("Case #%d: Volunteer cheated!\n", x);
        else printf("Case #%d: Bad magician!\n", x);
    }
    return 0;
}
