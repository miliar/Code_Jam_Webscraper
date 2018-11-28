#include <cstdio>
#include <cassert>
#include <vector>
#include <algorithm>
using namespace std;
const int MAX_DINERS = 1005;

int testCases, numDiners, minMinutes, numPancakes;

int calc_min(int a, int b) {
	return (a < b) ? a : b;
}

int calc(vector<int> a, int intp, int maxValue) {
	if(intp >= maxValue) return maxValue;
	sort(a.begin(), a.end());
	if(a[a.size() - 1] == 1) {
		return intp + 1;
	}

	int last = a[a.size() - 1];
	//for(int i = 0; i < a.size(); i++) printf("%d ", a[i]);
	//printf("| %d\n", intp);
	a.erase(a.begin() + (a.size() - 1));
	int minValue = last + intp;
	//if(last == 2) return calc_min(minValue, 2);
	for(int mid = (last%2?last/2+1:last/2); mid < last; mid++) {
		a.push_back(mid);
		a.push_back(last - mid);
		//printf("Adding %d-%d\n", mid, last-mid);
		minValue = calc_min(minValue, calc(a, intp+1, maxValue));
		a.erase(a.begin() + (a.size() - 1));
		a.erase(a.begin() + (a.size() - 1));
	}
	return minValue;
}

int main() {
	scanf("%d", &testCases);
	for(int t = 1; t <= testCases; t++) {
		scanf("%d", &numDiners);
		vector<int> a;
		int max_val = 0;
		for(int i = 0; i < numDiners; i++) {
			scanf("%d", &numPancakes);			
			a.push_back(numPancakes);
			if(numPancakes > max_val) max_val = numPancakes;
		}
		minMinutes = calc(a, 0, max_val);
		printf("Case #%d: %d\n", t, minMinutes);
	}
	return 0;
}