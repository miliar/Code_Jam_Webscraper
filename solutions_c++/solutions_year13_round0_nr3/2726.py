#include<iostream>
#include<cstdio>
#include<math.h>

using namespace std;

int revers (int temp) {
	int revers = 0;
  	while( temp != 0 )
   	{
      		revers = revers * 10;
      		revers = revers + temp%10;
      		temp = temp/10;
   	}
   	return revers;
}

main () {
	int cases;
	int rangeI;
	int rangeO;
	int temp ,reverse, cantidad;
	double square;
	scanf("%d",&cases);
	for ( int z=1; z <= cases; z++) {
		scanf("%d %d",&rangeI,&rangeO);
		cantidad = 0;
		for ( int i=rangeI; i <= rangeO ; i++ ) {
   			if ( i == revers(i) ) {
   				square = sqrt(i);
   				if ( square == (int)square ) {
   					if ( square == revers(square) ) {
   						cantidad++;
   					}
   				}
   			}
		}
		printf("Case #%d: %d\n",z,cantidad);
	}
}
