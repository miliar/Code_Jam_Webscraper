#include<stdio.h>
#include<stdlib.h>
int compare(const void *a,const void *b)
{
    return (*(long long int *)a - *(long long int *)b);
}
int main()
{
    long long int i,j,k,n,max,ans,t,d;
    long long int arr[1001],temp[1001],count;
    scanf("%lld",&t);
    d=1;
    while(t--)
    {
              scanf("%lld",&n);
              
              for(i=0;i<n;i++)
              scanf("%lld",&arr[i]);
              
              qsort(arr,n,sizeof(long long int),compare);
              max=arr[n-1];
              
    
    for(i=1;i<=max;i++)
    {
                        count=0;
                        for(j=0;j<n;j++)
                        {
                                        if(arr[j]%i==0)
                                        {
                                                       k=arr[j]/i;
                                                       count+=k-1;
                                        }
                                        else
                                        {
                                            k=arr[j]/i;
                                            count+=k;
                                        }
                        }
                        temp[i]=i+count;
    }
    
   // for(i=0;i<=max;i++)
   // printf("%d ",temp[i]);
    
    qsort(temp+1,max,sizeof(long long int),compare);
   // printf("\n");
    
   // for(i=0;i<=max;i++)
   // printf("%d ",temp[i]);
    
    printf("Case #%lld: %lld\n",d,temp[1]);
    d++;
}
                                        
                       return 0;
}                 
              
              
              
