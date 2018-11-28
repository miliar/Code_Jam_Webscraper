#include<iostream>
#include<stdio.h>
#include<algorithm>
using namespace std;

int main()
{
    int T,N,t,j,k,i,a;
    scanf("%d",&T);
    for(t=1;t<=T;t++)
    {
        int arr[2510];
        for(i=0;i<2500;i++)
            arr[i]=0;
        scanf("%d",&N);
        for(i=0;i<(2*N-1);i++)
        {
            for(j=0;j<N;j++)
            {
                scanf("%d",&a);
                k++;
                arr[a-1]++;
            }
        }
        printf("Case #%d: ",t);
        for(i=0;i<2500;i++)
        {
            if(arr[i]%2!=0)
                printf("%d ",i+1);
        }
        printf("\n");
    }
    return 0;
}
