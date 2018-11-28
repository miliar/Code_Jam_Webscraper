#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<cstring>
#include<cstdlib>
int mr[2000];
int min(int a,int b)
{
    if ( a < b ) return a ;
    return b;
}
int main()
{
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    int caseTest;
    scanf("%d",&caseTest);
    for (int _ = 1 ; _ <= caseTest ; _ ++)
    {
        int n ;
        scanf("%d",&n);
        int nowMax = 0;
        int ans1 = 0 , ans2 = 0;
        for (int i = 1; i <= n ; i ++)
        {
            scanf("%d",&mr[i]);
            if (i > 1 && mr[i - 1] - mr[i] > nowMax)
                nowMax = mr[i - 1] - mr[i];
        }
        for (int i = 2 ; i <= n ; i ++)
        {
            if (mr[i] < mr[i - 1])
                ans1 += mr[i - 1] - mr[i];
        }
        for (int i = 2 ; i <= n ; i ++)
        {
            int p = mr[i - 1] - mr[i];
            if (p < 0)
                ans2 += min(mr[i - 1],nowMax);
            else if ( p <= nowMax )
                ans2 += min(nowMax,mr[i - 1]);
        }
        printf("Case #%d: %d %d\n",_,ans1,ans2);

    }
    fclose(stdin);
    fclose(stdout);
}
