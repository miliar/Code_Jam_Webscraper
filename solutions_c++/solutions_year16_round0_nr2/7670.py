#include <cstdio>
#include <queue>
#include <string>
#include <map>
#include <cstring>
#include <algorithm>
#include <iostream>
#define MAXINT 2147483647 
using namespace std;
int casenum;
int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &casenum);
    for (int icn = 0; icn != casenum; ++icn)
    {
        char ch[200];
        int f[200];
        scanf("%s", ch);
        int len = strlen(ch);
        int cnt = 0;
        for (int i = len - 1; i >= 0; --i)
        {
            if (ch[i] == '+') f[i] = 1;
            else f[i] = 0;
        }
        int tt = 1;
        for (int i = len - 1; i >= 0; --i)
        {
            if (f[i] == tt) continue;
            else 
            {
                if (f[0] == 1 - tt)
                {
                    cnt++;
                    for (int j = 0; j < i; ++j) 
                        f[j] =  1 - f[j];
                }
                else
                {
                    tt = 1 - tt;
                    cnt++;

                }
            }
        }
        printf("Case #%d: %d\n", icn + 1, cnt);
    }
    return 0;
}