#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
	int T, N, totalA, totalB, maxDiff;
	vector<int> arr;
	cin >> T;
	for (int i = 0; i < T; i++){
		cin >> N;
		totalA = 0;
		totalB = 0;
		maxDiff = 0;
		for (int j = 0; j < N; j++){
			int temp = 0;
			cin >> temp;
			arr.push_back(temp);
		}
		for (int j = 0; j < N-1; j++){
			int diff = arr[j]-arr[j+1];
			if (diff>maxDiff) maxDiff = diff;
			if (arr[j]>arr[j+1]){
				totalA += diff;
			}
		}
		for (int j = 0; j< N-1; j++){
			if (arr[j]<=maxDiff) totalB+=arr[j];
			else totalB+=maxDiff;
		}
		cout << "Case #" << i+1 << ": " << totalA << " " << totalB << endl;
		arr.clear();
	}
  return 0;
}
