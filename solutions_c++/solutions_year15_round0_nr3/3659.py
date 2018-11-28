#include <cstring>
#include <cmath>
#include <cstdio>
#include <iostream>

using namespace std;


int main() {

	char A[4][4] = {{1, 2, 3, 4}, {2, -1, 4, -3}, {3, -4, -1, 2} ,{4, 3, -2, -1}};
	int t;
	scanf("%d", &t);

	int count = 1; 
	while( count  <= t){

		int answer = 0;
		int l, x;
		scanf("%d%d", &l, &x);
		int len = l*x;
		char T[10001], S[10001];
		cin >> T;
		strcpy(S, T);
		for(int i = 1; i<x; i++)
			strcat(S, T);
		int previous = 1;
		int I = 0, J = 0, K = 0;
		for(int i = 0; i<len; i++) {
			if(I == 0) {
				int val = A[(int)abs(previous)-1][S[i] - 'i' + 1];
				if(previous < 0) val = -val;
				previous = val;
				if(val == 2) {
					I = 1;
					previous = 1;
				}
			}
			else if( J == 0) {
				int val = A[(int)abs(previous)-1][S[i] - 'i' + 1];
				if(previous < 0) val = -val;
				previous = val;
				if(val == 3) {
					J = 1;
					previous = 1;
				}
			}
			else if( K == 0) {
				int val = A[(int)abs(previous)-1][S[i] - 'i' + 1];
				if(previous < 0) val = -val;
				previous = val;
				if(val == 4) {
					K = 1;
					previous = 1;
					if( i == len-1){
						answer = 1;
					}
				}
			}
			else {
				previous = 1;
				int val = 1;
				for(; i<len; i++) {
					val = A[(int)abs(previous)-1][S[i] - 'i' + 1];
					if(previous < 0) val = -val;
					previous = val;
				}
				if(val == 1)
					answer = 1;
			}
		}
		if(answer == 1)
			printf("Case #%d: YES\n", count);
		else
			printf("Case #%d: NO\n", count);
		count++;
	}
}
