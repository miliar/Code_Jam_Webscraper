#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int War(vector<double> Naomi, vector<double> Ken) {
	int size = Naomi.size();
	int score = 0;
	for (int i = 0; i < size; i++) {
		int smallest = -1, target = -1;
		for (int j = 0; j < size; j++) {
			if ((smallest < 0) && (Ken[j] > 0))
				smallest = j;
			if (Ken[j] > Naomi[i]) {
				target = j;
				break;
			}
		}
		Naomi[i] = 0;
		if (target < 0) {
			Ken[smallest] = 0;
			score++;
		} else {
			Ken[target] = 0;
		}
	}	
	return score;
}

int DWar(vector<double> Naomi, vector<double> Ken) {
	int size = Naomi.size();
	int score = 0;
	for (int i = 0; i < size; i++) {
		int smallest = -1, biggest = -1;
		for (int j = 0; j < size; j++) {
			if ((smallest < 0) && (Ken[j] > 0))
				smallest = j;
			if ((biggest < j) && (Ken[j] > 0))
				biggest = j;
		}
		//printf("%d %d\n", smallest, biggest);
		if (Naomi[i] < Ken[smallest]) {
			Ken[biggest] = 0;
		} else {
			Ken[smallest] = 0;
			score++;
		}
		Naomi[i] = 0;
	}
	return score;
}


int main() {
	freopen("D.in", "r", stdin);
	freopen("D.out", "w", stdout);
	int Total = 0, size = 0;
	scanf("%d", &Total);
	for (int i = 0; i < Total; i++) {
		vector<double> Naomi, Ken;
		scanf("%d", &size);
		printf("Case #%d: ", i + 1);
		for (int j = 0; j < size; j++) {
			double temp;
			scanf("%lf", &temp);
			Naomi.push_back(temp);
		}
		for (int j = 0; j < size; j++) {
			double temp;
			scanf("%lf", &temp);
			Ken.push_back(temp);
		}
		sort(Naomi.begin(), Naomi.end());
		sort(Ken.begin(), Ken.end());
		printf("%d %d\n", DWar(Naomi, Ken), War(Naomi, Ken));
	}
	return 0;
}
