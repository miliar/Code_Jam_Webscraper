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

void process(FILE* pfIn, FILE* pfOut)
{
    int i, count;
    unsigned A, B, K;

    fscanf(pfIn, "%d", &count);
    for (i = 1; i <= count; i++)
    {
        fscanf(pfIn, "%d %d %d", &A, &B, &K);

        int n = 0;
        for (int j = 0; j < A; j++)
        {
            for (int k = 0; k < B; k++)
            {
                if ((j & k) < K)
                    n++;
            }
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
