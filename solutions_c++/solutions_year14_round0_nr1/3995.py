#include <cstdio>
#include <cstdlib>

int main() {
    int T, iter;
    FILE *in = fopen("input", "r"), *out = fopen("output", "w");
    int a[4], b[4], i, j;
    int mat0[16], mat1[16], count, num;
    int r0, r1;
    fscanf(in, "%d", &T);
    for(iter = 0; iter < T; iter++) {
        fscanf(in, "%d", &r0);
        for(i = 0; i < 4; i++) {
            fscanf(in, "%d %d %d %d", mat0 + i * 4, mat0 + i * 4 + 1, mat0 + i * 4 + 2, mat0 + i * 4 + 3);
        }
        fscanf(in, "%d", &r1);
        for(i = 0; i < 4; i++) {
            fscanf(in, "%d %d %d %d", mat1 + i * 4, mat1 + i * 4 + 1, mat1 + i * 4 + 2, mat1 + i * 4 + 3);
        }
        for(i = 0; i < 4; i++){
            a[i] = mat0[0 + i + (r0 - 1) * 4];
            b[i] = mat1[0 + i + (r1 - 1) * 4];
        }
        count = 0;
        for(i = 0; i < 4; i++)
            for(j = 0; j < 4; j++) {
                if(a[i] == b[j]){
                    count++;
                    num = a[i];
                }
        }
        fprintf(out, "Case #%d: ", iter + 1);
        if(count == 1) {
            fprintf(out, "%d\n", num);
        }
        else if(count == 0) {
            fprintf(out, "Volunteer cheated!\n");
        }
        else {
            fprintf(out, "Bad magician!\n");
        }
    }
    fclose(in);
    fclose(out);
    return 0;
}
