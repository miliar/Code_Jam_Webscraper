#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>
using namespace std;


int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int t;
	cin >> t;
	for(int caseNum = 1; caseNum <= t; caseNum++) {
		int n;
		cin >> n;
		bool isOdd[2501] = {};
		for(int i = 0; i < 2*n-1; i++) {
			for(int j = 0; j < n; j++) {
				int num;
				cin >> num;
				isOdd[num] = !isOdd[num];
			}
		}
		vector<int> missingRank;
		for(int i = 1; i <= 2500; i++) {
			if(isOdd[i])
				missingRank.push_back(i);
		}
		cout << "Case #" << caseNum << ":";
		for(int i = 0; i < missingRank.size(); i++) {
			cout << " " << missingRank[i];
		}
		cout << endl;
	}
	return 0;
}