#include<stdio.h>
#include<stdlib.h>
#include<algorithm>

using namespace std;

double naomi[1010],ken[1010];

int main()
{
    freopen("war-l.in","rt",stdin);
    freopen("war-l.out","wt",stdout);
    int i,j,tcase,t,n,deceitful,war;
    scanf("%d",&tcase);
    for(t=1;t<=tcase;t++)
    {
        scanf("%d",&n);
        for(i=0;i<n;i++)
            scanf("%lf",&naomi[i]);
        for(i=0;i<n;i++)
            scanf("%lf",&ken[i]);
        sort(naomi,naomi+n);
        sort(ken,ken+n);
        i = n-1;
        j = n-1;
        deceitful = 0;
        while(i>=0 && j>=0)
        {
            if(naomi[i] > ken[j])
            {
                i--;
                j--;
                deceitful++;
            }
            else
                j--;

        }
        i = 0;
        j = 0;
        war = n;
        while(i<n && j<n)
        {
            if(naomi[i] < ken[j])
            {
                i++;
                j++;
                war--;
            }
            else
                j++;
        }
        printf("Case #%d: %d %d\n",t,deceitful,war);
    }
    return 0;
}
