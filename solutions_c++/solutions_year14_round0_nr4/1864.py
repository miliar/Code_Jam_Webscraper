#include<stdio.h>
#include<iostream>
#include<cstdlib>
#include<string.h>
#include<algorithm>
using namespace std;
double na[10000];
double ke[10000];
int mark[10000];
int main()
{
    freopen("C:\\Users\\Gaurav\\Desktop\\D.in","r",stdin);
    freopen("C:\\Users\\Gaurav\\Desktop\\output.txt","w",stdout);
    int t;
    scanf("%d",&t);
    int ca=0;
    while(t--)
    {
        ca++;
        int n,i,j;
        scanf("%d",&n);
        for(i=0;i<n;i++)
        scanf("%lf",&na[i]);
        for(i=0;i<n;i++)
        scanf("%lf",&ke[i]);
        sort(na,na+n);
        sort(ke,ke+n);
        int y=0,z=n;
        memset(mark,0,sizeof(mark));
        int s=0,l=n-1;
        for(i=0;i<n;i++)
        {
            if(s>l)
            break;
            double d=na[i]-ke[s];
            if(d>0)
            {
                s++;
                y++;
            }
            else
            {
                l--;
            }
        }
        memset(mark,0,sizeof(mark));
        for(i=0;i<n;i++)
        {
            for(j=0;j<n;j++)
            {
                if(mark[j]==1)
                continue;
                double d=ke[j]-na[i];
                //printf("%lf %d\n",d,j);
                if(d>0)
                {
                    z--;
                    mark[j]=1;
                    break;
                }
            }
        }
        printf("Case #%d: %d %d\n",ca,y,z);
    }
    return 0;
}
