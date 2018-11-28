#include<stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>


int main() 
{ 

#ifdef FILEIO
	freopen("in.txt","r",stdin); 
	freopen("out.txt","w",stdout); 
#endif

	int T;

	int A,B,K;
	scanf("%d",&T);

	for(int i=1;i<=T;i++)
	{
		scanf("%d",&A);
		scanf("%d",&B);
		scanf("%d",&K);
		int result = 0;

		for(int j=0;j<A;j++)
		{
			for(int k=0;k<B;k++)
			{
				if((j&k)<K)
					result++;
			}
		}
		printf("Case #%d: %d\n",i,result);
	}
	

#ifdef FILEIO
	fclose(stdin);
	fclose(stdout);
#endif  

	return 0; 
}
