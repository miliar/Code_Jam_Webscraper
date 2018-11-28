#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<math.h>
using namespace std;
#define INF 10000000

int main() {
	int testCases;
	vector<int> cakeCountForDiner;
	int totalDiners;
	int temp;
	cin>>testCases;
	for(int t = 1; t <= testCases; ++t){
		cin>>totalDiners;
		cakeCountForDiner.clear();
		for(int i = 0; i < totalDiners; ++i){
			cin>>temp;
			cakeCountForDiner.push_back(temp);
		}
		int maxValue = cakeCountForDiner[0];
		for(int i = 1; i < totalDiners; ++i){
			if(cakeCountForDiner[i] > maxValue) maxValue = cakeCountForDiner[i];
		}
		int minAns = INF;
		for(int i = 1; i <= maxValue; ++i){
			int tempAns = i;
			for(int j = 0; j < totalDiners; ++j){
				if(cakeCountForDiner[j] <= i) continue;
				int leftOver = (cakeCountForDiner[j] - i);
				int portions = leftOver / i;
				if(leftOver % i) portions++;
				tempAns += portions;
			}
			if(tempAns < minAns) minAns = tempAns;
		}
		cout<<"Case #"<<t<<": "<<minAns<<endl;
	}
	return 0;
}