#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <vector>
#include <string>
#include <map>

using namespace std;

int main(){
	freopen("output.txt","w",stdout);
	//freopen("B-large.in","r",stdin);
	printf("Case #1:\n");
	int start = 10000000;
	int startbase2 = 129;
	int base, ans, tens;
	for (int i=0; i<50; i++) {
		start = 10000000;
		tens = 1;
		for (int digit=0; digit<7; digit++) {
			if (startbase2 & (1 << digit)){
				start += tens;
			}
			tens *= 10;
		}
		printf("%d%d", start, start);
		for (base = 2; base<=10; base++) {
			ans = base*base*base*base*base*base*base*base+1;
			printf(" %d", ans);
		}
		printf("\n");
		startbase2 += 2;
		
	}
	return 0;
}