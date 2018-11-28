#include <cstdio>
#include <cstdlib>


int main(int argc, char **argv) {
    int T;
    bool mark[16];
    FILE* fin = fopen(argv[1], "r");
    FILE* fout = fopen("ans.txt", "w");
    fscanf(fin, "%d", &T);
    for (int t = 0; t < T; t++) {
        for (int i = 0; i < 16; i++) mark[i] = true;
        for (int a = 0; a < 2; a++) {
            int ans;
            fscanf(fin, "%d", &ans);
            for (int i = 0; i < 4; i++) {
                for (int j = 0; j < 4; j++) {
                    int num;
                    fscanf(fin, "%d", &num);
                    if (i != ans-1) {
                        mark[num-1] = false;
                    }
                }
            }
        }
        bool flag = false;
        bool flag2 = true;
        int j;
        for (int i = 0; i < 16; i++) {
            if (mark[i]) {
                if (flag) {
                    fprintf(fout, "Case #%d: Bad magician!\n", t+1);
                    flag2 = false;
                    break;
                }else {
                    flag = true;
                    j = i;
                }
            }
        }
        if (flag2) {
            if (flag) {
                fprintf(fout, "Case #%d: %d\n", t+1, j+1);
            }else {
                fprintf(fout, "Case #%d: Volunteer cheated!\n", t+1);
            }
        }
    }

    return 0;
}

    

