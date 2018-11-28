#include <iostream>
#include <algorithm>
#include <cassert>
#include <cfloat>
#include <climits>
#include <cstring>
#include <functional>
#include <list>
#include <map>
#include <numeric>
#include <stack>
#include <string>
#include <vector>
#include <queue>
#include <fstream>

using namespace std;

const string fileName = "InfiniteHouseOfPancakes";

int cakeCount;
int cache[1001][1001];

int minMinute(vector<int>& cakes){
	vector<int>::iterator maxIter = max_element(cakes.begin(), cakes.end());
	int result = *maxIter;
	if (result == 1) return 1;

	if (result % 9 == 0 && result / 9 % 2 == 1){
		int index = maxIter - cakes.begin();

		vector<int> subCakes1 = cakes;
		vector<int> subCakes2 = cakes;

		int result=subCakes1[index];

		int minValue = result;

		subCakes1[index]=result / 3 * 2;
		subCakes1.push_back(result - subCakes1[index]);

		minValue = min(minValue, minMinute(subCakes1)+1);

		subCakes2[index]= result / 2;
		subCakes2.push_back(result - subCakes2[index]);

		minValue = min(minValue, minMinute(subCakes2)+1);
		return minValue;
	}
	else{
		*maxIter = result / 2;
	}
	
	cakes.push_back(result - *maxIter);

	return min(result, minMinute(cakes)+1);
}

int main(){
	ofstream file(fileName + ".txt", ofstream::out);

	int testCase;
	cin >> testCase;
	for (int t = 0; t < testCase; t++){
		memset(cache, -1, sizeof(cache));

		cin >> cakeCount;
		vector<int> cakes(cakeCount);
		for (int i = 0; i < cakeCount; i++){
			cin >> cakes[i];
		}

		file << "Case #" << (t + 1) << ": " << minMinute(cakes) << endl;
	}

	file.close();
	return 0;
}