#include <stdio.h>
//#include <vector>

//using namespace std;

int main() {
	
	int t, i, smax, j, s, claping, invited;
	char c;

//	vector<int> shyvec;

	scanf("%d", &t);
	for (i = 0; i<t; ++i) {
		claping = 0;
		invited = 0;
		scanf("%d ", &smax);
//		printf("smax: %d, ", smax);	
		
		for (j = 0; j<=smax; ++j) {
			scanf("%c", &c);
			s = c-48;
			
			if (j <= claping) {
				claping += s;
			} 
					
//			printf("%d: clap %d, invit: %d\n", j, claping, invited);	
			if (claping < smax && claping < j+1) {
				invited += ((j+1)-claping);
				claping += ((j+1)-claping);
			}
			
					
//			printf("%d: clap %d, invit: %d\n\n", j, claping, invited);	
			
//			printf("%d ", c-48);	
		}
		
		if (claping < smax) {
//			invited += ((j+1)-claping);
//			claping += ((j+1)-claping);
		}
		
		printf("Case #%d: %d\n", i+1, invited);	
		
	}
	
		
    return 0;
}
