#include <stdio.h>

void quicksort(float x[],int first,int last)
{   
int pivot, j , i;
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
    freopen("D-large.in","r",stdin);
    freopen("D-large.out","w",stdout);
    int t,cas=1;
    scanf("%d",&t);
    while(t--)
    {
    int match=0,match1=0,i,n,j;
    scanf("%d",&n);
    float a[n],b[n];
    for(i=0;i<n;i++)
    scanf("%f",&a[i]);  
    for(i=0;i<n;i++)
    scanf("%f",&b[i]);
    quicksort(a,0,n-1);
    quicksort(b,0,n-1);
    j=n-1;
    for(i=n-1;i>=0;i--)
    {
         if(a[i]>b[j])
         {match++;}
         else
         {j--;}
    }
    j=n-1;
    for(i=n-1;i>=0;i--)
    {
         if(a[j]>b[i])
         {match1++;j--;}                   
    }
    printf("Case #%d: %d %d\n",cas,match1,match);
    cas++;
    }
    return 0;    
}
