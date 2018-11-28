#include<iostream>
#include<cstdio>
#include<algorithm>

using namespace std;

int main()
{
    int t,l;
    scanf("%d",&t);
    for(l=1;l<=t;l++)
    {
        int n,i,j,z=0,y=0;
        scanf("%d",&n);
        double naomi[n],ken[n];
        bool m1[n],m2[n];
        for(i=0;i<n;m2[i++]=false)
            scanf("%lf",&naomi[i]);
        for(i=0;i<n;m1[i++]=false)
            scanf("%lf",&ken[i]);
        sort(naomi,naomi+n);
        sort(ken,ken+n);
        for(i=0;i<n;i++)
        {
            for(j=0;j<n;j++)
            {
                if(naomi[i]<ken[j] && !m1[j])
                {
                    m1[j]=true;
                    break;
                }
            }
        }
        for(i=0;i<n;i++)
            if(!m1[i])
                z++;
        for(i=0;i<n;i++)
        {
            for(j=0;j<n;j++)
            {
                if(naomi[i]>ken[j] && !m2[j])
                {
                    m2[j]=true;
                    break;
                }
            }
        }
        for(i=0;i<n;i++)
            if(m2[i])
                y++;
        printf("Case #%d: %d %d\n",l,y,z);
    }

    return 0;
}
