#include <iostream>
#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <set>
#include <vector>
#include <map>
#include <stack>
#include <math.h>
using namespace std;
#define MAX(a,b) a > b ? a : b
#define MIN(a,b) a < b ? a : b
#define INF 0x7fffffff
#define maxn 1001000
#define eps 10e-7

int judge(int b)
{
    int a[1000];
    int sum = 0;
    while(b)
    {
        a[++sum] = b % 10;
        b /= 10;
    }
    for(int i = 1; i <= sum /2; i++)
    {
        if(a[i] != a[sum - i + 1])
        {
            return 0;
        }
    }
    return 1;
}

int main()
{
    int t,a,b;
    int T = 1;
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d%d",&a,&b);
        printf("Case #%d: ",T++);
        int ans = 0;
        for(int i = 1; i * i <= b; i++)
        {
            if(i * i >= a && judge(i * i) && judge(i))
            {
                ans++;
            }
        }
        printf("%d\n",ans);
    }
    return 0;
}
