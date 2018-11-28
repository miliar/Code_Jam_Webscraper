#include<stdio.h>

int war(double*, double*, int);
int dwar(double*, double*, int);
void merge(double *, int, int, int);
void mergeSort(double *, int, int);

int main()
{
    int i,t;
    scanf("%d",&t);
    for(i=1; i<=t; i++)
    {
        int j,n;
        scanf("%d",&n);
        double ken[n],naomi[n];

        for(j=0; j<n; j++)
            scanf("%lf",&naomi[j]);
        for(j=0; j<n; j++)
            scanf("%lf",&ken[j]);

        mergeSort(ken,0,n-1);
        mergeSort(naomi,0,n-1);
        /*for(j=0; j<n; j++)
            printf("%lf %lf\n",ken[j],naomi[j]);*/
        printf("Case #%d: %d %d\n",i,dwar(ken,naomi,n), war(ken,naomi,n));
    }
    return 0;
}

int war(double ken[], double nao[], int n)
{
    int i=0,j=0,sum=0;
    while(i<n && j<n)
    {
        if(ken[i] > nao[j])
        {
            sum++;
            i++;
            j++;
        }
        else
        {
            i++;
        }
    }
    return n-sum;
}

int dwar(double ken[], double nao[], int n)
{
    int i=0,j=0,sum=0;
    while(i<n && j<n)
    {
        if(ken[i] < nao[j])
        {
            sum++;
            i++;
            j++;
        }
        else
        {
            j++;
        }
    }
    return sum;
}

void merge(double data[],int low,int high,int mid)
{
    int n = high - low +1;
    int i=0, j=low, k=mid+1;
    double temp[n];
    while(j<=mid && k <=high)
    {
        if(data[j] <= data[k] )
            temp[i++] = data[j++];
        else
            temp[i++] = data[k++];
    }
    if(j>mid)
        while(k<=high) temp[i++] = data[k++];
    else if(k>high)
        while (j<=mid) temp[i++] = data[j++];
    for(i=0;i<n;i++)
        data[low+i] = temp[i];
    return;
}

void mergeSort(double list[],int low,int high)
{
    if(high <= low) return;
    else
    {
        int mid = (low + high)/2;
        mergeSort(list,low,mid);
        mergeSort(list,mid+1,high);
        merge(list,low,high,mid);
        return;
    }
}
