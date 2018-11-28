#include<stdio.h>
int partition(int,int,int a[],int);
int quicksort(int a[],int);
int main()
{
    freopen("D-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int test,i,n,NB[1000],KB[1000],j,k,c1,c2;
    float val;
    scanf("%d",&test);
    for(i=1;i<=test;i++)
    {
        scanf("%d",&n);
        for(j=0;j<n;j++)
        {
            scanf("%f",&val);
            val*=100000;
            NB[j]=(int)val;
        }
        quicksort(NB,n);
        for(j=0;j<n;j++)
        {
            scanf("%f",&val);
            val*=100000;
            KB[j]=(int)val;
        }
        quicksort(KB,n);
        c1=0;c2=0;
        k=0;
        for(j=0;j<n;j++)
        {
            if(NB[j]>KB[k])
            {
                c1++;
                k++;
            }
        }
        k=0;
        for(j=0;j<n;j++)
        {
            if(KB[j]>NB[k])
            {
                c2++;
                k++;
            }
        }
        c2=n-c2;
        printf("Case #%d: %d %d\n",i,c1,c2);
    }
    return 0;
}
int quicksort(int arr[],int n)
{
    int sto[100][100];
    int k=-1;
    sto[++k][0]=0;
    sto[k][1]=n-1;
    int low, up,part;
    for(;k>=0;)
    {
        low=sto[k][0];
        up=sto[k][1];
        k--;
        part=partition(low,up,arr,n);
        if(part>0&&low!=part)
        {
            sto[++k][0]=low;
            sto[k][1]=part-1;
        }
        if(part<(n-1)&&up!=part)
        {
            sto[++k][0]=part+1;
            sto[k][1]=up;
        }
    }
    return 0;
}
int partition(int low,int up,int arr[],int n)
{
    int x=arr[up];
    int i=low-1,j,temp;
    for(j=low;j<=(up-1);j++)
    {
        if(arr[j]<x)
        {
            i++;
            temp=arr[j];
            arr[j]=arr[i];
            arr[i]=temp;
        }
    }
    temp=arr[i+1];
    arr[i+1]=arr[up];
    arr[up]=temp;
    return i+1;
}
