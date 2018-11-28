#include<stdio.h>
#include <stdlib.h>
#include <iostream>
using namespace std;
void quicksort(float x[100],float first,float last)
{
     int pivot, j, i;
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
    freopen ("D-large.in","r",stdin);
    freopen ("output.in","w",stdout);
    int T,x=1,u,v;
    int n,i,j,war,d_war;
    //scanf("%d",&T);
    cin>>T;
    while(x<=T)
    {
      war=0;d_war=0;
        //scanf("%d",&n);
        cin>>n;
        float arr[n+1];
        float brr[n+1];
        for(j=0;j<n;j++)
            scanf("%f",&arr[j]);
        for(j=0;j<n;j++)
            scanf("%f",&brr[j]);

        quicksort(arr,0,n-1);
        quicksort(brr,0,n-1);
        //Logic starts here
        u=n-1;v=n-1;
        i=0;j=0;
        while(u>=0)
        {
            if(arr[u]>brr[v])
                war++;
            else
                v--;
            u--;
        }
       
        while(i<n)
        {
            if(arr[i]>brr[j])
            {
                j++;
                d_war++;
            }
            i++;
        }
        cout<<"Case #"<<x<<": "<<d_war<<" "<<war<<"\n";
        //printf("Case #%d: %d %d\n",x,d_war,war);
    x++;
    }
   // system("pause");
    return 0;
}
