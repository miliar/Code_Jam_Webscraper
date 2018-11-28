#include <iostream>
#include <fstream>
#include <vector>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#define M 16384

using namespace std;

char s[M][16];
int b[11];

int diviz(unsigned long long x) {
	int n = (int) sqrt(x);

	for (int i = 2; i <=n; i++)
		if (x%i == 0)
			return i;

	return 0;
}

int main() {
	
	int t, tst, k, ma = 0, j, x, n, i, d;
	unsigned long long rez, y, p;
	
	//generate potential coins
	for (i = 0; i < M; i++) {
		x = i;
		s[i][0] = '1';
		s[i][15] = '1';
		for (j = 0; j < 14; j++) {
			s[i][j+1] = (x & 1) + '0';
			x = x>>1;		
		}
		//printf("%s\n", s[i]);
			
	}
	

	printf("Case #1:\n");
	n = 0;
	for (i = 0; i < M; i++) {
		memset(b, 0, sizeof(b));
		
		for (j = 2; j < 11; j++) {
			y = 0;
			p = 1;
			for (k = 0; k < 16; k++){
				y += (s[i][k] - '0')*p;
				p *= j;
			}
			d = diviz(y);
			//printf("baza %d nr %llu div %d\n", j, y, d);
			if (!d)
				break;
			b[j] = d;
			
		}
		if (j == 11) {
			n++;
			printf("%llu ", y );
			for (j = 2; j < 11; j++) 
				printf("%d ", b[j]);
			printf("\n");				
			
			if (n==50)
				break;
		}
			
	}
	
	return 0;
}
