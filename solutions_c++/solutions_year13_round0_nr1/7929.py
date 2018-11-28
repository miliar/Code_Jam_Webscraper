#include <cstdio>
#include <windows.h>

int main()
{
    FILE *in = fopen("dataA.in", "r"), *out = fopen("dataA.out", "w");
    int T, casenum = 1;
    fscanf (in, "%d", &T);
    while (T--) {
        char arr[4][5];
        bool draw = true, win = false;
        for (int i = 0; i < 4; i++)
            fscanf (in, "%s", arr[i]);
        fprintf (out, "Case #%d: ", casenum++);
        for (int i = 0; i < 4; i++) {
            bool vert = true, horz = true;
            for (int j = 0; j < 3 && vert; j++)
                for (int k = j+1; k < 4 && vert; k++) {
                    vert &= (arr[j][i] == arr[k][i] || arr[j][i] == 'T' || arr[k][i] == 'T');
                }
            for (int j = 0; j < 3 && horz; j++)
                for (int k = j+1; k < 4 && horz; k++) {
                    horz &= (arr[i][j] == arr[i][k] || arr[i][j] == 'T' || arr[i][k] == 'T');
                }
            if (horz && arr[i][0] != '.' && arr[i][1] != '.') {
                draw = false;
                if (arr[i][0] != 'T') fprintf (out, "%c won\n", arr[i][0]);
                else fprintf (out, "%c won\n", arr[i][1]);
                win = true;
                break;
            }
            if (vert && arr[i][0] != '.' && arr[i][1] != '.') {
                draw = false;
                if (arr[0][i] != 'T') fprintf (out, "%c won\n", arr[0][i]);
                else fprintf (out, "%c won\n", arr[1][i]);
                win = true;
                break;
            }
        }
        if (!win) {
            bool left = true, right = true;
            for (int i = 0; i < 3 && left; i++)
                for (int j = i+1; j < 4 && left; j++) {
                    left &= (arr[i][i] == arr[j][j] || arr[i][i] == 'T' || arr[j][j] == 'T');
                }
            if (left && arr[0][0] != '.' && arr[1][1] != '.') {
                draw = false;
                if (arr[0][0] != 'T') fprintf (out, "%c won\n", arr[0][0]);
                else fprintf (out, "%c won\n", arr[1][1]);
                win = true;
            }
            for (int i = 0; i < 3 && right; i++)
                for (int j = i+1; j < 4 && right; j++) {
                    right &= (arr[3-i][i] == arr[3-j][j] || arr[3-i][i] == 'T' || arr[3-j][j] == 'T');
                }
            if (right && arr[3][0] != '.' && arr[2][1] != '.') {
                draw = false;
                if (arr[3][0] != 'T') fprintf (out, "%c won\n", arr[3][0]);
                else fprintf (out, "%c won\n", arr[2][1]);
                win = true;
            }
        }
        if (draw) {
            bool finished = true;
            for (int i = 0; i < 4 && finished; i++)
                for (int j = 0; j < 4 && finished; j++)
                    finished &= arr[i][j] != '.';
            if (finished) fprintf (out, "Draw\n");
            else fprintf (out, "Game has not completed\n");
        }
    }
    delete [] in, out;
    return 0;
}
