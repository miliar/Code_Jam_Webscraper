#include <cstdio>

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 0; t ++< T;) {
        int row, a, b, c, d, z, pos[4] = {}, cad[4] = {}, def[4] = {}, k = 0;
        scanf("%d", &row);
        for (int i = 0; i < row; i++)
            for (int j = 0; j < 4; j++)
                scanf("%d", &pos[j]);
        for (int i = row; i < 4; i++)
            scanf("%d%d%d%d", &z, &z, &z, &z);
        scanf("%d", &row);
        for (int i = 0; i < row; i++)
            for (int j = 0; j < 4; j++)
                scanf("%d", &cad[j]);
        for (int i = row; i < 4; i++)
            scanf("%d%d%d%d", &z, &z, &z, &z);
        for (int i = 0; i < 4; i++)
            for (int j = 0; j < 4; j++)
                if (pos[i] == cad[j])
                    def[k++] = pos[i];
        printf("Case #%d: ", t);
        if (k == 0)
            printf("Volunteer cheated!\n");
        else if (k == 1)
            printf("%d\n", def[0]);
        else
            printf("Bad magician!\n");
    }
}
