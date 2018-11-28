#include <stdio.h>
#include <string.h>
#include <string>
#include <stdlib.h>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <iostream>
#include <math.h>
#include <sstream>
using namespace std;

int main() {	
	int T = 0;
	scanf("%d\n",&T);	
	vector<int> data;

	for (int i=0; i<T; i++) {
		int N = 0;
		int jawab = 0;
		int jum = 0;

		scanf("%d\n", &N);
		data.clear();
				
		for (int j=0; j<4*(N-1); j++) {
			int tempD = 0;
			scanf("%d", &tempD);
		}
		for (int j=0; j<4; j++) {
			int tempD = 0;
			scanf("%d", &tempD);
			data.push_back(tempD);
		}
		for (int j=0; j<4*(4-N); j++) {
			int tempD = 0;
			scanf("%d", &tempD);
		}
		
		scanf("%d\n", &N);
		for (int j=0; j<4*(N-1); j++) {
			int tempD = 0;
			scanf("%d", &tempD);
		}
		for (int j=0; j<4; j++) {
			int tempD = 0;
			scanf("%d", &tempD);
			if (find(data.begin(), data.end(), tempD)!=data.end()) {
				jawab = tempD;
				jum++;
			}
		}
		for (int j=0; j<4*(4-N); j++) {
			int tempD = 0;
			scanf("%d", &tempD);
		}
		
		if (jum == 0) {
			printf("Case #%d: Volunteer cheated!\n",i+1);
		} else if (jum == 1) {
			printf("Case #%d: %d\n",i+1,jawab);
		} else {
			printf("Case #%d: Bad magician!\n",i+1);
		}
	}
	return 0;
}