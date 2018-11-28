#include <stdio.h>
#include <algorithm>
#include <limits.h>
#include <memory.h>
#include <math.h>
#include <list>
#include <set>
#include <vector>
#include <map>

using namespace std;
int T;
int N,A;
int input[110];

int solve(int value,int index)
{
	if(index == N)
		return 0;
	if(input[index] < value)
		return solve(value+input[index],index+1);
	
	int ovalue = value;
	int count = 0;
	while(ovalue <= input[index])
	{
		ovalue += (ovalue-1);
		count++;
	}
	return min(solve(ovalue+input[index],index+1)+count,solve(value,index+1)+1);	
}


int main()
{
	scanf("%d",&T);
	for(int i = 0; i<  T;i++)
	{
		scanf("%d %d",&A,&N);
		
		for(int j =0; j < N;j++)
			scanf("%d",&input[j]);
		
		sort(input,input+N);
		int result;
		if(A == 1)
			result = N;
		else
			result = solve(A,0);
		
		printf("Case #%d: %d",i+1,result);
				
		printf("\n");
	}
	
	return 0;
}
