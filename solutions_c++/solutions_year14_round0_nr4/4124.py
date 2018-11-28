#include<iostream>
#include<cstdio>

void merge(float *, int , int ,int);
void mergesort(float* a,int low, int high)
{
    int mid;
    if (low < high)
    {
        mid=(low+high)/2;
        mergesort(a,low,mid);
        mergesort(a,mid+1,high);
        merge(a,low,high,mid);
    }
    
}
void merge(float *a, int low, int high, int mid)
{
    int i, j, k;float c[1005];
    i = low;
    k = low;
    j = mid + 1;
    while (i <= mid && j <= high)
    {
        if (a[i] < a[j])
        {
            c[k] = a[i];
            k++;
            i++;
        }
        else
        {
            c[k] = a[j];
            k++;
            j++;
        }
    }
    while (i <= mid)
    {
        c[k] = a[i];
        k++;
        i++;
    }
    while (j <= high)
    {
        c[k] = a[j];
        k++;
        j++;
    }
    for (i = low; i < k; i++)
    {
        a[i] = c[i];
    }
}
using namespace std;
int main()
{
	int t,n,i,cou,ans1,j,ans2,l;float ni[1005],ken[1005];
	scanf("%d",&t);cou=0;
	while(t--)
	{
		//printf("love");
		ans1=0;ans2=0;
		cou++;
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			scanf("%f",&ni[i]);
		}
		for(i=0;i<n;i++)
		{
			scanf("%f",&ken[i]);
		}
		mergesort(ni,0,n-1);mergesort(ken,0,n-1);
		/*for(i=0;i<n;i++)
		{
			printf("%f  ",ni[i]);
		}
		printf("\n");
		for(i=0;i<n;i++)
		{
			printf("%f  ",ken[i]);
		}
		printf("\n");*/
		j=0;l=0;
		for(i=0;i<n;i++)
		{
			if(ni[i]>ken[j])
			{
				l=1;
				while(j<n && ni[i]>ken[j])
				{
					j++;
				}
			}
			else
			{
				j++;
			}
			if(j==n)
			{
				ans2=(n-1)-i+l;break;
			}
		}
		j=0;
		for(i=0;i<n;i++)
		{
			if(ni[i]>ken[j] && j<n)
			{
				ans1++;j++;
			}
		}
	//	printf("%d\n",ans2);
	cout<<"Case #"<<cou<<": "<<ans1<<" "<<ans2<<endl;
	}
	return 0;
}
