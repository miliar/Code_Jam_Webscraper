#include <stdio.h>
#include <stdlib.h>

int main()
{
    int T = 0;//Test cases
    int v1 = 0;
    int v2 = 0;
    int c1[4][4];
    int c2[4][4];
    int j = 0;
    int k = 0;
    int r1 = 0;
    int r2 = 0;
    int r3 = 0;
    FILE *in = fopen("input.txt", "rt");
    FILE *out= fopen("output.txt", "wt");
    //FILE *in = fopen("A-small-attempt0.in", "rt");
    //FILE *out = fopen("A-small-attempt0.out", "wt");
    
    fscanf(in, "%d", &T);
    for(int i = 0; i < T; i++)
    {
        r1 = 0; r2 = 0; r3 = 0;
        v1 = 0; v2 = 0;
        c1[0][0] = c1[0][1] = c1[0][2] = c1[0][3] = 0;
        c1[1][0] = c1[1][1] = c1[1][2] = c1[1][3] = 0;
        c1[2][0] = c1[2][1] = c1[2][2] = c1[2][3] = 0;
        c1[3][0] = c1[3][1] = c1[3][2] = c1[3][3] = 0;
        c2[0][0] = c2[0][1] = c2[0][2] = c2[0][3] = 0;
        c2[1][0] = c2[1][1] = c2[1][2] = c2[1][3] = 0;
        c2[2][0] = c2[2][1] = c2[2][2] = c2[2][3] = 0;
        c2[3][0] = c2[3][1] = c2[3][2] = c2[3][3] = 0;

        fscanf(in, "%d", &v1);
        fscanf(in, "%d %d %d %d", &c1[0][0], &c1[0][1], &c1[0][2], &c1[0][3]);
        fscanf(in, "%d %d %d %d", &c1[1][0], &c1[1][1], &c1[1][2], &c1[1][3]);
        fscanf(in, "%d %d %d %d", &c1[2][0], &c1[2][1], &c1[2][2], &c1[2][3]);
        fscanf(in, "%d %d %d %d", &c1[3][0], &c1[3][1], &c1[3][2], &c1[3][3]);

        fscanf(in, "%d", &v2);
        fscanf(in, "%d %d %d %d", &c2[0][0], &c2[0][1], &c2[0][2], &c2[0][3]);
        fscanf(in, "%d %d %d %d", &c2[1][0], &c2[1][1], &c2[1][2], &c2[1][3]);
        fscanf(in, "%d %d %d %d", &c2[2][0], &c2[2][1], &c2[2][2], &c2[2][3]);
        fscanf(in, "%d %d %d %d", &c2[3][0], &c2[3][1], &c2[3][2], &c2[3][3]);

        // Array indices start from 0, adjust the input
        v1--;
        v2--;
        j = 0;
        k = 0;
        if (c1[v1][0] == c2[v2][0] ||
            c1[v1][0] == c2[v2][1] ||
            c1[v1][0] == c2[v2][2] ||
            c1[v1][0] == c2[v2][3])
        {
            r1++;
            r2 = c1[v1][0];
        }

        if (c1[v1][1] == c2[v2][0] ||
            c1[v1][1] == c2[v2][1] ||
            c1[v1][1] == c2[v2][2] ||
            c1[v1][1] == c2[v2][3])
        {
            r1++;
            r2 = c1[v1][1];
        }

        if (c1[v1][2] == c2[v2][0] ||
            c1[v1][2] == c2[v2][1] ||
            c1[v1][2] == c2[v2][2] ||
            c1[v1][2] == c2[v2][3])
        {
            r1++;
            r2 = c1[v1][2];
        }

        if (c1[v1][3] == c2[v2][0] ||
            c1[v1][3] == c2[v2][1] ||
            c1[v1][3] == c2[v2][2] ||
            c1[v1][3] == c2[v2][3])
        {
            r1++;
            r2 = c1[v1][3];
        }

        if (r1 == 0)
        {
            // cheating
            printf("Case #%d: Volunteer cheated!\n", i+1);
            fprintf(out, "Case #%d: Volunteer cheated!\n", i+1);
        }
        else if (r1 == 1)
        {
            // correct card is r2
            printf("Case #%d: %d\n", i+1, r2);
            fprintf(out, "Case #%d: %d\n", i+1, r2);
        }
        else
        {
            // bad magician
            printf("Case #%d: Bad magician!\n", i+1);
            fprintf(out, "Case #%d: Bad magician!\n", i+1);
        }
    }
    return 0;
}