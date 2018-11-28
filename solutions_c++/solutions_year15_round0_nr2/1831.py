#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#include<iostream>
#include<algorithm>
#include<queue>
#include<stack>
#include<vector>
#include<map>
#include<set>
#include<deque>
#include<bitset>
#include<time.h>
#define ll __int64
#define inf 0x7FFFFFFF
#pragma comment(linker, "/STACK:102400000,102400000")
using namespace std;
int a[10000];
int n;
int find(int x)
{
    int extra = 0;
    for (int i=1; i<=n; i++)
    {
        if (a[i]>x)
        {
            extra += a[i]/x;
            if (a[i]%x!=0)
                extra++;
            extra--;
        }
    }
    return x+extra;
}
int main()
{
    int i,j,k;
    int m,t;
    //srand((unsigned)time(NULL));//int data=rand()%10000+1;
    freopen("B-large.in","r",stdin);freopen("B-output-large.txt","w",stdout);
    scanf("%d",&t);for(int tcase=1;tcase<=t;tcase++)
    //while(scanf("%d",&n)!=EOF)
    {
        scanf("%d",&n);
        int mmax = -1;
        for (i=1; i<=n; i++)
        {
            scanf("%d", &a[i]);
            mmax=max(mmax, a[i]);
        }
        int ans = inf;
        for (i=1; i<=mmax; i++)
        {
            ans = min(ans, find(i));
        }
        printf("Case #%d: %d\n", tcase, ans);
    }
}
/*
11
25 7 7 7 7 7 7 7 7 7 7
-->10
11
25 9 9 9 9 9 9 9 9 9 9
-->11
2
25 9
-->10
2
24 24
-->12
4
9 8 5 6
*/
