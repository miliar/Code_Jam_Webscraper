#include<cstdio>
#include<stdlib.h>
int t,n,a,b,c;
double naomi[1111],ken[1111];
int nao(const void *a,const void *b)
{
    double *aa=(double *)a;
    double *bb=(double *)b;
    if(*aa>*bb) return 1;
    else return -1;
}
void war()
{
    int cnt1=0;
    int cnaomi[1111]= {0};
    int cken[1111]= {0};
    for(b=0; b<n; b++)
    {
        for(c=0; c<n; c++)
        {
            if(naomi[b]<ken[c]&&cnaomi[b]!=-1&&cken[c]!=-1)
            {
                cnt1++;
                cnaomi[b]=-1;
                cken[c]=-1;
                break;
            }
        }
    }
    printf("%d\n",n-cnt1);
}
void deceitful()
{
        int cnt1=0;
        int cnaomi[1111]= {0};
        int cken[1111]= {0};
        int kt=n-1;
        int kd=0;
        int nd=0;
        while(kd<kt+1)
        {
            if(naomi[nd]>ken[kd])
            {
                cnt1++;
                cnaomi[nd++]=-1;
                cken[kd++]=-1;
            }
            else
            {
                cnaomi[nd++]=-1;
                cken[kt--]=-1;
            }
        }
        printf("Case #%d: %d ",a,cnt1);
}
int main()
{
    scanf("%d",&t);
    for(a=1; a<=t; a++)
    {
        scanf("%d",&n);
        for(b=0; b<n; b++) scanf("%lf",&naomi[b]);
        for(b=0; b<n; b++) scanf("%lf",&ken[b]);
        qsort(naomi,n,sizeof(double),nao);
        qsort(ken,n,sizeof(double),nao);
        deceitful();
        war();
    }
    return 0;
}
