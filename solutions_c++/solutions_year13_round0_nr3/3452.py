#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>
using namespace std;

bool is_palindrome(int n)
{
    char num[100];
    itoa(n, num, 10);
    int len = strlen(num);
    for (int i = 0; i < len / 2; ++ i)
        if (num[i] != num[len - i - 1])
            return false;
    return true;
}

int main()
{
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int r = 1; r <= T; ++ r)
    {
        int a, b;
        scanf("%d%d", &a, &b);
        int cnt = 0;
        for (int i = 1; i < 100; i ++)
        {
            int t = i * i;
            if (t < a) continue;
            if (t > b) break;
            if (is_palindrome(i) && is_palindrome(t))
                cnt ++;
        }
        printf("Case #%d: %d\n", r, cnt);
    }
    return 0;
}
