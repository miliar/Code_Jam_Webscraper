#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <string.h>
long i,j,k,m,t;
long r,c,n,tmp;

int height[3000];
int result[100];
int main()  
{


    int size,len;
    int tmp;

    scanf("%ld",&t);


    for(m=1;m<=t;m++)
    {   

        printf( "Case #%ld: ",m);
        scanf("%ld",&n);
        for(i=0;i<=3000;i++)  height[i]=0;
        for(i=0;i<n*(2*n-1);i++)
        {
         scanf("%ld",&tmp);
         height[tmp]^=1;
        }
        k=0;
        for(i=0;i<3000;i++)  if (height[i]==1) {
            result[k++]=i;
        }
        for(i=0;i<k;i++)
            for(j=i+1
                ;j<k;j++)
            {
                if(result[i]>result[j])  tmp=result[i],result[i]=result[j],result[j]=tmp;
            }
        for(i=0;i<k;i++)
            printf( "%d ",result[i] );
        printf( "\n");
    }   
 
    return 0;
}
