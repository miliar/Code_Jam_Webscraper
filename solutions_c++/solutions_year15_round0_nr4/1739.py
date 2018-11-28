#include <iostream>
#include <stdio.h>
using namespace std;

int  X,R,C;
bool deal()
{
	if(R*C%X!=0) return 0;
	if(X==1 || X==2) return 1;
	else if(X==3)
	{
		if(R*C==3) return 0;
		return 1;
	}
	else
	{
		if(R*C<=8) return 0;
		return 1;
	}
	
}

int main() {
	// your code goes here
	int T, cases;
	scanf("%d",&T);
	for(cases=0;cases<T;++cases)
	{
		printf("Case #%d: ", cases+1);
		scanf("%d%d%d",&X,&R,&C);
	//	printf("X=%d R=%d C=%d: ", X, R, C);
		if(deal()) printf("GABRIEL\n");
		else printf("RICHARD\n");
	}
	return 0;
}