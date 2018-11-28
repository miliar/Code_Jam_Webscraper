#include <stdio.h>

bool validate(int * pattern, int j, int k, int n, int m)
{
    bool valid = true;
    for (int i = 0; i < n && valid; ++i)
    {
        if (pattern[10*i+k] != 1)
        {
            valid = false;
        }
    }
    if (valid) return true;
    valid = true;
    for (int i = 0; i < m && valid; ++i)
    {
        if (pattern[10*j+i] != 1)
        {
            valid = false;
        }
    }
    return valid;
}

int main()
{
    int pattern[100], n, m, t;
    for (int i = 0; i < 10; ++i)
    {
        for (int j = 0; j < 10; ++j)
        {
            pattern[10*i+j] = 0;
        }
    }
    scanf("%d", &t);
    for (int i = 0; i < t; ++i)
    {
        bool valid = true;
        scanf("%d %d", &n, &m);
        for (int j = 0; j < n; ++j)
        {
            for (int k = 0; k < m; ++k)
            {
                scanf("%d", &pattern[10*j+k]);
            }
        }
        for (int j = 0; j < n && valid; ++j)
        {
            for (int k = 0; k < m && valid; ++k)
            {
                if (pattern[10*j+k] == 1)
                {
                    valid = validate(pattern, j, k, n, m);
                }
            }
        }
        if (valid)
        {
            printf("Case #%d: YES\n", i+1);
        } else {
            printf("Case #%d: NO\n", i+1);
        }
    }
    return 0;
}
