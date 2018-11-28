#include <stdio.h>

int main() {
	int T, Smax;
	char S[1002];

	scanf("%d", &T);
	
	for(int t=0; t<T; t++) {

		scanf("%d", &Smax);
		scanf("%s", S);
		int F = 0;
		int Count = 0;
		for(int i=0; i<Smax+1; i++) {
			int temp = S[i]-'0';

			if(i > Count) {
				F+=(i-Count);
				Count+=(i-Count);
			}
			Count+=temp;			
		}
		
		printf("Case #%d: %d\n", t+1, F);
	}
	
	return 0;
}