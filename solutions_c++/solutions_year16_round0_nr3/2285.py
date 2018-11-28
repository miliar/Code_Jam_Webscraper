#include <stdio.h>

char str[33] = "1";

void println()
{
    for (int i = 3; i <= 11; i++)
    {
        printf(" %d", i);
    }
    printf("\n");
}

void out(int n, int s, int deep, int& need)
{
    if (need == 0)
    {
        return;
    }
    int gap = (n % 2 == 1 && deep == 0 ? 2 : 1);
    for (int i = s; i < n - 1; i++)
    {
        str[i] = '1';
        for (int j = i + gap; j < n - 1; j += 2)
        {
            str[j] = '1';
            printf("%s", str);
            println();
            need--;
            out(n, j + 1, deep + 1, need);
            if (need == 0)
            {
                return;
            }
            str[j] = '0';
        }
        str[i] = '0';
    }
}

int main()
{
    int T;
    scanf("%d", &T);
    for (int c = 1; c <= T; c++)
    {
        printf("Case #%d:\n", c);
        int n, j;
        scanf("%d%d", &n, &j);
        for (int i = 1; i < n - 1; i++)
        {
            str[i] = '0';
        }
        str[n - 1] = '1';
        str[n] = '\0';
        if (n % 2 == 0)
        {
            printf("%s", str);
            println();
            j--;
        }
        out(n, 1, 0, j);
    }
}

