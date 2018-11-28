//B_Infinite House of Pancakes.cpp -- Google Code Jam Qualification Round 2015
#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <cmath>
typedef long long ll;
using namespace std;
const int maxd = 1000 + 100;
int d, p[maxd];
int main()
{
    int T, ans = 0;
    scanf("%d", &T);
    while( T-- )
    {
        scanf("%d", &d);
        int Max = 0, cnt = 0;
        for(int i=0; i<d; i++)
        {
            scanf("%d", &p[i]);
            Max = max(Max, p[i]);
        }
        int Min = Max;
        for(int i=1; i<=Max; i++)
        {
            cnt = i;
            for(int j=0; j<d; j++)
            {
                if( p[j]>i )
                {
                    cnt += (p[j]-1)/i;
                }
            }
            Min = min(Min, cnt);
        }
        printf("Case #%d: %d\n", ++ans, Min);
    }
    return 0;
}

