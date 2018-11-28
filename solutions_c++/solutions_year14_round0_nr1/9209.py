#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <cstdlib>
using namespace std;
int a[20],b[20];
bool ch[20];
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int t,T = 1;
    scanf("%d",&t);
    while(t--)
    {
        int n;
        scanf("%d",&n);
        memset(ch,false,sizeof(ch));
        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;j++)
            {
                int x;
                scanf("%d",&x);
                a[x] = i;
                if(i==n)
                {
                    ch[x] = true;
                }
            }
        }
        scanf("%d",&n);
        int ans,sum=0;
        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;j++)
            {
                int x;
                scanf("%d",&x);
                if(i==n)
                {
                    if(ch[x])
                    {
                        sum++;
                        ans = x;
                    }
                }
            }
        }
        if(sum==0)
        {
            printf("Case #%d: Volunteer cheated!\n",T++);
        }else if(sum==1)
        {
            printf("Case #%d: %d\n",T++,ans);
        }else
        {
            printf("Case #%d: Bad magician!\n",T++);
        }
    }
    return 0;
}

