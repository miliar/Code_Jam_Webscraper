#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cmath>
using namespace std;

bool comp(float x, float y) {
	return ( (x - y) < 0.0000001 );
}

int main() {
	int T, N;
	int j, s1, e1, s2, e2, k;
	
	scanf("%d", &T);
	
	for(int i=0; i<T; i++) {
		scanf("%d", &N);
		float *naomi = new float[N];
		float *ken = new float[N];
		int c1 = 0, c2 = 0;
		
		for(j=0; j<N; j++) {
			scanf("%f", &naomi[j]);	
		}
		for(j=0; j<N; j++) {
			scanf("%f", &ken[j]);	
		}
		sort(naomi, naomi+N, comp);
		sort(ken, ken+N, comp);
		
		s1=0; s2=0; e1=N-1; e2=N-1;
		
		/*for(j=0; j<N; j++) {
			printf("%f ", naomi[j]);
		}
		printf("\n");
		for(j=0; j<N; j++) {
			printf("%f ", ken[j]);
		}
		printf("\n");
		*/
		while(s1 <= e1) {
			if( ((ken[s2] - naomi[s1]) > 0.000001) ) {
				s1 = s1+1;
				e2 = e2-1;
			}
			else if( (naomi[s1] - ken[s2]) > 0.000001 ) {
				s1 = s1+1;
				s2 = s2+1;
				c1+=1;
			}
		}
		
		for(j=0; j<N; j++) {
			for(k=0; k<N; k++) {
				if ( ((ken[k] - naomi[j]) > 0.000001) ) {
					ken[k] = 0.0;
					naomi[j] = 0.0;
					break;
				}
			}
		}
		
		for(j=0; j<N; j++) {
			if( fabs(naomi[j] - 0.0) > 0.000001 ) {
				c2+=1;
			}
		}
		
		printf("Case #%d: %d %d\n", i+1, c1, c2);
		delete[] naomi;
		delete[] ken;
	}
	return 0;
}