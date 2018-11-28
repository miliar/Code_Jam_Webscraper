#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <algorithm>

#define IT                  iterator
#define VEC(T)              vector<T >
#define VIT(T)              vector<T >::IT

typedef long long           I64;
typedef unsigned long long  UI64;

using namespace std;

int gR, gC;
char gB[100][101];

int  gRN[100];
int  gRC[100][100];

int  gCN[100];
int  gCR[100][100];

int solve()
{
    memset(gRN, 0, sizeof(gRN));
    memset(gCN, 0, sizeof(gCN));

    int res = 0;
    
    for (int i = 0; i < gR; i++)
    {
        for (int j = 0; j < gC; j++)
        {
            if (gB[i][j] != '.')
            {
                gRC[i][gRN[i]++] = j;
                gCR[j][gCN[j]++] = i;
            }
        }
    }

    for (int i = 0; i < gR; i++)
    {
        int rc0 = gRC[i][0];
        int rc1 = gRC[i][gRN[i] - 1];
        for (int j = 0; j < gC; j++)
        {
            if (gB[i][j] == '.')
                continue;

            if ((gRN[i] == 1 && gCN[j] <= 1) || (gRN[i] <= 1 && gCN[j] == 1))
                return -1;

            int cr0 = gCR[j][0];
            int cr1 = gCR[j][gCN[j] - 1];

            if ((j == rc0 && gB[i][j] == '<') || (i == cr0 && gB[i][j] == '^')) {
                res++;
                if (gRN[i] > 1)
                    gB[i][j] = '>';
                else if (gCN[i] > 1)
                    gB[i][j] = 'v';
            }
            else if ((j == rc1 && gB[i][j] == '>') || (i == cr1 && gB[i][j] == 'v')) {
                res++;
                if (gRN[i] > 1)
                    gB[i][j] = '<';
                else if (gCN[i] > 1)
                    gB[i][j] = '^';
            }
        }
    }

    return res;
}

void process(FILE* pfIn, FILE* pfOut)
{
    int tn, T;

    fscanf(pfIn, "%d", &T);
    for (tn = 1; tn <= T; tn++)
    {
        fscanf(pfIn, "%d %d", &gR, &gC);
        for (int i = 0; i < gR; i++)
            fscanf(pfIn, "%s", gB[i]);

        int res = solve();
        if (res < 0)
            fprintf(pfOut, "Case #%d: %s\n", tn, "IMPOSSIBLE");
        else
            fprintf(pfOut, "Case #%d: %d\n", tn, res);
    }
}

//-----------------------------------------------------------------------------

void process(const char* pcszInFile, const char* pcszOutFile)
{
    FILE* pfIn = fopen(pcszInFile, "rt");
    if (pfIn == NULL)
    {
        printf("file not found! \"%s\"\n", pcszInFile);
        exit(-2);
    }

    FILE* pfOut = fopen(pcszOutFile, "wt");
    if (pfOut == NULL)
    {
        printf("can't create file! \"%s\"\n", pcszOutFile);
        exit(-3);
    }

    process(pfIn, pfOut);

    fclose(pfIn);
    fclose(pfOut);
}

void main(int argc, char* argv[])
{
    if (argc != 3)
    {
        printf("Usage : %s <input_file> <output_file>\n", argv[0]);
        exit(-1);
    }

    process(argv[1], argv[2]);
}
