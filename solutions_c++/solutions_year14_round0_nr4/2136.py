#include<stdio.h>
#include<iostream> 

// A utility function to swap two elements
void swap ( float* a, float* b )
{
    float t = *a;
    *a = *b;
    *b = t;
}
 
/* This function is same in both iterative and recursive*/
int partition (float arr[], int l, int h)
{
    float x = arr[h];
    int i = (l - 1);
 
    for (int j = l; j <= h- 1; j++)
    {
        if (arr[j] <= x)
        {
            i++;
            swap (&arr[i], &arr[j]);
        }
    }
    swap (&arr[i + 1], &arr[h]);
    return (i + 1);
}
 
void quickSortIterative(float arr[], int l, int h)
{
    // Create an auxiliary stack
    int stack[ h - l + 1 ];
 
    // initialize top of stack
    int top = -1;
 
    // push initial values of l and h to stack
    stack[ ++top ] = l;
    stack[ ++top ] = h;
 
    // Keep popping from stack while is not empty
    while ( top >= 0 )
    {
        // Pop h and l
        h = stack[ top-- ];
        l = stack[ top-- ];
 
        // Set pivot element at its correct position in sorted array
        int p = partition( arr, l, h );
 
        // If there are elements on left side of pivot, then push left
        // side to stack
        if ( p-1 > l )
        {
            stack[ ++top ] = l;
            stack[ ++top ] = p - 1;
        }
 
        // If there are elements on right side of pivot, then push right
        // side to stack
        if ( p+1 < h )
        {
            stack[ ++top ] = p + 1;
            stack[ ++top ] = h;
        }
    }
}


int main()
{
    freopen("D-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    float a[1000],b[1000];
    int i,k,test,n,j,res1,res2,count,count1;
    scanf("%d",&test);
    for(i=0;i<test;i++)
    {
    	res1=res2=count=count1=0;
        scanf("%d",&n);
        for(j=0;j<n;j++)
        scanf("%f",&a[j]);
        for(j=0;j<n;j++)
        scanf("%f",&b[j]);
        quickSortIterative(a,0,n-1);
        quickSortIterative(b,0,n-1);
  //      quickSort(b,0,n-1);
     
        //for(j=0;j<n;j++)
        //{
        	//printf("%f\t",a[j]);
        //	printf("%f",b[j]);
        //}
    
        //printf("\n");
        
        for(j=0;j<n;j++)
        {
        	if(a[j]<b[0])
        	count++;
        	else
        	break;
        }
		 
	//	printf("%d\n",count); 
		for(j=count;j<n;j++)
		{
			if(a[j]>b[j-count])
			res1++;
			else
			count++;
		}
        

            j=0;
            k=0;
        	while(k<n)
        	{
        		if(a[j]<b[k])
        		{
        			count1++;
        			j++;
        		}
        	
        		k++;
			}
		res2=n-count1;
        
        printf("Case #%d: %d %d\n",i+1,res1,res2);
    }
    return 0;
}




