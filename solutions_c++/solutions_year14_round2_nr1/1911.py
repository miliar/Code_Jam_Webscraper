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

int  gN;
char gStr[200][200];

int  gCharN;
int  gChar[200];
int  gCharCnt[200][200];

void checkFirstStr()
{
    int i, j;

    char* s = gStr[0];

    j = 0;
    for (i = 1; s[i]; i++)
    {
        if (s[j] != s[i])
        {
            gChar[gCharN] = s[j];
            gCharCnt[0][gCharN] = i - j;
            gCharN++;
            j = i;
        }
    }
    gChar[gCharN] = s[j];
    gCharCnt[0][gCharN] = i - j;
    gCharN++;
}

bool checkStr(int n)
{
    int i, j, k;

    char* s = gStr[n];

    j = 0;
    k = 0;
    for (i = 1; s[i]; i++)
    {
        if (s[j] != s[i])
        {
            if (gChar[k] != s[j])
                return false;
            gCharCnt[n][k] = i - j;
            k++;
            j = i;
        }
    }
    if (gChar[k] != s[j])
        return false;
    gCharCnt[n][k] = i - j;
    k++;

    if (k != gCharN)
        return false;

    return true;
}

int minMove(void)
{
    int i, j, m, n1, n2, sum;

    sum = 0;
    for (i = 0; i < gCharN; i++)
    {
        m = 0;
        for (j = 0; j < gN; j++)
            m += gCharCnt[j][i];
        m /= gN;

        n1 = 0;
        for (j = 0; j < gN; j++)
            n1 += abs(m - gCharCnt[j][i]);

        m++;

        n2 = 0;
        for (j = 0; j < gN; j++)
            n2 += abs(m - gCharCnt[j][i]);

        sum += min(n1, n2);
    }

    return sum;
}

void process(FILE* pfIn, FILE* pfOut)
{
    int i, j, count;
    char buff[200];

    fscanf(pfIn, "%d", &count);
    for (i = 1; i <= count; i++)
    {
        fscanf(pfIn, "%d", &gN);
        for (j = 0; j < gN; j++)
            fscanf(pfIn, "%s", gStr[j]);

        fprintf(pfOut, "Case #%d: ", i);

        bool ok = true;

        gCharN = 0;
        checkFirstStr();
        for (j = 1; j < gN; j++)
        {
            ok = checkStr(j);
            if (!ok)
                break;
        }
        if (!ok)
            fprintf(pfOut, "Fegla Won\n");
        else
            fprintf(pfOut, "%d\n", minMove());
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
