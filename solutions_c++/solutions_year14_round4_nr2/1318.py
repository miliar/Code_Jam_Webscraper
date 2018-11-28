#include <iostream>
#include <sstream>
#include <numeric>
#include <set>
#include <algorithm>
#include <map>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <math.h>
#include <stdlib.h>
#include <limits.h>

using namespace std;

bool isValid(vector<int> &data){
	bool decr = false;
	for (int i = 0; i < data.size() - 1; i++){
		if ((data[i+1] > data[i]) && (decr)){
			return false;
		}
		if (data[i+1] < data[i]){
			decr = true;	
		}
	}
	return true;
}

int main(){
	int tests;
	cin >> tests;
	for (int t = 0; t < tests; t++){
		int N;
		cin >> N;
		vector<int> data(N), dataCopy, data2;
		for (int i = 0; i < N; i++){
			cin >> data[i];
		}
		dataCopy = data;
		int minChanges = INT_MAX;
		sort(data.begin(), data.end());
		do {
			if (isValid(data)){
				data2 = dataCopy;
				map<unsigned long, int> position;
				for (int i = 0; i < data2.size(); i++){
					position[data[i]] = i;
				}
				int changes = 0;
				bool fine = false;
				while(!fine){
					fine = true;
					for (int i = 0; i < data2.size() - 1; i++){
						if (position[data2[i]] > position[data2[i+1]]){
							fine = false;
							swap(data2[i], data2[i+1]);
							changes++;
						}
					}
				}
				minChanges = min(changes, minChanges);
			}
		} while(next_permutation(data.begin(), data.end()));
		int solution = 0;
		cout << "Case #" << (t+1) << ": " << minChanges << endl;
	}
}
