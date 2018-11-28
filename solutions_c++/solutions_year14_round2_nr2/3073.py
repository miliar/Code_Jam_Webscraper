#include<iostream>
#include<stdio.h>
using namespace std;
int main() {
	int testCase;
	cin>>testCase;
	for(int i=0; i<testCase; i++)
	{
		int n=0;
	    int A,B,K;
		cin>>A>>B>>K;
		for(int x=0 ; x<A ; x++)
		{
			for(int y=0; y<B; y++)
			{
				if((x & y)<K) n++;
			}
		}
		printf("Case #%d: %d\n",i+1,n);
	}
	return 0;
}

