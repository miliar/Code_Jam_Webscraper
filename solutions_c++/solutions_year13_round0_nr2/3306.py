# include<stdio.h>
# include<stdlib.h>
# include<string.h>

FILE *input,*output;
int N,M;
int check(int matrix[105][105],int*a,int*b)
{
	int i,j;
	for(i=0;i<N;i++)
	{
		for(j=0;j<M;j++)
		{
			if(matrix[i][j]!=a[i] && matrix[i][j] != b[j] )
			return 0;
		}
	}
	return 1;
}

int main()
{
	int matrix[105][105];
	int a[105],sum=0,max,j;
	int b[105];


	int i,t,T;
	 input  = fopen("F:\Lawn.in","r");
	 output = fopen("F:\output.txt","w");
	fscanf(input,"%d",&T);
	
	
	for(t=1;t<=T;t++)
	{
		memset(a,0,sizeof(a));
		memset(b,0,sizeof(b));
		
		fprintf(output,"Case #%d: ",t);
		
		fscanf(input,"%d%d",&N,&M);
		
	
		
		for(i=0;i<N;i++)
		{
			for(j=0;j<M;j++)
				fscanf(input,"%d",&matrix[i][j]);
			
		}
		
		
		for(i=0;i<N;i++)
		{
			max = matrix[i][0];
			for(j=0;j<M;j++)
			{
				if(matrix[i][j] > max)
					max = matrix[i][j];				
			}
			
			a[i] = max;		
			
		}
		
		for(i=0;i<M;i++)
		{
			max = matrix[0][i];
			for(j=0;j<N;j++)
			{
				if(matrix[j][i] > max)
					max = matrix[j][i];				
			}
			
			b[i] = max;		
			
		}
	
		if(check(matrix,a,b))
		{
			char* str = "YES\n";
			fprintf(output,"%s",str);
		}	
		else
		{
			char* str = "NO\n";
			fprintf(output,"%s",str);
		}
		
		
	
	
	}
return 0;	
}
