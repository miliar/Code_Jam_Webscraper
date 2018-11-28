#include <bits/stdc++.h>

using namespace std;

char s[2010];

int c[30], digit[20];

vector<char> ans;

int val(char c)
{
    return c-'A';
}

int main()
{
    int test;
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
    scanf("%d", &test);
    for (int t = 1; t <= test; t++)
    {
        scanf("%s", s);
        int len = strlen(s);
        memset(c, 0, sizeof(c));
        for (int i = 0; i < len; i++)
        {
            c[s[i]-'A']++;
        }
        digit[0] = c[25];
        c[val('E')] -= digit[0];
        c[val('R')] -= digit[0];
        c[val('O')] -= digit[0];
        digit[2] = c[val('W')];
        c[val('T')] -= digit[2];
        c[val('O')] -= digit[2];
        digit[8] = c[val('G')];
        c[val('E')] -= digit[8];
        c[val('I')] -= digit[8];
        c[val('H')] -= digit[8];
        c[val('T')] -= digit[8];
        digit[3] = c[val('H')];
        c[val('T')] -= digit[3];
        c[val('R')] -= digit[3];
        c[val('E')] -= digit[3];
        c[val('E')] -= digit[3];
        digit[4] = c[val('U')];
        c[val('F')] -= digit[4];
        c[val('O')] -= digit[4];
        c[val('R')] -= digit[4];
        digit[5] = c[val('F')];
        c[val('I')] -= digit[5];
        c[val('V')] -= digit[5];
        c[val('E')] -= digit[5];
        digit[7] = c[val('V')];
        c[val('S')] -= digit[7];
        c[val('E')] -= digit[7];
        c[val('E')] -= digit[7];
        c[val('N')] -= digit[7];
        digit[6] = c[val('S')];
        c[val('I')] -= digit[6];
        c[val('X')] -= digit[6];
        digit[1] = c[val('O')];
        digit[9] = c[val('I')];
        printf("Case #%d: ", t);
        for (int i = 0; i < 10; i++)
        {
            for (int j = 0; j < digit[i]; j++)
            {
                printf("%d", i);
            }
        }
        printf("\n");
    }
    return 0;
}
