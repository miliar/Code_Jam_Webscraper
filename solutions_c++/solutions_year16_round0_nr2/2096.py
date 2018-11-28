#include <stdio.h>
#include <cstring>
#include <string>
//#include <algorithm>

using namespace std;

char s[105];
int count;

char invert(char x)
{
    if (x == '+')
        return '-';
    return '+';
}

void flip(int j)
{
    count++;
    for (int i = 0; i <= j/2; i++)
    {
        char temp = s[i];
        s[i] = invert(s[j-i]);
        s[j-i] = invert(temp);
    }
}

int main()
{
    int test, last, front;
    //freopen("test.in", "r", stdin);
    //freopen("test.out", "w", stdout);
    scanf("%d", &test);
    for (int t = 1; t <= test; t++)
    {
        count = 0;
        scanf("%s", s);
        int len = strlen(s);
        last = len-1;
        while (1)
        {
            while (s[last] == '+' && last >= 0)
                last--;
            if (last < 0)
                break;
            if (s[0] == '-')
            {
                flip(last);
            }
            else
            {
                for (front = 0; front < len; front++)
                {
                    if (s[front] == '-')
                        break;
                }
                flip(front-1);
            }
            //printf("%s\n", s);
        }
        printf("Case #%d: %d\n", t, count);
    }
    return 0;
}
