#include<cstdio>
#include<cstdlib>
#include<algorithm>
using namespace std;
int main()
{
    int t=0,i=0,n=0,j=0,l,war=0,dwar=0;
    double *nl,*ke;
    scanf("%d",&t);
    for(l=0;l<t;l++)
    {
        war=0;dwar=0;
        scanf("%d",&n);
        nl=(double *)calloc(n,sizeof(double));
        ke=(double *)calloc(n,sizeof(double));
        for(i=0;i<n;i++)
            scanf("%lf",&nl[i]);
        for(i=0;i<n;i++)
            scanf("%lf",&ke[i]);
        sort(nl,nl+n);
        sort(ke,ke+n);
        j=n-1;
        i=0;
        int i2=0;
        int j2=n-1;

        while(i<=j)
        {
            if(nl[j]>ke[j2])
            {
                war++;
                j--;
                i2++;
            }
            else
            {
                j--;
                j2--;
            }
        }
        i=0;j=n-1;j2=n-1;i2=0;
        while(i<=j)
        {
            if(nl[j]>ke[j2])
            {
                dwar++;
                j--;j2--;
            }
            else
            {
                i++;j2--;
            }
        }
        printf("Case #%d: %d %d\n",l+1,dwar,war);

    }
    return 0;
}
