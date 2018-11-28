#include <iostream>
#include <string>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <functional>
#include <queue>
using namespace std;

long long solve1(vector<long long> arr){
	int ret = 0;
	for (int i = 1; i < arr.size(); ++i) {
		if (arr[i] < arr[i - 1])
			ret += (arr[i - 1] - arr[i]);
	}
	return ret;
}

long long solve2(vector<long long> arr){
	long long rate10sec = -1;
	long long ret = 0;
	for (int i = 1; i < arr.size(); ++i) {
		int interval = arr[i - 1] - arr[i];
		if (rate10sec < interval)
			rate10sec = interval;
	}

	for (int i = 1; i < arr.size(); ++i) {
		if (arr[i - 1] < rate10sec)
			ret += arr[i - 1];
		else
			ret += rate10sec;
	}
	return ret;
}
void main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	//freopen("A-small-attempt0.in", "r", stdin);
	//freopen("A-small-attempt0.out", "w", stdout);
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	int nCase;
	cin >> nCase;
	for (int cc = 0; cc < nCase; ++cc) {
		vector<long long> arr;
		int N;
		cin >> N;
		arr.resize(N);
		for (int i = 0; i < arr.size(); ++i) {
			cin >> arr[i];
		}
		long long y, z;
		y = solve1(arr);
		z = solve2(arr);
		cout << "Case #" << cc + 1 << ": " << y << " " << z << endl;
	}
}