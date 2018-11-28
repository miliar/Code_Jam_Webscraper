/*
 * Solution to Problem A. Counting Sheep
 */

#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <iterator>

using namespace std;

int main() {
	int T;
	long long int N, temp, temp2;  // starting number	
	scanf("%d",&T);  // number of test cases
	for(int i=0; i<T ; i++)
	{
		int ref[10];
		for(int k=0;k<10;k++)
		{
			ref[k]=0;
		}
		cin>>N;
		
		if(N==0)
		{
			printf("Case #%d: INSOMNIA\n", i+1);
			continue;
		}
		else
		{
			temp = N;
			here:
			temp2 = temp;			
			while(temp2>0)
			{
				ref[temp2%10] = 1;
				temp2 = temp2/10;
			}
			int total=0;
			for(int k=0; k<10; k++)
			{
				if(ref[k]==1)
					total+= 1;
			}
			if(total!=10) 
			{
				temp = temp+N;
				goto here;
			}
			printf("Case #%d: %llu\n",i+1, temp);
		}
	}
	return 0;
}
