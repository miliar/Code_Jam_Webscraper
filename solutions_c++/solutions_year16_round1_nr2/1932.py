#include <stdio.h>
using namespace std;
void merge(int arr[], int l, int m, int r);
 
// Utility function to find minimum of two integers
int min(int x, int y) { return (x<y)? x :y; }
void mergeSort(int arr[], int n)
{
   int curr_size;  // For current size of subarrays to be merged
                   // curr_size varies from 1 to n/2
   int left_start;
   for (curr_size=1; curr_size<=n-1; curr_size = 2*curr_size)
   {
       // Pick starting point of different subarrays of current size
       for (left_start=0; left_start<n-1; left_start += 2*curr_size)
       {
           // Find ending point of left subarray. mid+1 is starting 
           // point of right
           int mid = left_start + curr_size - 1;
 
           int right_end = min(left_start + 2*curr_size - 1, n-1);
 
           // Merge Subarrays arr[left_start...mid] & arr[mid+1...right_end]
           merge(arr, left_start, mid, right_end);
       }
   }
}
 
/* Function to merge the two haves arr[l..m] and arr[m+1..r] of array arr[] */
void merge(int arr[], int l, int m, int r)
{
    int i, j, k;
    int n1 = m - l + 1;
    int n2 =  r - m;
 
    /* create temp arrays */
    int L[n1], R[n2];
 
    /* Copy data to temp arrays L[] and R[] */
    for (i = 0; i < n1; i++)
        L[i] = arr[l + i];
    for (j = 0; j < n2; j++)
        R[j] = arr[m + 1+ j];
 
    /* Merge the temp arrays back into arr[l..r]*/
    i = 0;
    j = 0;
    k = l;
    while (i < n1 && j < n2)
    {
        if (L[i] <= R[j])
        {
            arr[k] = L[i];
            i++;
        }
        else
        {
            arr[k] = R[j];
            j++;
        }
        k++;
    }
 
    /* Copy the remaining elements of L[], if there are any */
    while (i < n1)
    {
        arr[k] = L[i];
        i++;
        k++;
    }
 
    /* Copy the remaining elements of R[], if there are any */
    while (j < n2)
    {
        arr[k] = R[j];
        j++;
        k++;
    }
}
void printArray(int A[], int size)
{
    int i;
    for (i=0; i < size; i++)
        printf("%d ", A[i]);
    printf("\n");
}
int main() {
	int t,d;
	freopen("one.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&t);
	d=t;
	while(t--){
	    int n;
	    int a[2600];
	    int i=0;
	    for(i =0;i<2600;i++){
	        a[i]=0;
	    }
	    scanf("%d",&n);
	    int b;
	    for(i=0;i<((2*n-1)*n);i++){
	        scanf("%d",&b);
	        a[b]++;
	    }
	    int rs[100];
	    int k=0;
	    for(i=0;i<2600;i++){
	        if(a[i]%2==1){
	            rs[k++]=i;
	        }
	    }
	    mergeSort(rs,k);
	    printf("Case #%d: ",(d-t));
	    printArray(rs,k);
	}
	return 0;
}

