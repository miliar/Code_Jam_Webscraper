#include<stdio.h>
#include<algorithm>
using namespace std;
double tb[2][500],se[500],num[500];
double calc(double *a,int n)
{
    int c,p,i,j,k;
    for(j=0;j<2*n+1;j++)
    {
        tb[0][j]=0;
    }
    tb[0][n]=1;
    for(i=0;i<n;i++)
    {
//        printf("\n%d:\n",i);
        c=i%2;
        p=(i+1)%2;
        for(j=0;j<2*n+1;j++)
        {
//            printf("%d: %f\n",j,tb[c][j]);
            tb[p][j]=0;
        }
        for(j=0;j<2*n+1;j++)
        {
//            printf("%d:\n",j);
            if(j>0)
                tb[p][j-1]+=tb[c][j]*a[i];
            if(j<2*n)
                tb[p][j+1]+=tb[c][j]*(1-a[i]);
        }
    }
//    printf("\n%d:\n",i);
//    for(j=0;j<2*n+1;j++)
//    {
//        printf("%d: %f\n",j,tb[p][j]);
//    }
    return tb[p][n];
}
main()
{
    double cal,ans=0;
    int n,nk,i,j,k,nq,q;
    scanf("%d",&nq);
    for(q=1;q<=nq;q++)
    {
        ans=0;
        scanf("%d%d",&n,&nk);
        for(i=0;i<n;i++)
            scanf("%lf",&num[i]);
        sort(num,num+n);
//        printf("Sort: ");
//        for(i=0;i<n;i++)
//            printf("%.2f ",num[i]);
//        printf("\n");
//        for(i=0;i<nk/2;i++)
//        {
//            se[2*i]=num[i];
//            se[2*i+1]=num[n-i-1];
//        }
//        printf("Seleciton: ");
//        for(i=0;i<nk;i++)
//            printf("%.2f ",se[i]);
//        printf("\n");
        for(i=0;i<(1<<n);i++)
        {
            k=0;
            for(j=0;j<n;j++)
            {
                if(i&(1<<j))
                {
                    se[k++]=num[j];
                }
            }
            if(k!=nk)
                continue;
//            printf("Try %d\n",i);
            cal=calc(se,nk);
            ans=max(ans,cal);
        }
//        cal=calc(se,nk);
        printf("Case #%d: %f\n",q,ans);
    }
    return 0;
}
