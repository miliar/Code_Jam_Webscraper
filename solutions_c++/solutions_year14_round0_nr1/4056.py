#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
int main()
{
    int i, j, k, n, m, t, a, b, count, l;
    cin >> t;
    int mat1[10][10];
    int mat2[10][10];
    int v[25];
    FILE *fp = fopen("out.txt", "w");
    for (k = 1; k <= t; k++) {
        cin >> a;
        memset(v, 0, sizeof(v));
        for (i = 0; i < 4; i++) {
            for (j = 0; j < 4; j++) {
                cin >> mat1[i][j];
                if (i+1 == a) {
                    v[mat1[i][j]]++;
                }
            }
        }
        cin >> b;
        for (i = 0; i < 4; i++) {
            for (j = 0; j < 4; j++) {
                cin >> mat2[i][j];
                if (i + 1 == b) {
                    v[mat2[i][j]]++;
                }
            }
        }
        count = 0;
        for (i = 1; i <= 16; i++) {
            if (v[i] >= 2) {
                count++;
                l = i;
            }
        }
        if (count == 1) {
            fprintf(fp, "Case #%d: %d\n", k, l);
            //cout << "Case #" << k << ": "  << l << endl;
        }
        else if (count > 1) {
            fprintf(fp, "Case #%d: Bad magician!\n", k);
            //cout << "Case #" << k << ": " << "Bad magician!" << endl;
        }
        else {
            fprintf(fp, "Case #%d: Volunteer cheated!\n", k);
            //cout << "Case #" << k << ": " << "Volunteer cheated!" << endl;
        }

    }
    fclose(fp);
    return 0;
}
