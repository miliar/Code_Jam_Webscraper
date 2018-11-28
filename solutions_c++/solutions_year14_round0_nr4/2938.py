#include<cstdio>
#include<algorithm>
#include<iostream>
using namespace std;
int main()
{
    int t,n,i,j,count,count1,k,f1;
    scanf("%d",&t);
    for(i=0;i<t;i++)
    {
          scanf("%d",&n);
          double a[n],b[n];
          count=0;
          count1=0;
          f1=0;
          int z[n];
          for(j=0;j<n;j++)
          {
          scanf("%lf",&a[j]);
          z[j]=0;
          }
          for(j=0;j<n;j++)
          {
          scanf("%lf",&b[j]);
          }
          sort(a,a+n);
          sort(b,b+n);
          j=0;
          k=0;
          while(j<n)
          {
             if(a[j]>b[k])
             {
             count++;
             j++;
             k++;
             }
             else
             j++;
         }
         for(j=0;j<n;j++)
         {
           for(k=0;k<n;k++)
           {
           	if(a[j]<b[k])
           	{
           		count1++;
           		b[k]=0;
           		break;
           	}
           }
         }
          printf("Case #%d: %d %d\n",i+1,count,n-count1);
   } 
          
     return 0;
}                                                
                          
                                          
                                       
                    
