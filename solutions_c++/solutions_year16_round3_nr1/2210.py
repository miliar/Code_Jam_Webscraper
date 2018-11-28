/*
 * Qa.cpp
 *
 *  Created on: May 8, 2016
 *      Author: suparsh14
 */
#include<bits/stdc++.h>
using namespace std;
vector<int> large_indices(int *p, int n) {
	int max = -1;
	for (int j = 0; j < n; j++) {
		if (max < p[j])
			max = p[j];
	}
	vector<int> maxarr;
	for (int j = 0; j < n; j++) {
		if (p[j] == max)
			maxarr.push_back(j);
	}
	return maxarr;
}

int main() {

	int tc;
	scanf("%d",&tc);
	for (int i = 1; i <= tc; i++) {
		int n;
		scanf("%d", &n);
		int p[n], tot = 0;
		for (int j = 0; j < n; j++) {
			scanf("%d", &p[j]);
			tot += p[j];
		}
		printf("Case #%d: ", i);

		while (tot != 0) {
			vector<int> large = large_indices(p, n);
			if(large.size()==0)break;// never reaches here
			if(large.size()==1 || large.size()>2)
			{
				printf("%c ",'A'+large[0]);
				p[large[0]]--;
				tot--;
			}
			else{
				printf("%c%c ",'A'+large[0],'A'+large[1]);
				p[large[0]]--;
				p[large[1]]--;
				tot-=2;
			}

		}
		printf("\n");

	}

	return 0;
}

