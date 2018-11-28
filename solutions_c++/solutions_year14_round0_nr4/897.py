#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstdlib>
using namespace std;
double ar1[1005],ar2[1005];
int t1[1005];
int n;
int main()
{
    freopen("D-large.in","r",stdin);
    freopen("Dout.txt","w",stdout);
    int t,tc;
    scanf("%d",&t);
    for(tc=1;tc<=t;tc++)
    {
        int i,k=0;
        double x;
          scanf("%d",&n);
        for(i=0;i<n;i++)
             scanf("%lf",&ar1[i]);
        for(i=0;i<n;i++)
             scanf("%lf",&ar2[i]);
        sort(ar1,ar1+n);
        sort(ar2,ar2+n);
        for(i=0;i<n;i++)
            t1[i]=0;
        int w1=0,w2=0;
        for(i=0;i<n;i++)
        {
            if(ar1[i]>ar2[k])
            {
                w1++; k++;
            }
        }
        for(i=0;i<n;i++)
        {
            x=ar1[i];
            for(k=0;k<n;k++)
            {
                if(t1[k]==0 && ar2[k]>x)
                {  t1[k]=1;  break;  }
            }
            if(k==n)
            {
                for(k=0;k<n;k++)
                {
                    if(t1[k]==0)
                    {  t1[k]=1; w2++; break;  }
                }
            }
        }
        printf("Case #%d: %d %d\n",tc,w1,w2);
    }
    return 0;
}
