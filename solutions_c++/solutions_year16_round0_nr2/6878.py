#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int calculate(char *s)
{
    int l, n = 0, i;

    l = strlen(s);

    for(i = 1; i < l; i++)
    {
        if(s[i-1] != s[i])
            n++;
    }

    if(s[l-1] == '-')
        return n+1;
    return n;


}

int main()
{
    int i, n, t;
    char s[101];

    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    scanf("%d\n",&t);

    for(i = 0; i < t; i++)
    {
        gets(s);

        n = calculate(s);

        printf("Case #%d: %d\n",i + 1, n);

    }

    return 0;
}
