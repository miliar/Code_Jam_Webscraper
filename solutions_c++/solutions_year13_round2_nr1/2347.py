#include <iostream>
#include <cstdio>
#include <math.h>
#include <algorithm>
using namespace std;

int A,n;
int s[10005];

int judge(long long cur,int big)
{
    int step = 0;
    while(step < n)
    {
        if(cur > big)
            return step;

        cur = 2 * cur - 1;
        step ++;
    }
    return step;
}

long long add(long long cur,int step)
{
    for(int i = 0; i < step; i ++)
        cur = cur *2 -1;
    return cur;
}

int main()
{
    int T;
    freopen("A-small-attempt3.in","r",stdin);
    freopen("AOUT.out","w",stdout);

    scanf("%d",&T);
    for(int tt = 1; tt <= T; tt++)
    {
        scanf("%d %d",&A,&n);
        long long current = A;
        int ans = 0;
        for(int i = 0; i < n ; i++)
            scanf("%d",&s[i]);

        sort(s,s + n);

        if(A == 1)
        {
            ans = n;
            printf("Case #%d: %d\n",tt,ans);
            continue;
        }

        for(int i = 0; i < n; i++)
        {
            int temp = s[i];
            if(current > temp)
                current += temp;
            else if(current <= temp)
            {
                long long cur = current;
                int t = judge(cur,temp);
                //printf("judege:%d\n",t);
                if(t < n - i)
                {
                    ans += t;
                    current = add(current,t);
                    current += s[i];
                }
                else
                {
                    ans = ans + n - i;
                    break;
                }
            }
            //printf("cur:%lld\n",current);
        }
        printf("Case #%d: %d\n",tt,ans);
    }
    return 0;
}

