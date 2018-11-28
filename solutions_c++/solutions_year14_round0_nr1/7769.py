#include <iostream>
#include <stdio.h>

using namespace std;

void input(int a[])
{
    int row;
    scanf("%d", &row);
    for (int j = 0; j < 4; ++j)
    {
        int tmp[4];
        for (int t = 0; t < 4; ++t)
            scanf("%d", &tmp[t]);
        if (j+1 == row)
            for (int t = 0; t < 4; ++t)
                a[t] = tmp[t];
    }
}

int Find(int a[], int b[], int &ans)
{
    int dem = 0;
    for (int i = 0; i < 4; ++i)
        for (int j = 0; j < 4; ++j)
        if (a[i] == b[j])
        {
            ans = a[i];
            ++dem;
            if (dem > 1)
                return 2;
        }
    return dem;
}

int main()
{
   freopen("A-small-attempt4.in", "r", stdin);
   freopen("A-small-attempt4.out", "w", stdout);

    int test;
    scanf("%d", &test);
    for (int i = 1; i <= test; ++i)
    {
        int a[4], b[4];
        input(a);
        input(b);
        printf("Case #%d: ", i);
        int ans = 0;
        switch(Find(a, b, ans))
        {
            case 2: printf("Bad magician!\n"); break;
            case 1: printf("%d\n", ans); break;
            case 0: printf("Volunteer cheated!\n"); break;
        }
    }
    return 0;
}
