#include <stdlib.h>
#include <stdio.h>

int data[101][101];

int current[101][101];

int height;
int width;

const char* judge() {
    for (int y = 0; y < height; y++) {
        int max = data[y][0];
        for (int x = 1; x < width; x++) {
            if (data[y][x] > max) {
                max = data[y][x];
            }
        }
        for (int x = 0; x < width; x++) {
            current[y][x] = max;
        }
    }
    for (int x = 0; x < width; x++) {
        int max = data[0][x];
        for (int y = 1; y < height; y++) {
            if (data[y][x] > max) {
                max = data[y][x];
            }
        }
        for (int y = 0; y < height; y++) {
            if (current[y][x] > max) {
                current[y][x] = max;
            }
        }
    }

    for (int y = 0; y < height; y++) {
        for (int x = 0; x < width; x++) {
            if (current[y][x] != data[y][x]) {
                return "NO";
            }
        }
    }
    return "YES";
}
int main()
{
    FILE *in = fopen("e:\\codejam\\in.txt", "rw");
    FILE *out = fopen("e:\\codejam\\out.txt", "w");
    int n = 0;
    fscanf(in, "%d", &n);
    for (int caseIndex = 0; caseIndex < n; caseIndex++) {
        fscanf(in, "%d %d", &height, &width);
        for (int y = 0; y < height; y++) {
            for (int x = 0;  x < width; x++) {
                fscanf(in, "%d", &data[y][x]);
            }
        }

        fprintf(out, "Case #%d: ", caseIndex + 1);
        fprintf(out, "%s\n", judge());
    }
    return 0;
}
