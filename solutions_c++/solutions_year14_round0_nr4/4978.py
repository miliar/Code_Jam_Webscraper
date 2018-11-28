#include<stdio.h>
int t,n,flag,dcount,wcount,c,i,j,flag2;
float a1[1000],a2[1000],a12[1000],a22[1000];
void mergeSort(float arr[],int low,int mid,int high);
void partition(float arr[],int low,int high)
{
    int mid;
    if(low<high)
	{
         mid=(low+high)/2;
         partition(arr,low,mid);
         partition(arr,mid+1,high);
         mergeSort(arr,low,mid,high);
    }
}
void mergeSort(float arr[],int low,int mid,int high)
{
    int i,m,k,l;
	float temp[high];
    l=low;
    i=low;
    m=mid+1;
    while((l<=mid)&&(m<=high))
	{
         if(arr[l]<=arr[m])
		 {
             temp[i]=arr[l];
             l++;
         }
         else
		 {
             temp[i]=arr[m];
             m++;
         }
         i++;
    }
    if(l>mid)
	{
         for(k=m;k<=high;k++)
		 {
             temp[i]=arr[k];
             i++;
         }
    }
    else
	{
         for(k=l;k<=mid;k++)
		 {
             temp[i]=arr[k];
             i++;
         }
    }
    for(k=low;k<=high;k++)
	{
         arr[k]=temp[k];
    }
}
int main()
{
	c=0;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d",&n);
		for(i=0;i<n;++i)
		{
			scanf("%f",&a1[i]);
		}
		for(i=0;i<n;++i)
		{
			scanf("%f",&a2[i]);
		}
		partition(a1,0,n-1);
		partition(a2,0,n-1);
		for(i=0;i<n;++i)
			a12[i]=a1[i];
		for(i=0;i<n;++i)
			a22[i]=a2[i];
		wcount=n;
		for(i=0;i<n;++i)
		{
			flag2=0;
			for(j=0;j<n;++j)
			{
				if(a12[i]<a22[j] && flag2==0)
				{
					--wcount;
					flag=1;
					a12[i]=a22[j]=0;
					flag2=1;
				}
			}
		}
		dcount=0;
		for(i=n-1;i>=0;--i)
		{
			for(j=n-1;j>=0;--j)
			{
				if(a1[i]>a2[j] && a2[j]!=0)
				{
					a1[i]=a2[j]=0;
					++dcount;
				}
			}
		}
		++c;
		printf("Case #%d: %d %d\n",c,dcount,wcount);
	}
	return 0;
}
