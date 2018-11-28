#include <stdio.h>
#include <math.h>
#include <vector>

using namespace std;


void run() {
	int K, C, S;
	scanf("%d %d %d", &K, &C, &S);
	
	for (int i=1; i<=S; i++) {
		printf("%d ", i);
	}
	printf("\n");
}

int main() {
	int testCase;
	scanf("%d", &testCase);
	
	for (int t=1; t<=testCase; t++) {
		printf("Case #%d: ", t);
		run();
	}
}
