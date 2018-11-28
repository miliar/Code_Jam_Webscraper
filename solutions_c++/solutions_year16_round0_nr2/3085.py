#include<cstdio>
#include<cstring>
#include<algorithm>
#define N 105
using namespace std;

inline void turn(char* first, char *last);
int main()
{
    int Case;
    char str[N];
    scanf("%d", &Case);
    getchar();

    for (int c = 1; c <= Case; c++)
    {
        gets(str);
        int len = strlen(str), idx, count = 0, i;
        for (idx = len - 1; idx > 0; idx--)
        {
            if (str[idx] == '-')
            {
                if (str[0] == '+')
                {
                    for (i = idx - 1; str[i] == '-'; i--);
                    turn(str, str + i + 1);
                    count++;
                }

                turn(str, str + idx + 1);
                count++;
            }
        }

        if (str[0] == '-')
            count++;
        
        printf("Case #%d: %d\n", c, count);
    }

    return 0;
}
inline void turn(char* first, char *last)
{
    reverse(first, last);
    while (first != last)
    {
        *first = (*first) == '+' ? '-' : '+';
        first++;
    }
}