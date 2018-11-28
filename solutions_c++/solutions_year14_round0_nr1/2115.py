#include <cstdio>
#include <vector>

using namespace std;
vector<int> andSet;

int T, a, b, conA[4][4], conB[4][4];

int main() {
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);

    scanf("%d", &T);

    for (int test = 0; test < T; test++) {
        andSet = vector<int>();

        scanf("%d", &a); a--;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                scanf("%d", &conA[i][j]);
            }
        }

        scanf("%d", &b); b--;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                scanf("%d", &conB[i][j]);
            }
        }

        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                if (conA[a][i] == conB[b][j]) {
                    andSet.push_back(conA[a][i]);
                }
            }
        }

        if (andSet.size() == 1) printf("Case #%d: %d\n", test + 1, andSet[0]);
        else if (andSet.size() == 0) printf("Case #%d: Volunteer cheated!\n", test + 1);
        else printf("Case #%d: Bad magician!\n", test + 1);
    }
}
