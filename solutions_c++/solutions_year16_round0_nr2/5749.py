#include <algorithm>
#include <string.h>
#include <vector>
#include <cstdio>
#include <climits>
#include <iostream>
using namespace std;
typedef long long lld;

int N;
char seq[102];

int Process()
{
    scanf("%s", seq);
    N = strlen(seq);

    int rev = 0;
    for (int i=N-1; i>=0; i--)
    {
        int cur = (seq[i] == '+');
        if (rev&1) cur = !cur;

        if (!cur)
        {
            rev++;
        }
    }

    return rev;
}

int main ()
{
    freopen("input.txt", "r", stdin);
    freopen("otp.txt", "w", stdout);

    int tests;
    scanf("%d", &tests);
    for (int t=1; t<=tests; t++)
    {
        int ans = Process();
        printf("Case #%d: %d\n", t, ans);
    }
}

