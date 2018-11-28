/*
 */
#include <cassert>
#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;

int K,C,S;

int main() {
	int i,j,k,ts,cs = 0;
	for ( scanf("%d",&ts); ts--; ) {
		printf("Case #%d:",++cs);
		scanf("%d %d %d",&K,&C,&S);
		for ( i = 1; i <= S; printf(" %d",i++) );
		putchar('\n');
	}
	return 0;
};

