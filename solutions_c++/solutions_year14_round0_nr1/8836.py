#include <cstdio>

int main() {
    int d;
    scanf("%d", &d);
    for (int t_nr = 1; t_nr <= d; ++t_nr) {
        bool jest[17];
        for (int i = 1; i <= 16; ++i) jest[i] = 1;
        for (int i = 0; i < 2; ++i) {
            int w, t[5][5];
            scanf("%d", &w);
            for (int j = 1; j <= 4; ++j) {
                for (int k = 1; k <= 4; ++k) {
                    scanf("%d", &t[j][k]);
                    if (j != w) jest[t[j][k]] = 0;
                }
            }
        }
        int ile = 0, wyn;
        for (int i = 1; i <= 16; ++i) if (jest[i]) ++ile, wyn = i;
        printf("Case #%d: ", t_nr);
        if (ile == 0) printf("Volunteer cheated!\n");
        else if (ile == 1) printf("%d\n", wyn);
        else printf("Bad magician!\n");
    }
}
