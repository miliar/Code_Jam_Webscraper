#include<iostream>
#include<cstdio>
using namespace std;

void merge(double a[],int p,int q,int r)
{
    int m,n,i,j,k;
    m=q-p+1;
    n=r-q;
    double L[m+1],R[n+1];
    for(i=0;i<m;i++)
    L[i]=a[p+i];
    L[m]=2.0;
    for(j=0;j<n;j++)
    R[j]=a[q+1+j];
    R[n]=2.0;
    i=0;j=0;
    for(k=p; k<=r ;k++)
    {
        if(L[i]<R[j])
        {
            a[k]=L[i];
            i++;
        }
        else
        {
            a[k]=R[j];
            j++;
        }
    }


}


void mergesort(double a[],int p,int r)
{
    if(p<r)
    {
        int q=(p+r)/2;
        mergesort(a,p,q);
        mergesort(a,q+1,r);
        merge(a,p,q,r);
    }
}

int main()
{
    int t,ct=1;
    scanf("%d",&t);
    while(t--)
    {
        double a[50],b[50];

        int n,i,j;
        scanf("%d",&n);

        for(i=0;i<n;i++)
        scanf("%lf",&a[i]);

        for(i=0;i<n;i++)
        scanf("%lf",&b[i]);

        mergesort(a,0,n-1);
        mergesort(b,0,n-1);

        int r1=0,r2=0;

        j=0;i=0;
        for(i=0;i<n;i++)
        if(a[i]>b[j])
        {
            r1++;
            j++;
        }
        j=0;
        for(i=0;i<n;i++)
        if(b[i]>a[j])
        {
            j++;
            r2++;
        }
        r2=n-r2;

        printf("Case #%d: %d %d\n",ct,r1,r2);\
        ct++;
    }
    return 0;
}
