#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <cstdlib>
using namespace std;
#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define MAX 128
int INF = 9876543210;
int digit[10];
int num[100];

int solve() {
	int N, temp;
	cin >> N;
	for(int i = 0; i < 100; i++) {
		temp = N * (i+1);
		while (temp != 0) {
			digit[temp % 10] = 1;
			temp = temp / 10;
		}
		//for(int j = 0; j < 10; j++)
		//	printf("%d ", digit[j]);
		//printf("\n");
		for(int j = 0; j < 10; j++) {
			if (digit[j] == -1)
				break;
			else if(j == 9)
				return N * (i+1);
		}
	}
	return INF;

	// printf("%s\n", num);
}

int main()
{
	int t;
	cin >> t;

	for(int i = 0; i < t; i++) {
	    memset(digit, -1, sizeof(digit));
		int dap = solve();
		if (dap == INF)
			printf("Case #%d: INSOMNIA\n", i+1);
		else
			printf("Case #%d: %d\n", i+1, dap);
	}

	return 0;
}
