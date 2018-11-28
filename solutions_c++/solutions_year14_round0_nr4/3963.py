

#include <stdio.h>
#include <vector>
#include <algorithm>

int getRes1(int N, std::vector<double> naomi, std::vector<double> ken);
int getRes2(int N, std::vector<double> naomi, std::vector<double> ken);

int main() {
	int T;
	
	scanf("%d", &T);
	
	for (int t = 1; t <= T; t++) {
	
		int N;
		scanf("%d", &N);
		
		std::vector<double> naomi;
		std::vector<double> ken;
		
		for (int i = 0; i < N; i++) {
			double d;
			scanf("%lf", &d);
			naomi.push_back(d);
		}
		
		for (int i = 0; i < N; i++) {
			double d;
			scanf("%lf", &d);
			ken.push_back(d);
		}
		
		std::sort (naomi.begin(), naomi.end());
		std::sort (ken.begin(), ken.end());
		
		int res1 = getRes1(N, naomi, ken);
		int res2 = getRes2(N, naomi, ken);
		
		printf("Case #%d: %d %d\n", t, res2, res1);
	}

}

int getRes1(int N, std::vector<double> naomi, std::vector<double> ken) {
	int nwon = 0;
	int nidx = 0;
	for(int kidx = 0; kidx < N; kidx++) {
		if (naomi[nidx] > ken[kidx]) {
			nwon++;
		}
		else {
			nidx++;
		}
	}
	return nwon;
}

int getRes2(int N, std::vector<double> naomi, std::vector<double> ken) {
	int kwon = 0;
	int kidx = 0;
	for(int nidx = 0; nidx < N; nidx++) {
		if (naomi[nidx] > ken[kidx]) {
			kidx++;
		}
		else {
			kwon++;
			
		}
	}
	return N-kwon;
}

