#include<cstdio>
#include <cstring>
#include<algorithm>
using namespace std;

int t;
char s[105], s1[105];

int nrMinus(char *s, int dim)
{
    int y = 0;
    for (int i = 0; i < dim - 1; i++)
        if (s[i] == '+' && s[i + 1] == '-')
            y ++;

    if (s[0] == '-')
        y++;

    return y;
}

char * full(char s[105], int dim)
{
    for (int i = 0; i < dim; i++)
        s[i] = '+';

    return s;
}

int lastXX(char s[105], int dim)
{
    int y = 0;
    for (int i = 0; i < dim; i++)
        if (s[i] == '-')
            y = i;

    return y;
}

char * schimb(char s[105], int poz)
{
    for (int i = 0; i <= poz; i++)
        if (s[i] == '+')
            s[i] = '-';
            else s[i] = '+';

    return s;
}

int main()
{
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);

    scanf("%d\n", &t);
    for (int index = 1; index <= t; index++)
    {
        gets(s);
        int ans = 0;
        for (int i = 1; i < strlen(s); i++)
        {
            if (s[i-1] != s[i])
            ans++;
        }
        if (s[strlen(s)  -1] == '-' )ans++;
        printf("Case #%d: %d\n", index, ans);
    }

    return 0;
}
