#include <stdio.h>

int t;
int n, rest;
bool check[10];

void checkdigit(int x)
{
    while (x)
    {
        if (not check[x%10])
        {
            check[x%10] = true;
            rest--;
        }
        x /= 10;
    }
}

int main()
{
    freopen("/Users/IohcEjnim/Downloads/A-large.in.txt", "r", stdin);
    freopen("/Users/IohcEjnim/Downloads/result.txt", "w", stdout);
    int tn, i;
    scanf("%d", &t);
    for (tn = 1; tn <= t; tn++)
    {
        scanf("%d", &n);
        printf("Case #%d: ", tn);
        if (n == 0)
        {
            printf("INSOMNIA\n");
            continue;
        }
        for (i = 0; i < 10; i++) check[i] = false;
        rest = 10;
        for (i = 1; ; i++)
        {
            checkdigit(i*n);
            if (rest == 0)
            {
                printf("%d\n", i*n);
                break;
            }
        }
    }
}