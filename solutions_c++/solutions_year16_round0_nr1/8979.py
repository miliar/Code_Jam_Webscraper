#include <iostream>
#include <cstring>
#include <cmath>
#include <sstream>
#include <cstdio>
using namespace std;

int main()
{
    freopen("A-large.in", "r", stdin);

    freopen("A-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    int a[10];
    int flag;
    stringstream stream;
    for (int kase = 1; kase <= T; kase++)
    {
        int n;
        scanf("%d", &n);
        if (n == 0)
        {
            printf("Case #%d: INSOMNIA\n", kase);
        }
        else
        {
            for (int z = 0; z < 10; z++)
                a[z] = 0;

            for(int i = 1; i<=100; i++)
            {
                int t = n*i;
                int tmp = t;
                while (t)
                {
                    int m = t%10;
                    a[m] = 1;
                    t /= 10;
                }
                flag = 1;
                for (int j = 0; j < 10; j++)
                {
                    if (a[j] == 0)
                    {
                        flag = 0;
                        break;
                    }

                }
                if (flag == 1)
                {
                    printf("Case #%d: %d\n", kase, tmp);

                    break;
                }
            }
        }

    }
    return 0;
}
