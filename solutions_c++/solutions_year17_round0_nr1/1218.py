#include <bits/stdc++.h>

using namespace std;

const int MAXS = 1000;

char s[MAXS + 9];

int answ;
bool isOk(int lenS)
{
    for (int i=0; i<lenS; i++)
        if (s[ i ] == '-')
            return false;

    return true;
}

void flip(int it, int len)
{
    for (;len>0; it++, len--)
    {
        if (s[it] == '+')
            s[it] = '-';
        else
            s[it] = '+';
    }
}

int main()
{
    int T;scanf("%d", &T);
    for (int c = 1; c<=T; c++)
    {
        int K;
        scanf("%s %d", s, &K);

        int lenS = strlen(s);
        answ = 0;

        for (int i=0; i+K<=lenS; i++)
        {
            if (s[ i ] == '-')
            {
                flip(i, K);
                answ++;
            }
        }

        printf("Case #%d: ", c);
        if (isOk(lenS))
            printf("%d", answ);
        else
            printf("IMPOSSIBLE");
        printf("\n");
    }

    return 0;
}


