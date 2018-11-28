#include <iostream>
#include <cstdio>

using namespace std;

bool use[10];

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);

    int n;
    scanf("%d", &n);

    for (int i = 1; i <= n; i++)
    {
        printf("Case #%d: ", i);

        int x;
        scanf("%d", &x);

        if (x == 0)
        {
            printf("INSOMNIA\n");
            continue;
        }

        for (int j = 0; j < 10; j++)
            use[j] = false;

        int j = 0;
        int cnt = 10;
        while (cnt > 0)
        {
            j += x;
            int y = j;

            while (y)
            {
                if (!use[y % 10]) cnt--;
                use[y % 10] = true;
                y /= 10;
            }
        }

        printf("%d\n", j);
    }
}
