#include<iostream>
#include<algorithm>
#include<stdio.h>
using namespace std;
int main()
{
    int T,a,N,i,j,k,x,y,war,dwar;
    scanf("%d",&T);
    for(a=1;a<=T;a++)
    {
        scanf("%d",&N);
        float arr1[N],arr2[N];
        for(i=0;i<N;i++)
            scanf("%f",&arr1[i]);
        for(i=0;i<N;i++)
            scanf("%f",&arr2[i]);
        sort(arr1,arr1+N);
        sort(arr2,arr2+N);
        k=N-1;j=0;i=N-1;
        war=0;
        while(j<=k)
        {
            if(arr1[i]>arr2[k])
            {
                j++;
                i--;
                war++;
            }
            else
            {
                i--;
                k--;
            }
        }
        
        i=N-1;x=0;y=N-1;dwar=0;
        while(x<=y)
        {
            if(arr1[y]>arr2[i])
            {
                i--;
                y--;
                dwar++;
            }
            else
            {
                i--;
                x++;
            }
        }
        printf("Case #%d: %d %d\n",a,dwar,war);
    }
    return 0;
}
