#include<iostream>
#include<stdlib.h>
#include <stdio.h>
using namespace std;
#define False 0
#define True 1
int main()
{
	int test;
	scanf("%d", &test);
	for(int t=0;t<test;t++)
	{
		int n;
		scanf("%d", &n);
		if(n!=0){
		int *found = (int*)calloc(10,sizeof(int));
		int allObtained = False;
		int i = 1;
		int number = n;
		while(allObtained != True)
		{
			n = i*number;
			int m = n;
			while(m!=0)
			{
				int	digit = m%10;
				m = m/10;
				if (found[digit] == False)
					found[digit] = True;
			}
			i++;
			for (int j=0;j<10;j++)
			{
				if(found[j] == False)
				{
					allObtained = False;
					break;
				}
				allObtained = True;
			}
		}
		printf("Case #%d: %d\n",t+1,n);
		}
		else
			printf("Case #%d: INSOMNIA\n", t+1);
	}
	return 0;
}

