#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<cstring>
#include<algorithm>
using namespace std;

int a[1010];
int n;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int T;
    scanf("%d",&T);
    for (int t=1;t<=T;t++)
    {
        scanf("%d",&n);
        for (int i=0;i<n;i++)
            scanf("%d",&a[i]);
        int l=0,r=n-1,ans=0;
        while (l<=r)
        {
            int small=l;
            for (int j=l+1;j<=r;j++)
                if (a[j]<a[small]) small=j;
            //printf("SMALL: %d\n",small);
            if (small-l<r-small)
            {
                ans+=small-l;
                for (int j=small;j>=l;j--)
                    a[j]=a[j-1];
                l++;
            }
            else
            {
                ans+=r-small;
                for (int j=small;j<=r;j++)
                    a[j]=a[j+1];
                r--;
            }
        }
        printf("Case #%d: %d\n",t,ans);
    }

    return 0;
}
