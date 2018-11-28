#include <stdio.h>
#include <mem.h>

int mat_in[100][100];
int mat_out[100][100];

int main(int argc, char *argv[])
{
	int i,j,k,m,n;
	int T, isequal;
    	  	  	   		
	scanf("%d", &T);
	for(i=0;i<T;i++)
	{
		scanf("%d%d",&m,&n);
		for(j=0;j<m;j++)
        	for(k=0;k<n;k++)
				scanf("%d", &mat_in[j][k]);

		for(j=0;j<m;j++)
        	for(k=0;k<n;k++)
				mat_out[j][k]=100;

		for(j=0;j<m;j++)
		{
			int max = 1;
        	for(k=0;k<n;k++)
			{
				if(mat_in[j][k] > max)
					max = mat_in[j][k];
			} 
        	for(k=0;k<n;k++)
			{
				if(mat_out[j][k] > max)
					mat_out[j][k]=max;
			}
		}		
		for(k=0;k<n;k++)
		{
			int max = 1;
        	for(j=0;j<m;j++)
			{
				if(mat_in[j][k] > max)
					max = mat_in[j][k];
			} 
        	for(j=0;j<m;j++)
			{
				if(mat_out[j][k] > max)
					mat_out[j][k]=max;
			}
		}		

		isequal = 1;
		for(j=0;j<m;j++)
        	for(k=0;k<n;k++)
				if(mat_in[j][k] != mat_out[j][k])
					isequal = 0;
					
/*		for(j=0;j<m;j++)
		{
        	for(k=0;k<n;k++)
				printf("%d ", mat_out[j][k]);
			printf("\n");
		}
*/
		if(isequal)
		{
			printf("Case #%d: YES\n",i+1);
		}
		else
		{
			printf("Case #%d: NO\n",i+1);
		}
	}
	return 0;
}
