#include<stdio.h>
int partition(int,int,int a[],int);
int quicksort(int a[],int);
int main()
{
    freopen("D-large.in","r",stdin);
    freopen("output_D_1.txt","w",stdout);
    int test,i,n,arr1[1000],arr2[1000],j,k,counter1,counter2;
    float val;
    scanf("%d",&test);
    for(i=1;i<=test;i++)
    {
        scanf("%d",&n);
        for(j=0;j<n;j++)
        {
            scanf("%f",&val);
            val*=100000;
            arr1[j]=(int)val;
        }
        quicksort(arr1,n);
        /*for(j=0;j<n;j++)
            printf("\n%d",arr1[j]);*/
        for(j=0;j<n;j++)
        {
            scanf("%f",&val);
            val*=100000;
            arr2[j]=(int)val;
        }
        //printf("\n");
        quicksort(arr2,n);
        /*for(j=0;j<n;j++)
            printf("\n%d",arr2[j]);
        printf("\n\nn=%d",n);*/
        counter1=0;counter2=0;
        k=0;
        for(j=0;j<n;j++)
        {
            if(arr1[j]>arr2[k])
            {
                counter1++;
                k++;
            }
        }
        k=0;
        for(j=0;j<n;j++)
        {
            if(arr2[j]>arr1[k])
            {
                counter2++;
                k++;
            }
        }
        counter2=n-counter2;
        printf("Case #%d: %d %d\n",i,counter1,counter2);
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
        //printf("\nin\n");
        part=partition(low,up,arr,n);
        /*printf("\npart=%d low=%d up=%d\n",part,low,up);*/
        if(part>0&&low!=part)//low<=(part-1)
        {
            //printf("input");
            sto[++k][0]=low;
            sto[k][1]=part-1;
        }
        if(part<(n-1)&&up!=part)//up>=(part+1)
        {
            //printf("output");
            sto[++k][0]=part+1;
            sto[k][1]=up;
        }
    }
    return 0;
}
int partition(int low,int up,int arr[],int n)
{
    //printf("low=%d up=%d",low,up);
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
    //printf("partition position is %d",i+1);
    //getch();
    return i+1;
}
