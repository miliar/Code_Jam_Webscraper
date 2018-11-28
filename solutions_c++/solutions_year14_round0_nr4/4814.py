#include <iostream>
#include<cmath>
#include<cstdio>
#include<cstring>

using namespace std;

int main()
{
    int t,n,k=0,cnt,cnt1;
    double arr1[11],arr2[11],arr3[11],arr4[11];
    FILE *q;
    q=fopen("suraj1.txt","w");

    scanf("%d",&n);
    while(n--)
    {
       scanf("%d",&t);
       for(int i=0;i<t;i++)
            cin>>arr1[i];
       for(int i=0;i<t;i++)
            cin>>arr2[i];
       for( int i=1;i<t ;i++ )
       {
            for( int j=0; j<t-1; j++)
            {
                if(arr1[j] > arr1[j+1])
                {
                    double temp;
                    temp = arr1[j];
                    arr1[j] = arr1[j+1];
                    arr1[j+1] = temp;
                }
                if(arr2[j] > arr2[j+1])
                {
                    double temp;
                    temp = arr2[j];
                    arr2[j] = arr2[j+1];
                    arr2[j+1] = temp;
                }
            }
        }
         for(int i=0;i<t;i++)
         {
             arr3[i]=arr1[i];
             arr4[i]=arr2[i];
         }
         cnt=0;
         cnt1=t;
         for( int i=0;i<t ;i++ )
         {
            for( int j=0; j<t; j++)
            {
                if(arr1[i]>arr2[j])
                {
                    arr2[j]=99.0;
                    cnt++;
                    break;
                }
            }
         }
          for( int i=0;i<t ;i++ )
         {
            for( int j=0; j<t; j++)
            {
                if(arr3[i]<arr4[j])
                {
                    arr4[j]=-99.0;
                    cnt1--;
                    break;
                }
            }
         }
        k++;
        fprintf(q,"Case #%d: %d %d\n",k,cnt,cnt1);
    }
    fclose(q);
    return 0;
}
