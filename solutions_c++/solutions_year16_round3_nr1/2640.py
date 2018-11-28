#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <math.h>
#include <algorithm>
#include <unordered_map>
#include <unordered_set>
#include <queue>
using namespace std;
struct help {
public:
	help(int a, int b) : party(a), number(b){};
	int party;
	int number;
	bool operator <(help b) {
		if (number == b.number)
			return party > b.party;
		else return number < b.number;
	};
};
void solutionA(vector<int> input, int num) {
	cout << "Case #" << num << ":";
	int n = input.size();
	vector<help> myset;
	int sum = 0;
	for (int i = 0; i < n; i++) {
		help tmp(i, input[i]);
		myset.push_back(tmp);
		sum += input[i];
	}
	while (sum > 3) {
		sort(myset.begin(), myset.end());
		if (myset[n - 1].number > myset[n - 2].number) {
			cout << " " << (char)('A' + myset[n - 1].party);
			myset[n - 1].number--;
			sum--;
		}
		else {
			cout << " " << (char)('A' + myset[n - 1].party) << (char)('A' + myset[n - 2].party);
			myset[n - 1].number--;
			myset[n - 2].number--;
			sum -= 2;
		}
	}
	if (sum == 3) {
		sort(myset.begin(), myset.end());
		cout << " " << (char)('A' + myset[n - 1].party);
		myset[n - 1].number--;
		sum--;
	}
	if (sum == 2) {
		sort(myset.begin(), myset.end());
		cout << " " << (char)('A' + myset[n - 1].party) << (char)('A' + myset[n - 2].party);
	}
}
int main() {
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t, n;
	cin >> t;
	for (int i = 0; i < t; i++) {
		cin >> n;
		vector<int> input(n);
		for (int j = 0; j < n; j++) {
			cin >> input[j];
		}
		solutionA(input, i + 1);
		cout << endl;
	}		
	return 1;
}
