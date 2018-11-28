#include <cstdio>
#include <algorithm>
using namespace std;
bool digits[10];
void processDigits(int x)
{
    while (x != 0)
    {
        int y = x%10;
        digits[y] = true;
        x /= 10;
    }
}
int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out_codejam1_1.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int z = 1; z <= t; z++)
    {
        for (int i = 0; i < 10; i++)
            digits[i] = false;
        int n;
        scanf("%d", &n);
        if (n == 0)
        {
            printf("Case #%d: INSOMNIA\n", z);
        }
        else
        {
            int num = 0;
            for (int i = 0; i <= 10000000; i++)
            {
                num += n;
                processDigits(num);
                bool done = true;
                for (int i = 0; i < 10; i++)
                {
                    if (digits[i] == false)
                        done = false;
                }
                if (done)
                    break;
            }
            bool done = true;
            for (int i = 0; i < 10; i++)
            {
                if (digits[i] == false)
                    done = false;
            }
            if (done)
                printf("Case #%d: %d\n", z, num);
            else
                printf("Case #%d: INSOMNIA\n", z);
        }
    }
    return 0;
}
