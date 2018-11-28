#include<iostream>
#include<cstdio>
#include<cmath>

using namespace std;

int g[5][5] =
{
{0,1,2,3,4},
{0,1,2,3,4},
{0,2,-1,4,-3},
{0,3,-4,-1,2},
{0,4,3,-2,-1}
};
int T, L, X;
char s[10010];

int myabs(int a)
{
    if (a < 0)
        return -a;
    return a;
}

bool check()
{
    int state = 0, now = 1, flag = 1;
    for (; X > 0; --X)
    {
        for (int i = 0; i < L; ++i)
        {
            int j = s[i] - 'i' + 2;
            now = g[myabs(now)][j];
            if (now < 0)
                flag *= -1;
            now = myabs(now);

            if (flag > 0 && now == 2 && state == 0)
                state++;
            else
            if (flag > 0 && now == 4 && state == 1)
                state++;
            else
            if (flag < 0 && now == 1 && state == 2)
                state++;
        }
    }
    //printf("[%d %d %d\n", state, now, flag);
    return state == 3 && now == 1 && flag == -1;
}

int main()
{
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small.out", "w", stdout);
    cin >> T;
    int cas = 1;
    for (int cas = 1; cas <= T; ++cas)
    {
        cin >> L >> X;
        cin >> s;
        printf("Case #%d: ", cas);
        if (check())
            puts("YES");
        else
            puts("NO");
    }
    return 0;
}
