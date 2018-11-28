#include <vector>
#include <cstdio>

using namespace std;

int main(int argc, char *argv[]) {
    FILE *in = fopen("A-small-attempt2.in", "r");
    FILE *out = fopen("QualA.out", "w");

    int T;
    fscanf(in, "%d", &T);

    int testCase;
    for (testCase = 0; testCase < T; testCase++) {
        int R1, R2;
        vector <int> firstRow;

        fscanf(in, "%d", &R1);
        int row = 1;
        while (row <= 4) {
            int a, b, c, d;
            fscanf(in, "%d %d %d %d", &a, &b, &c, &d);

            if (row == R1) {
                firstRow.push_back(a);
                firstRow.push_back(b);
                firstRow.push_back(c);
                firstRow.push_back(d);
            }

            ++row;
        }

        vector <int> secondRow;

        fscanf(in, "%d", &R2);
        row = 1;
        while (row <= 4) {
            int a, b, c, d;
            fscanf(in, "%d %d %d %d", &a, &b, &c, &d);

            if (row == R2) {
                secondRow.push_back(a);
                secondRow.push_back(b);
                secondRow.push_back(c);
                secondRow.push_back(d);
            }

            ++row;
        }

        int possible = 0, result = 0;
        int i, k;
        for (i = 0; i < firstRow.size(); i++) {
            for (k = 0; k < secondRow.size(); k++) {
                if (firstRow[i] == secondRow[k]) {
                    ++possible;
                    result = firstRow[i];
                }
            }
        }

        if (possible < 1) {
            fprintf(out, "Case #%d: Volunteer cheated!\n", testCase + 1);
        } else if (possible > 1) {
            fprintf(out, "Case #%d: Bad magician!\n", testCase + 1);
        } else {
            fprintf(out, "Case #%d: %d\n", testCase + 1, result);
        }
    }

    fclose(in);
    fclose(out);
}