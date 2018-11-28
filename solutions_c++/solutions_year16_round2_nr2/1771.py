#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#define LL long long
using namespace std;

int T, kase = 0, n;
char s1[20], s2[20], a1[20], a2[20];

bool check(int i, char s[], int n)
{
    int x = 0;
    int j;
    for (j = n - 1; j >= 0; j--, i /= 10)
        if (s[j] != '?' && i % 10 != s[j] - '0') return false;
    return true;
}

int main()
{
    freopen("B-small-attempt5.in", "r", stdin);
    freopen("BB-small-attempt5.out", "w", stdout);
    cin >> T;
    while (T--)
    {
        scanf("%s%s", s1, s2);
        n = strlen(s1);
        int i, j, ansi, ansj, ans = 99999999;;
        if (n == 1)
        {
            for (i = 0; i <= 9; i++)
                for (j = 0; j <= 9; j++)
                if (check(i, s1, n) && check(j, s2, n) && abs(i - j) < ans)
            {
                ans = abs(i - j);
                ansi = i;
                ansj = j;
            }
            a1[0] = ansi + '0';
            a1[1] = '\0';
            a2[0] = ansj + '0';
            a2[1] = '\0';
        }
        if (n == 2)
        {
            for (i = 0; i <= 99; i++)
                for (j = 0; j <= 99; j++)
                if (check(i, s1, n) && check(j, s2, n) && abs(i - j) < ans)
            {
                ans = abs(i - j);
                ansi = i;
                ansj = j;
            }
            a1[0] = ansi / 10 + '0';
            a1[1] = ansi % 10 + '0';
            a1[2] = '\0';
            a2[0] = ansj / 10 + '0';
            a2[1] = ansj % 10 + '0';
            a2[2] = '\0';
        }
        if (n == 3)
        {
            for (i = 0; i <= 999; i++)
                for (j = 0; j <= 999; j++)
                if (check(i, s1, n) && check(j, s2, n) && abs(i - j) < ans)
            {
                ans = abs(i - j);
                ansi = i;
                ansj = j;
            }
            a1[0] = ansi / 100 + '0';
            a1[1] = ansi / 10 % 10 + '0';
            a1[2] = ansi % 10 + '0';
            a1[3] = '\0';
            a2[0] = ansj / 100 + '0';
            a2[1] = ansj / 10 % 10 + '0';
            a2[2] = ansj % 10 + '0';
            a2[3] = '\0';
        }
        printf("Case #%d: %s %s\n", ++kase, a1, a2);
  //      printf("Case #%d: %s %s %s %s\n", ++kase, s1, s2, s3, s4);
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
