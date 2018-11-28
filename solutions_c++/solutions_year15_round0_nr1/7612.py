#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <queue>
#include <algorithm>
#include <vector>
#include <set>
#include <math.h>
#define LL long long

const int maxn = 1000 + 10;

using namespace std;

int a[maxn];
int main()
{
    //freopen("in","r",stdin);
    //freopen("out","w",stdout);
    int t,n;
    string s;
    cin >>t;
    for(int cs = 1; cs <= t; cs ++)
    {
        int ans = 0,sum = 0;

        scanf("%d",&n);
        cin >>s;
        for(int i = 0; i <= n; i++)
        {
            a[i] = s[i] - '0';
        }

        sum = a[0];

        for(int i = 1; i <= n; i++)
        {
            if(i > sum)
            {
                ans += i - sum;
                sum = i + a[i];
            }
            else
            {
                sum += a[i];
            }
        }
        printf("Case #%d: %d\n",cs,ans);
    }
    return 0;
}

