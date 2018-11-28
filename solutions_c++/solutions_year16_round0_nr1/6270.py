/*int main2016num(int argc,char **argv);*/
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

#define FILEIO

void numtobit(int n,int array[10])
{
	while(n > 0)
	{
		int k = n%10;
		n=n/10;
		array[k]=1;
	}
}

int isFallSleep(int array[10])
{
	int result = 1;

	for(int i=0;i<10;i++)
	{
		if(array[i] == 0)
		{
			result = 0;
			break;
		}
	}
	return result;
}

int main(int argc,char **argv) 
{ 

#ifdef FILEIO
	freopen("in.txt","r",stdin); 
	freopen("out.txt","w",stdout); 
#endif

	int N;
	int array[10] = {0};

	scanf("%d\n",&N);

	int n;
	int count = 1;
	for(int i=0;i<N;i++)
	{
		scanf("%d\n",&n);
		count = 1;
		memset(array,0,sizeof(int)*10);
		
		if(n==0) {printf("Case #%d: INSOMNIA\n",(i+1));continue;}

		while(1)
		{
			numtobit(count*n,array);

			if(isFallSleep(array))
			{
				printf("Case #%d: %d\n",(i+1),count*n);
				break;
			}

			count++;
		}
	}

#ifdef FILEIO
	fclose(stdin);
	fclose(stdout);
#endif  

	return 0; 
}
