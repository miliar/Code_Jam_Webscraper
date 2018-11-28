#include <iostream>
#include <stdio.h>
using namespace std;

int main() {
	// your code goes here
	int T, S, i, cases;
	scanf("%d",&T);
	for(cases=0;cases<T;++cases)
	{
		scanf("%d",&S);
		int ans=0, tmp=0, sum=0;
		for(i=0;i<=S;++i)
		{
			scanf("%1d",&tmp);
			if(i==0) sum+=tmp;
			else
			{
				if(sum<i && tmp!=0) 
				{
					 ans+=i-sum;
					 sum = i;
				}
				sum+=tmp;
			}
		}
		printf("Case #%d: %d\n", cases+1, ans);
		
	}
	return 0;
}