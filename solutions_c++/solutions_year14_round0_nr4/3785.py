#include<stdio.h>
#include<fstream>
using namespace std;
double A[1000],B[1000];
int war,dwar;
void merge(double *a, int low, int high, int mid)
{
    int i, j, k;
	double c[1000];
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

void mergesort(double *a, int low, int high)
{
    int mid;
    if (low < high)
    {
        mid=(low+high)/2;
        mergesort(a,low,mid);
        mergesort(a,mid+1,high);
        merge(a,low,high,mid);
    }
    return;
}

void getwar(int n)
{
	war=0;
dwar=0;
int i=0,j=0;
while(i<n&&j<n)
{
if(A[i]<B[j])
{
i++;
j++;
war++;
}
else
j++;
}
war=n-war;
i=n-1;
j=n-1;
while(i>=0&&j>=0)
{
    if(A[i]>B[j])
    {
        i--;
        j--;
        dwar++;
    }
    else
        j--;
}
}

int main()
{
FILE *P,*Q;
P=fopen("input.in","r+");
Q=fopen("output.in","w+");
int t,i,n,j=1;
fscanf(P,"%d",&t);
while(j<=t)
{
fscanf(P,"%d",&n);
for(i=0;i<n;i++)
fscanf(P,"%lf",&A[i]);
for(i=0;i<n;i++)
fscanf(P,"%lf",&B[i]);
mergesort(A,0,n-1);
mergesort(B,0,n-1);
getwar(n);

fprintf(Q,"Case #%d: %d %d\n",j,dwar,war);
j++;
}
fclose(P);
fclose(Q);
return 0;
}
