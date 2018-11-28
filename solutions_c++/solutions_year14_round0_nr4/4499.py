#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstring>
using namespace std;
double naomi[1024], ken[1024], used[1024];
const double eps = 1e-6;
bool check(int pos1, int n)
{
    for(int pos2 = 0; pos1 < n; pos1++, pos2++)
        if(naomi[pos1] < ken[pos2])
            return 0;
    return 1;
}
int main()
{
    int t = 0, T;
    scanf("%d", &T);
    while(t++ < T)
    {
        memset(used, 0, sizeof(used));
        int n, i, j, fair = 0, cheat = 0;
        scanf("%d", &n);
        for(i = 0; i < n; i++)
            cin>>naomi[i];
        for(i = 0; i < n; i++)
            cin>>ken[i];
        sort(naomi, naomi + n);
        sort(ken, ken + n);
        for(i = 0; i < n; i++)
        {
            for(j = 0; j < n; j++)
            {
                if(ken[j] > naomi[i] && used[j] == 0)
                {
                    used[j] = 1;
                    break;
                }
            }
            if(j == n)
                fair++;
        }
        int pos = 0;
        for(i = n - 1; i >= 0; i--)
        {
            if(check(pos, n))
            {
                cheat = n - pos;
                break;
            }
            pos++;
        }
        printf("Case #%d: %d %d\n", t, cheat, fair);
    }
    return 0;
}