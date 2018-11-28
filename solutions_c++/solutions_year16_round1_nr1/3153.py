// probA.cpp : The Last Word
#include <cstdio>
#include <cstring>
using namespace std;

const int MAXL = 1000 + 10;
int T;
char str[MAXL];
char ans[MAXL * 2];
int p, q;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    scanf("%d", &T);
    for (int z = 1; z <= T; ++z)
    {
        scanf("%s", str);
        p = q = MAXL;
        ans[q++] = str[0];
        for (int i = 1; str[i]; ++i)
        {
            if (str[i] >= ans[p])
                ans[--p] = str[i];
            else
                ans[q++] = str[i];
        }
        ans[q] = 0;
        printf("Case #%d: %s\n", z, &ans[p]);
    }

    fclose(stdin);
    fclose(stdout);
    return 0;
}

