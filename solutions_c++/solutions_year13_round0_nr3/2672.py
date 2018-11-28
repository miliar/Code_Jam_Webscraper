#include<cstdio>
#include<stdio.h>
#include<iostream>
#include<cstring>
#include<string.h>
#include<string>
#include<algorithm>
#include<cmath>
#include<math.h>
#include<vector>
#include<list>
#include<ctime>
#include<cctype>
#include<deque>
#include<set>
#include<stack>
#include<queue>
using namespace std;

bool isOk[11000000];

bool isH(long long x)
{
    int len = 0, bt[20] = {0};
    while (x != 0)
    {
        bt[++len] = x % 10;
        x /= 10;
    }
    bool flag = true;
    for (int i = 1; i * 2 <= len; i++)
    {
        if (bt[i] != bt[len + 1 - i])
        {
            flag = false;
            break;
        }
    }

    return flag;
}

void sick(void)
{
    memset(isOk, false, sizeof(isOk));
    for (long long i = 1; i <= 10100000LL; i++)
    {
        if (isH(i) && isH(i * i))
        {
            isOk[i] = true;
            //printf("<%lld>--><%lld>\n", i, i * i);
        }

    }
}

int main(void)
{
    // freopen("input.txt", "r", stdin);
   // freopen("output.txt", "w", stdout);
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);
   // freopen("C-large.in", "r", stdin);
   // freopen("C-large.out", "w", stdout);

   sick();

   int T, cas = 1; scanf("%d", &T);
    while (T--)
    {
        long long A, B; scanf("%lld%lld", &A, &B);
        long long a = long(sqrt(A)) - 2, b = long(sqrt(B)) + 2;
        while (a * a < A) a++; while (b * b > B) b--;

        printf("Case #%d: ", cas++);

        int cnt = 0;

        for (int i = a; i <= b; i++)
        {
            if (isOk[i] == true)
            {
                cnt++;
            }
        }

        printf("%d\n", cnt);
    }


    return 0;
}


