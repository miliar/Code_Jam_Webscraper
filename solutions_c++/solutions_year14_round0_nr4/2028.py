#include<stdio.h>
#include<math.h>
#include<string.h>
#include<stdlib.h>
#include<ctype.h>
#include<vector>
#include<algorithm>
#include<map>
#include<queue>
#include<set>
#include<limits.h>
#include<iostream>
using namespace std;
int main()
{
    ios::sync_with_stdio(false);
    freopen("D-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,b;
    scanf("%d",&t);
    for(b=1;b<=t;b++)
    {
        int n,i,w=0,dec=0,k;
        int p;
        int visited[1005]={0};
        scanf("%d",&n);
        double naomi[1005],ken[1005];
        for(i=0;i<n;i++)
            scanf("%lf",&naomi[i]);
        for(i=0;i<n;i++)
            scanf("%lf",&ken[i]);
        sort(naomi,naomi+n);
        sort(ken,ken+n);
        int j=0;
        i=0;
        while(i<n)
        {
            if(naomi[i]<ken[j])
            {
            while(i<n&&naomi[i]<ken[j])
            i++;
            if(i>=n)
                break;
            }
            else
            {
                i++;
                dec++;
                j++;
            }
        }
        k=n-1;
        i=0;j=n-1;
        double curr;
        while(k>=0)
        {
            curr=naomi[k];
            while(1)
            {
                p=upper_bound(ken,ken+n,curr)-ken;
                if(!visited[p]||p>=n)
                    break;
                else
                    curr=ken[p];
            }
            if(p<n)
            {
                visited[p]=1;
            }
            else
            {
                visited[i]=1;
                i++;
                w++;
            }
            k--;

        }
        printf("Case #%d: %d %d\n",b,dec,w);

    }

}
