#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <vector>
#include <set>
using namespace std;

int T;
int N;

int war(const vector<float>& p1, const vector<float>& p2){   

	int n = p2.size(), wins = 0;

	multiset<float> weights(p1.begin(), p1.end());
	for (int i = 0; i < n; i++){
		if (*weights.rbegin() < p2[i]){
			weights.erase(weights.begin());
		}
		else{
			weights.erase(weights.lower_bound(p2[i]));
			++wins;
		}
	}
	
	return wins;
}


int main(){
	freopen("D-large.in", "r", stdin);
	freopen("D-large.out", "w", stdout);

	float block;
	vector<float> naomi, ken;

	scanf("%d", &T);

	int nCase = 1;
	while (T-- > 0){

		scanf("%d", &N);

		for (int i = 0; i < N; i++){
			scanf("%f", &block);
			naomi.push_back(block);
		}

		for (int i = 0; i < N; i++){
			scanf("%f", &block);
			ken.push_back(block);
		}

		printf("Case #%d: %d %d\n",nCase, war(naomi, ken), N - war(ken, naomi));

		naomi.clear();
		ken.clear();
		
		nCase++;
	}


	return 0;
}