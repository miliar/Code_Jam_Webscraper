#include <stdlib.h>
#include <stdio.h>

int main(){

	int T;
	int N;
	int* m;
	int r1 = 0, r2 = 0;

	scanf("%d", &T);

	for(int x = 0; x < T; ++x){
		r1 = 0;
		r2 = 0;
		scanf("%d", &N);

		m = new int[N];
		for(int y = 0; y < N; ++y){
			scanf("%d", &(m[y]));
		}

		int max_dif = 0;
		int dif;
		//first method
		for(int y = 0; y < N - 1; ++y){
			dif = m[y] - m[y + 1];
			if(dif > max_dif){
				max_dif = dif;
			}
			r1 +=  dif > 0 ? dif : 0;
		}

		//second method
		for(int y = 0; y < N - 1; ++y){
			dif = m[y] - m[y + 1];
			
			r2 += (m[y] <= max_dif) ? m[y] : max_dif; 
		}


		printf("Case #%d: %d %d\n", x + 1, r1, r2);
	}


	return 0;
}
