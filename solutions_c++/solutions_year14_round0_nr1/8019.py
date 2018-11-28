#include <stdio.h>

int v1[4], v2[4];

FILE* in;

void read_matrix(int* a) {
    int row = 4;
    fscanf(in, "%d", &row);
    row--;
    for (int i=0; i<4; ++i) {
        for (int j=0; j<4; ++j) {
            int tmp;
            fscanf(in, "%d", &tmp);
            if (i==row) {
                a[j] = tmp;
            }
        }
    }
}

void cmp() {
    int ret = -1;
    for (int i=0; i<4; ++i) {
        for (int j=0; j<4; ++j) {
            if (v1[i] == v2[j]) {
                if (ret == -1) {
                    ret = v1[i];
                }
                else {
                    printf("Bad magician!\n");
                    return;
                }
            }
        }
    }

    if (ret == -1) {
        printf("Volunteer cheated!\n");
    }
    else  {
        printf("%d\n", ret);
    }
}

int main() {
    int T;
    in = fopen("in.in", "r");
    fscanf(in, "%d", &T);
    for (int t=0; t<T; ++t) {
        printf("Case #%d: ", t+1);
        read_matrix(v1);
        read_matrix(v2);
        cmp();
    }

    return 0;
}
