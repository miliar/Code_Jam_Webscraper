#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;
string S;
int T, ans;

void _main()
{
    cin >> S; ans = 0;
    int N = (int) S.length();
    for (int i = N - 1; i >= 0; i --)
    {
        if (S[i] == '-')
        {
            ans ++;
            for (int j = 0; j <= i; j ++)
            {
                if (S[j] == '-') S[j] = '+';
                else S[j] = '-';
            }
        }
    }
}
int main()
{
    freopen("pancakesin.txt","r",stdin);
    freopen("pancakesout.txt","w",stdout);
    scanf("%d", &T);
    for (int i = 1; i <= T; i ++)
    {
        _main();
        printf("Case #%d: %d\n", i, ans);
    }
}

