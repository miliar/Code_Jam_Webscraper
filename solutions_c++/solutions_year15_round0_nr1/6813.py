#include <cstdio>

int main(int argc, char **argv)
{
    int T, C, SM, i, s, n, t;
    char *S;
    freopen(argv[1], "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &T);
    for (C = 1; C <= T; C++)
    {
        scanf("%d", &SM);
        S = new char[SM + 2];
        scanf("%s", S);
        for (n = s = i = 0; i < SM + 2; i++)
        {
            if (S[i] == '0')
            {
                continue;
            }
            t = i - s;
            if (t > 0)
            {
                n += t;
                s += t;
            }
            s += S[i] - '0';
        }
        printf("Case #%d: %d\n", C, n);
    }
    return 0;
}