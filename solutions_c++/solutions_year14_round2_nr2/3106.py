#include <iostream>
using namespace std;
#include<stdio.h>
int main() {
	// your code goes here
	int T;
	scanf("%d",&T);
    for(int t=1;t<=T;t++)
    {
    	int count=0;
        printf("Case #%d: ",t);
        int A,B,K;
        scanf("%d %d %d",&A,&B,&K);
        for(int i=0;i<A;i++)
        {
        	for(int j=0;j<B;j++)
        	if((i & j) <K) count++;
        }
        printf("%d\n",count);
    }
		return 0;
}
