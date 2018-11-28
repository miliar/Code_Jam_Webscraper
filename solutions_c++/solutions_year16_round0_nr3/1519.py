#include <string>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <vector>

using namespace std;
int n, j;

void print_number(int x) {
	long long nums[11];
	long long pow[11];
	vector<int> v;

	fill(nums, nums + 11, 0);
	fill(pow, pow + 11, 1);

	while (x != 0) {
		v.push_back(x % 2);
		x = x / 2;
	}
	reverse(v.begin(), v.end());

	for (int i = 0; i < v.size(); i++) {
		cout << v[i];
	}
	for (int i = 0; i < n - v.size() * 2; i++) {
		cout << "0";
	}
	for (int i = 0; i < v.size(); i++) {
		cout << v[i];
	}
	cout << " ";
	

	for (int i = v.size()-1; i >= 0; i--) {
		for (int k = 2; k <= 10; k++) {
			nums[k] += v[i] * pow[k];
			pow[k] *= k;
		}
	}

	for (int i = 2; i <= 10; i++) {
		cout << nums[i] << " ";
	}

	cout << "\n";
}

int main() {
	int tests;

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	cin >> tests;

	cin >> n >> j;


	cout << "Case #1:\n";
	for (int i = 3; i <= 2 * j + 1; i+=2) {
		print_number(i);
	}

	return 0;
}