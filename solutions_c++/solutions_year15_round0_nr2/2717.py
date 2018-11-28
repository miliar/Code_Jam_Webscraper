#include<cstdio>
#include<iostream>
#include<cstring>
#include<algorithm>
using namespace std;
int N;
int A[1010];
int main()
{
    freopen("inbl.in","r",stdin);
    freopen("outbl.out","w",stdout);
    int T;
    scanf("%d",&T);
    int tt = 0;
    while(T--)
    {
        tt++;
        int ma = 0;
        scanf("%d",&N);
        for(int i=0;i<N;i++)
        {
            scanf("%d",&A[i]);
            ma = max(ma,A[i]);
        }
        int ans = ma;
        for(int k=1;k<=ma;k++)
        {
            int s = k;
            for(int i=0;i<N;i++)
            {
                s += (A[i]-1)/k;
            }
            ans = min(ans,s);
        }
        printf("Case #%d: %d\n",tt,ans);
    }
    return 0;
}
