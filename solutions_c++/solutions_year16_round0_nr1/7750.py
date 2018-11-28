
#include <iostream>
#include <list>
#include <memory.h>

int arr[10];

int main(int argc, char** argv) {
	int i,j,k,l;
	int test,T;
	long N,temp;
	int digit;
	freopen("C:\\Users\\raju\\Documents\\input.txt","r",stdin);
	freopen("C:\\Users\\raju\\Documents\\out.txt","a+",stdout);
	scanf("%d\n",&T);
	for(test=1;test<=T;test++)
	{
		scanf("%ld\n",&N);
		memset(arr,0x00,sizeof(arr) );
		
		if(N == 0)
		{
			printf("Case #%d: INSOMNIA\n",test);
			continue;
		}
		
		for(i=1;;i++)
		{
			temp = i * N;
			
			while(temp)
			{
			
				digit = temp % 10;
				arr[digit] = 1;
				temp = temp / 10;
			}//while
			
			for(j=0;j<10;j++)//check if all digits are found
			{
				if(arr[j] == 0)
				{
					break;
				}
			}
			
			if(j == 10) //all digits found
			{
				printf("Case #%d: %ld\n",test, (i*N) );
				break;
			}
		}
		
		
		
	}//test
	return 0;
}

	
