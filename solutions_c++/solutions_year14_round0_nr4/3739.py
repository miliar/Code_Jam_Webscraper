#include<stdio.h>
void quicksort(float x[],int first,int last){
    int pivot,j,i;
	float temp;
     if(first<last){
         pivot=first;
         i=first;
         j=last;

         while(i<j){
             while(x[i]<=x[pivot]&&i<last)
                 i++;
             while(x[j]>x[pivot])
                 j--;
             if(i<j){
                 temp=x[i];
                  x[i]=x[j];
                  x[j]=temp;
             }
         }

         temp=x[pivot];
         x[pivot]=x[j];
         x[j]=temp;
         quicksort(x,first,j-1);
         quicksort(x,j+1,last);

    }
}
int main()
{
	freopen("C:\\Users\\manish\\Desktop\\input.txt","r",stdin);
 	freopen("C:\\Users\\manish\\Desktop\\output.txt","w",stdout);
	int t,i,j,n,k,l,x,m,ans;
	scanf("%d",&t);
	for(i=0;i<t;i++)
	{
		
		scanf("%d",&n);
		float a[n],b[n],ar[n],br[n];
		for(j=0;j<n;j++)
			{scanf("%f",&a[j]);}
		for(j=0;j<n;j++)
			{scanf("%f",&b[j]);}
		quicksort(a,0,n-1);
		quicksort(b,0,n-1);x=0;
		for(j=0;j<n;j++)
		{
			ar[j]=a[j];
			br[j]=b[j];
		}
		for(j=n-1;j>=0;j--)
		{
			for(k=0;k<n;k++)
			{
				if(a[j]<b[k])
					{
						a[j]=0;
						b[k]=0;
						break;
					}
			}
			if(a[j]!=0)
			{
			a[j]=0;b[x]=0;
				x++;}
		}//printf("%d\n",x);
		ans=0;
		for(j=0;j<n;j++)
	{
		if(ar[j]!=0)
		{if(ar[j]<br[0])
			{ar[j]=0;br[n-1-j]=0;}
		}
	}
	/*for(i=0;i<n;i++)
	{
		printf("%f ",br[i]);
	}*/
	l=0;
	for(j=n-1;j>=0;j--)
	{
		if(br[j]==0)	continue;
		//qprintf("manish\n");
			for(k=0;k<n;k++)
			{
				if(ar[k]!=0)
				{
					if(ar[k]>br[j])
					{
						br[j]=0;ar[k]=0;ans++;break;
					}
				}
			}
			if(br[j]!=0)
			{
				br[j]=0;
				while(ar[l]==0)
				l++;
				ar[l]=0;
			}
	}
		printf("Case #%d: %d %d\n",i+1,ans,x);
	}
}
