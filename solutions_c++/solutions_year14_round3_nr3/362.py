#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <algorithm>

#define iterator            IT
#define VEC(T)              vector<T >
#define VIT(T)              vector<T >::IT

typedef long long           I64;
typedef unsigned long long  UI64;

using namespace std;

int gN, gM, gK;

bool getXY(int k, int& x, int& y)
{
    int v, gap = INT_MAX;

    int iMax = min(gN, k / 2);
    int jMax = min(gM, k / 2);
    for (int i = iMax; i > 0; i--)
    {
        for (int j = jMax; j > 0; j--)
        {
            v = i * j;
            if (v > k)
                break;

            if (gap > abs(v - k))
            {
                gap = abs(v - k);
                x = i;
                y = j;

                if (v == k)
                    return true;
            }
        }
    }

    for (int i = 1; i <= gN; i++)
    {
        for (int j = 1; j <= gM; j++)
        {
            v = i * j;
            if (v > k)
                break;

            if (gap > abs(v - k))
            {
                gap = abs(v - k);
                x = i;
                y = j;

                if (v == k)
                    return true;
            }
        }
    }

    return false;
}

void process(FILE* pfIn, FILE* pfOut)
{
    int i, count, x, y;

    fscanf(pfIn, "%d", &count);
    for (i = 1; i <= count; i++)
    {
        fscanf(pfIn, "%d %d %d", &gN, &gM, &gK);

        int n;

        x = gN;
        y = gM;

        if (gN < 3 || gM < 3)
        {
            n = gK;
        }
        else if (getXY(gK + 4, x, y))
        {
            if (x > gN || y > gM)
                printf("%d : %d %d %d ==> %d %d\n", i, gN, gM, gK, x, y);
            n = (x - 2) * 2 + (y - 2) * 2;
        }
        else
        {
            if (x > gN || y > gM)
                printf("%d : %d %d %d ==> %d %d\n", i, gN, gM, gK, x, y);

            n = (x - 2) * 2 + (y - 2) * 2;

            if (x < gN || y < gM)
                n += 1;
            else
                n += gK - (x * y - 4);
        }

        fprintf(pfOut, "Case #%d: %d\n", i, n);
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
