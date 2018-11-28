#include<iostream>
#include<stdio.h>
#include<algorithm>
using namespace std;
int main()
{
     int test,i,j,row1,row2,cont1,cont2,t1;
     cin>>test;
     int n;
     double arr[1000];
     double brr[1000];
     int l =test;
     while(test--)
     {
         cin>>n;
          cont1=0,cont2=0;
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

                        cont1++;
                        t1=j+1;
                        if(j==n-1)
                          t1=n;
                        break;
                    }
                }

         }
         row2=n-cont1;

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
                        cont2++;
                        t1=j+1;
                        if(j==n-1)
                            t1=n;
                        break;
                    }
                }

         }

         row1=cont2;

         printf("Case #%d: %d %d\n",l-test,row1,row2);
     }
    return 0;
}
