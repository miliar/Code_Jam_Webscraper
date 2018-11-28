#include<cstdio>

int main()
{
    int Case;
    scanf("%d", &Case);

    for (int c = 1; c <= Case; c++)
    {
        bool digits[10] = {};
        int n, num = 0, temp, count = 0;
        scanf("%d", &n);
        if (!n)
        {
            printf("Case #%d: INSOMNIA\n", c);
            continue;
        }

        while (count < 10)
        {
            num += n;
            temp = num;
            while (temp)
            {
                int m = temp % 10;
                if (!digits[m])
                    digits[m] = true, count++;
                temp /= 10;
            }
        }

        printf("Case #%d: %d\n", c, num);
    }

    return 0;
}