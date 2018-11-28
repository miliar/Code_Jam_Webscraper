#include<stdio.h>


int partition(int a[],int low,int high)
{
int pivot,max,temp;
pivot=low;
max=high;
while(low<high)
{
	while(a[low]<=a[pivot] && low<max)
		low++;
	while(a[high]>a[pivot])
		high--;
	if(low<high)
	{
		temp=a[low];
		a[low]=a[high];
		a[high]=temp;
	}
	
}
temp=a[pivot];
a[pivot]=a[high];
a[high]=temp;

return high;
}

void quicksort(int a[],int low,int high)
{
int pos;
if(low>=high)
	return;
 pos=partition(a,low,high);
 quicksort(a,low,pos-1);
 quicksort(a,pos+1,high);
 
}  

int op_required(int mote,int max)
{
int op=0;
	while(mote<=max)
	{
		mote=mote+mote-1;
		op++;
	}	
return  op;
}




int main()
{

	int a[1000001],t,i,j,op,n;
	unsigned long long mote;
	scanf("%d",&t);
	
	for(i=1;i<=t;i++)
	{
		op=0;
		scanf("%llu%d",&mote,&n);
		for(j=0;j<n;j++)
			scanf("%d",a+j);
		if(mote==1)
			printf("Case #%d: %d\n",i,n);
		else
		{
		
			quicksort(a,0,n-1);
			j=0;
			while(j<n)
			{
				if(a[j]<mote)
				{
					mote=mote+a[j];
					j++;
				}
				else
				{
					if(op_required(mote,a[j])>n-j)
					{
						op=op+n-j;
						break;
					}
					else
					{				
						mote=mote+mote-1;
						op++;
					}
				}
			}
		printf("Case #%d: %d\n",i,op);
		}
		
	}
 return 0;
}
			
			
			
			
			
			
			
			
			
			
			
		
		
		
		
		
	
