#include <stdio.h>
#include<stdlib.h>
FILE *in, *out;
#pragma warning(disable:4996)
#include <vector>
#include <algorithm>
using namespace std;



int main(){
	out = fopen("1.out", "w");
	int T,N;
	int y, z;
	int m[10007];
	scanf("%d", &T);
	for (int i = 0; i < T; i++){
		scanf("%d", &N);
		y = 0; z = 0; int maxrate = 0;
		for (int j = 0; j < N; j++){
			scanf("%d", &m[j]);
		}
		for (int j = 1; j < N; j++){
			int x;
			x = m[j-1] - m[j];
			if (x > 0){
				y += x;
				if (x > maxrate){
					maxrate = x;
				}
			}
		}
		// second

		for (int j = 0; j < N - 1; j++){
			int mx;
			maxrate > m[j] ? mx = m[j] : mx = maxrate;
			z += mx;
		}

		printf("Case #%d: %d %d\n", i + 1, y, z);
		fprintf(out,"Case #%d: %d %d\n", i + 1, y, z);

	}

}


