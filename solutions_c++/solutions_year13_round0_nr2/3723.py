#include<cstdio>
#include<cstring>
#include<cstdlib>

using namespace std;

int main(void)
{
    int a[103][103];
    int rmax[103];
    int cmax[103];
    int yes;
    //FILE *in = fopen("in.txt","r");
    //FILE *out = fopen("out.txt","w");
    int i,j,k;
    int T;
    int n,m;
    scanf("%d",&T);
    for(i=1;i<=T;i++)
    {
        memset(a,0,sizeof(a));
        memset(rmax,0,sizeof(rmax));
        memset(cmax,0,sizeof(cmax));
        yes = 1;
        scanf("%d %d",&n,&m);

        for(j=1;j<=n;j++)
            for(k=1;k<=m;k++)
            {
                scanf("%d",&a[j][k]);
                if(a[j][k]>rmax[j])
                    rmax[j] = a[j][k];
                if(a[j][k]>cmax[k])
                    cmax[k] = a[j][k];

            }
        for(j=1;j<=n;j++)
            for(k=1;k<=m;k++)
            if(a[j][k]<rmax[j]&&a[j][k]<cmax[k])
            {
                yes = 0;
            }
        if(yes==1)
            printf("Case #%d: YES\n",i);
        else
            printf("Case #%d: NO\n",i);

    }



    return 0;
}
