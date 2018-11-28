#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <vector>

using namespace std;

int main() {
	int cases,i,j,k,p,n;
	scanf("%i\n", &cases);
	char LINE[1010];
	for (i = 0; i < cases; i++){
		scanf("%i %s\n", &n, &LINE);
		int EXTRAS = 0;
		int LAST = 0;
		for (j =1; j <=n; j++){
			LAST += LINE[j - 1] - '0';
			while (j > LAST + EXTRAS){
				EXTRAS++;
			}
		}
		printf("Case #%i: %i\n", i + 1, EXTRAS);
	}
	return 0;
}