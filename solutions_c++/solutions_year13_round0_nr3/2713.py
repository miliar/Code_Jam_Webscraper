#include <cstdio>
#include <cstring>
#include <string>
#include <iostream>
using namespace std;

int T, A, B;
int f[1100];

bool rev(string s)
{
    int len = s.size();
    for (int i = 0; i < len; i++)
        if (s[i] != s[len - 1 - i]) return false;
    return true;
}

int check(int x)
{
    char s[10];
    itoa(x, s, 10);
    string str = s;
    if (!rev(str))
        return 0;
    itoa(x * x, s, 10);
    str = s;
    if (!rev(str))
        return 0;
    //cout << str << endl;
    return 1;
}

void init()
{
    memset(f, 0, sizeof(f));
    for (int i = 1; i <= 31; i++)
        f[i * i] = check(i);
    for (int i = 1; i <= 1000; i++)
        f[i] += f[i - 1];
}

int main()
{
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);
    scanf("%d", &T);
    init();
    for (int t = 1; t <= T; t++)
    {
        scanf("%d%d", &A, &B);
        printf("Case #%d: %d\n", t, f[B] - f[A - 1]);
    }
    return 0;
}
