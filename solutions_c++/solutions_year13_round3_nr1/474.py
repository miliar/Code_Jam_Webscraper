#include <stdio.h>
#include <string.h>

#define SIZE 1000010

char name[SIZE];
int pos[SIZE];

bool is_vowel(char c)
{
    if (c >= 'A' && c <= 'Z')
    {
        c = c - 'A' + 'a';
    }

    switch (c)
    {
        case 'a':
        case 'e':
        case 'i':
        case 'o':
        case 'u':
            return true;

        default:
            break;
    }

    return false;
}

void run(int n)
{
    int len = strlen(name);
    int top = 0;
    int count = 0;

    for (int i = 0; i < len; ++i)
        if (!is_vowel(name[i]))
        {
            count++;

            if (count >= n)
            {
                pos[top++] = i;
            }
#if 0            
            int j;
            for (j = i + 1 - n; j < i; ++j)
                if (is_vowel(name[j]))
                    break;

            if (j == i)
            {
                pos[top++] = i;
            }
#endif
        }
        else
        {
            count = 0;
        }

    if (top == 0)
    {
        printf("0\n");
        return;
    }

    pos[top++] = len;

#if 0
    printf("\n! ");
    for (int i = 0; i < top - 1; ++i)
    {
        printf("%d ", pos[i]);
    }
    printf("\n");
#endif

    unsigned long long ans = 0;
    for (int i = 0; i < top - 1; ++i)
    {
        unsigned long long num = pos[i] + 2 - n;
        ans += num * (pos[i + 1] - pos[i]);
    }

    printf("%llu\n", ans);
}

int main()
{
    int num_case;
    int n;

    scanf("%d", &num_case);

    for (int i = 1; i <= num_case; ++i)
    {
        scanf("%s %d", name, &n);

        printf("Case #%d: ", i);
        run(n);
    }

    return 0;
}
