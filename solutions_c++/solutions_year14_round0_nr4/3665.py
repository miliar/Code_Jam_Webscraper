#include<stdio.h>
#include<algorithm>
#include<stdlib.h>
using namespace std;
int main()
{
    int t,n,z,i,dwar,war,j,k;
    double naomi[1009];
    double ken[1009];
    FILE *fp=fopen("out.txt","w");
    FILE *in=fopen("D-large.in","r");
    fscanf(in,"%d",&t);
    //scanf("%d",&t);
    for(z=1;z<=t;z++)
    {
        war=0;
        dwar=0;
        fscanf(in,"%d",&n);
        //scanf("%d",&n);
        for(i=0;i<n;i++)
        {
            fscanf(in,"%lf",&naomi[i]);
            //scanf("%lf",&naomi[i]);
        }
        for(i=0;i<n;i++)
        {
            fscanf(in,"%lf",&ken[i]);
            //scanf("%lf",&ken[i]);
        }
        sort(naomi,naomi+n);
        sort(ken,ken+n);
        j=0;
        k=n-1;
        for(i=n-1;i>=0;i--)
        {
            if(naomi[i]>ken[k])
            {
                j++;
                war++;
            }
            else
                k--;
        }
        j=0;
        for(i=0;i<n;i++)
        {
            if(naomi[i]>ken[j])
            {
                dwar++;
                j++;
            }
        }
        fprintf(fp,"Case #%d: %d %d\n",z,dwar,war);
    }
    return 0;
}
