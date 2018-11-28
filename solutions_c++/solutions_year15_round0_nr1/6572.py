#include <stdio.h>
#include <stdlib.h>

using namespace std;

int main(){

	int T;
	
	scanf("%d", &T);
	
	for(int t=0; t<T; t++){
		int sMax;
		scanf("%d ", &sMax);
		
		char buffer[sMax+2];
		scanf("%s", buffer);
		
		int count = buffer[0] - '0';
		int diff=0, total=0;
		
		for(int i=1; i<=sMax; i++){
			if(buffer[i] - '0' > 0 && i > count){
				diff = i-count;
				count += diff;
				total += diff;
			}
			
			count += buffer[i] - '0';
		} 
		printf("Case #%d: %d\n", t+1, total);
	} 
	
	return 0;
}
