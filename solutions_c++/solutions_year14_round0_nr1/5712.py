#include<cstdio>
#include<algorithm>
#include<cstdlib>
#include<vector>
using namespace std;

int T, ans1, q2, gr1[4][4], gr2[4][4];

int main() {
    scanf("%d", &T);
    for (int t=1; t<=T; t++) {
        scanf("%d",&ans1);
        for (int i=0; i<4; i++) {
            for (int j=0; j<4; j++) {
                scanf("%d",&gr1[i][j]);
            }
        }
        scanf("%d",&q2);
        for (int i=0; i<4; i++) {
            for (int j=0; j<4; j++) {
                scanf("%d", &gr2[i][j]);
            }
        }
        ans1--;
        q2--;
        sort(gr1[ans1], gr1[ans1]+4);
        sort(gr2[q2], gr2[q2]+4);
        vector<int> V(4);
        vector<int>::iterator it = set_intersection(gr1[ans1], gr1[ans1]+4,
                                                    gr2[q2], gr2[q2]+4,
                                                    V.begin());
        V.resize(it-V.begin());
        if (V.size() > 1) {
            printf("Case #%d: Bad magician!", t);
        } else if (V.size() == 0) {
            printf("Case #%d: Volunteer cheated!", t);
        } else {
            printf("Case #%d: %d", t, V[0]);
        }
        printf("\n");
    }
    return 0;
}
