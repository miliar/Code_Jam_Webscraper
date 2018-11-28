#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <stack>
#include <bitset>
#define INF 1000000005
#define eps 1e-9
#define PI acos(-1.0)
#define K (0.017453292519943295769236907684886l)
#define LL long long

using namespace std;

const int maxn=1005;

int n,a[maxn],top;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int T,cas=0;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d",&n);
        top=0;
        for (int i=1;i<=n;i++)
            {
                scanf("%d",&a[i]);
                top=max(top,a[i]);
                //printf("%d\n",a[i]);
            }
        int ans=INF;
        for (int i=top;i>=1;i--)
        {
            int temp=0;
            for (int j=1;j<=n;j++)
            {
                if (a[j]>i)
                {
                    int num=a[j]-i;
                    if (num%i==0) num=num/i; else num=num/i+1;
                    temp+=num;
                }
            }
            ans=min(ans,i+temp);
        }
        printf("Case #%d: %d\n",++cas,ans);
    }
    return 0;
}
