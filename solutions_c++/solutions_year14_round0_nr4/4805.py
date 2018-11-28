#include <stdio.h>

void swap(double &a,double &b)
{
    double tmp;
    tmp = a;
    a = b;
    b = tmp;
}


int part(double *a,int left,int right)
{
    double p = a[right];
    int i=left-1;
    for(int j=left;j<right;j++)
    {
        if(a[j]<=a[right])
        {
            i++;
            swap(a[j],a[i]);
        }
    }
    swap(a[i+1],a[right]);
    return i+1;
}


void qs(double *a,int left,int right)
{
    if(left == right)
        return;
    int index = part(a,left,right);
    if(index > left)
        qs(a,left,index-1);
    if(index < right)
        qs(a,index+1,right);
}

int war(double* N,double* K,int n)
{
    int j=n-1;
    int score=0;
    for(int i=n-1;i>=0;i--)
    {
        if(N[i] > K[j])
           score++;
        else
           j--;
    }
    return score;
}


int deceitfulwar(double* N,double* K,int n)
{
    int j_l=0;
    int j_r=n-1;
    int score=0;
    for(int i=0;i<n;i++)
    {
        if(N[i]<K[j_l])
           j_r--;
        else
        {
           score++;
           j_l++;
       }    
    }
    return score;
}

int main()
{
    freopen("./D-small-attempt0.in","r",stdin);
    freopen("./d.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int i=0;i<T;i++)
    {
        int n;
        double Ken[1000];
        double Naomi[1000];
        scanf("%d",&n);
        for(int j=0;j<n;j++)
                scanf("%lf",&Naomi[j]);
        for(int j=0;j<n;j++)
                scanf("%lf",&Ken[j]);
        qs(Naomi,0,n-1);
        qs(Ken,0,n-1);

        int w=war(Naomi,Ken,n);
        int dw=deceitfulwar(Naomi,Ken,n);
        printf("Case #%d: %d %d\n",i+1,dw,w);
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
