#include <iostream>
#include<stdio.h>
#include<math.h>
using namespace std;

int main() 
{
int T,i,N,count,j,k,l,m;
int a[10];
scanf("%d",&T);

for(i=1;i<=T;i++)
{
scanf("%d",&N);
if(N==0)
{
    printf("Case #%d: INSOMNIA\n",i);
    continue;
}

count =0;
    for(j=0;j<10;j++)
    a[j]=0;
    k=1;
    while(count!=10)
    {
        m=k*N;
        while(m!=0)
        {
            l=m%10;
            if(a[l]==0)
            {
                a[l]=1;
                count++;
                
            }
            m=m/10;
        }
        k++;
    }
    m=(k-1)*N;
    printf("Case #%d: %d\n",i,m);
}	
return 0;
}
