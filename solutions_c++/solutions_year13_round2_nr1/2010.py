#include<stdio.h>
#include<string.h>
#include<vector>
#include<queue>
#include<iostream>
#include<stack>
//#include<conio.h>
#include<math.h>

using namespace std;

void mergesort(int *arr,int low, int mid, int high);
void split(int *arr,int low, int high)
{
     int mid;
     if(low!=high)
     {
                 mid=(low+high)/2;
                 split(arr,low,mid);
                 split(arr,mid+1,high);
                 mergesort(arr,low,mid,high);
     }
}

void mergesort(int *arr,int low, int mid, int high)
{
     int i,j,k,brr[high-low+1];
     for(i=low,j=mid+1,k=0;i<=mid &&j<=high;k++)
     {
                                              if(arr[i]<=arr[j])
                                              {brr[k]=arr[i];i++;}
                                              else if(arr[i]>=arr[j])
                                              {brr[k]=arr[j];j++;}
     }
     
     if(i>mid && j<=high)
     while(j<=high)
     {brr[k]=arr[j];j++;k++;}
     else if(j>high && i<=mid)
     while(i<=mid)
     {brr[k]=arr[i];i++;k++;}
     
     for(i=0,j=low;i<high-low+1 && j<=high;i++,j++)
     arr[j]=brr[i];
}

int main()
{
    
   freopen("input.txt","r",stdin);
   //freopen("output.txt","w",stdout);
   int t,z;
   scanf("%d",&t);
   for(z=1;z<=t;z++)
   {
   int i,a,n,j;
   scanf("%d%d",&a,&n);
   int arr[110];
   for(i=0;i<n;i++)
   scanf("%d",&arr[i]);
   
   
   split(arr,0,n-1);
   //for(i=0;i<n;i++) printf("%d ",arr[i]); printf("\n");
   int ans=n;
   
   if(a==1)
   printf("Case #%d: %d\n",z,n);
   else
   {
   for(i=0;i<n;i++)
   {
                   int temp=n-i-1;
                   int size=a;
                     for(j=0;j<=i;j++)
                     {
                                      if(size>arr[j]) size+=arr[j];
                                      else 
                                      {
                                           while(size<=arr[j])
                                           {size+=(size-1);temp++;}
                                           size+=arr[j];
                                      }
                     }
                     if(temp<ans) ans=temp;
                     //printf("%d ",size);
   }
   //printf("\n");
   printf("Case #%d: %d\n",z,ans);
}
   }
   //getch();
   return 0;
}
