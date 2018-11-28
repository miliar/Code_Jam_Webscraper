#include<stdio.h>
#include<conio.h>
#include<string.h>
#include<math.h>
typedef int bool;
int true=1,false=0;

void swap(int* a, int* b)
{
    int t = *a;
    *a = *b;
    *b = t;
}
int partition (int arr[], int l, int h)
{
    int x = arr[h];
    int i = (l - 1);

    for (int j = l; j <= h- 1; j++)
    {
	// If current element is smaller than or equal to pivot
	if (arr[j] <= x)
	{
	    i++;    // increment index of smaller element
	    swap(&arr[i], &arr[j]);  // Swap current element with index
	}
    }
    swap(&arr[i + 1], &arr[h]);
    return (i + 1);
}
void quickSort(int arr[], int l, int h)
{
    if (l < h)
    {
	int p = partition(arr, l, h); /* Partitioning index */
	quickSort(arr, l, p - 1);
	quickSort(arr, p + 1, h);
    }
}
bool isSubsetSum(int set[], int n, int sum)
{
   // Base Cases
   if (sum == 0)
     return true;
   if (n == 0 && sum != 0)
     return false;

   // If last element is greater than sum, then ignore it
   if (set[n-1] > sum)
     return isSubsetSum(set, n-1, sum);

   /* else, check if sum can be obtained by any of the following
      (a) including the last element
      (b) excluding the last element   */
   return isSubsetSum(set, n-1, sum) || isSubsetSum(set, n-1, sum-set[n-1]);
}


int logic(int c,int d,int v,int set[])
{

	int sum;
	int n=d;
	for(sum=1;sum<=v;sum++)
	{
		quickSort(set,0,n-1);
		if (isSubsetSum(set,n, sum) == true);
		else
		set[n++]=sum;
	}
  return n-d;
}
void inputoutput(char inputfile[],char outputfile[])
{
	FILE *f1,*f2;
	int D,C,V;
	f1=fopen(inputfile,"r");
	f2=fopen(outputfile,"w");
	int no_case,set[200];
	fscanf(f1,"%d",&no_case);
	for(int i=1;i<=no_case;i++)
	{
	  fprintf(f2,"case #%d: ",i);
	  fscanf(f1,"%d%d%d",&C,&D,&V) ;
	  for(int i=0;i<D;i++)
	  fscanf(f1,"%d",&set[i]);
	  fprintf(f2,"%d\n",logic(C,D,V,set));
	}
}
int main()
{
	char inputfile[]="input.txt";
	char outputfile[]="output.txt";
	clrscr();
	inputoutput(inputfile,outputfile);
	getch();
  return 0;
}
