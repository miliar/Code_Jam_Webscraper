#include <iostream>
using namespace std;
#include<stdio.h>
int main() {
	int T,i,j,N,l;
	int A[2501];
	scanf("%d",&T);
	for(i=1;i<=T;i++)
	{
	    scanf("%d",&N);
	    N=((2*N)-1)*N;
	    for(j=0;j<=2500;j++)
	    A[j]=0;
	    for(j=1;j<=N;j++)
	    {
	        scanf("%d",&l);
	        A[l]=A[l]+1;
	        
	        
	    }
	    printf("Case #%d: ",i);
	    
	    for(j=1;j<=2500;j++)
	    {
	        if(A[j]%2!=0)
	        {
	            printf("%d ",j);
	        }
	        
	        
	    }
	    printf("\n");
	    
	    
	}
	
	
	
	return 0;
}
