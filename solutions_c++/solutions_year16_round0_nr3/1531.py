#include <bits/stdc++.h>
using namespace std;

int A[50];

void createall(int len, int num) {
	int con = len/2-2;
	for(int i=0; i<num; i++) {
		memset(A, 0, sizeof A);
		int curr = 0;
		A[curr++] = 1; 
		A[curr++] = 1;
		for(int j=0; j<con; j++) {
			if(i & (1ll<<j)) {
				A[curr++] = 1;
				A[curr++] = 1;
			}
			else {
				A[curr++] = 0;
				A[curr++] = 0;
			}
		}
		A[curr++] = 1;
		A[curr++] = 1;
		for(int i=0; i<len; i++)
			printf("%d", A[i]);
		printf(" 3 4 5 6 7 8 9 10 11\n");
	}
}

int main() {
	int t;
	scanf("%d", &t);
	for(int tc = 1; tc<=t; tc++) {
		int len, num;
		scanf("%d %d", &len, &num);
		printf("Case #%d:\n", tc);
		createall(len, num);
	}
}	