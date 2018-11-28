#include <bits/stdc++.h>

using namespace std;

long long N, nextNum, countDig, T;
bool used[10];

void checkNum(long long curNum)
{
    while (curNum)
    {
        if (!used[curNum % 10])
        {
            countDig++;
            used[curNum % 10] = true;
        }
        curNum /= 10;
    }
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    scanf("%lld", &T);
    for (int i = 0; i < T; ++i)
    {
        fill(used, used + 10, 0);
        nextNum = 0;
        countDig = 0;
        scanf("%lld", &N);
        if (!N) printf("Case #%d: INSOMNIA\n", i + 1);
        else
        {
            while (countDig < 10)
            {
                nextNum += N;
                checkNum(nextNum);
            }
            printf("Case #%d: %lld\n", i + 1, nextNum);
        }
    }
}
