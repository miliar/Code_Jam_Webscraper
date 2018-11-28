#include<iostream>
#include<stdio.h>
#include<algorithm>
using namespace std;
int main()
{
     int t,i,j,r1,r2,c1,c2,t1;
     cin>>t;
     int n;
     double arr[1000];
     double brr[1000];
     int l=t;
     while(t--)
     {
         cin>>n;
         c1=0,c2=0;
         for(i=0;i<n;i++)
         {
            cin>>arr[i];
         }
         for(i=0;i<n;i++)
         {
            cin>>brr[i];
         }
         sort(arr,arr+n);
         sort(brr,brr+n);
         t1=0;
         for(i=0;i<n;i++)
         {
             for(j=t1;j<n;j++)
                {
                    if(arr[i]<brr[j])
                    {

                        c1++;
                        t1=j+1;
                        if(j==n-1)
                          t1=n;
                        break;
                    }
                }

         }
         r2=n-c1;

         t1=0;
         for(i=0;i<n;i++)
         {

             for(j=t1;j<n;j++)
                {
                    if(arr[i]<brr[j])
                    {

                        break;
                    }
                    else if(arr[i]>brr[j])
                    {
                        c2++;
                        t1=j+1;
                        if(j==n-1)
                            t1=n;
                        break;
                    }
                }

         }

         r1=c2;

         printf("Case #%d: %d %d\n",l-t,r1,r2);
     }
    return 0;
}
