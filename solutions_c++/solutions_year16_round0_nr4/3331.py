#include <iostream>
#include <stdio.h>
using namespace std;

int main(int argc, char const *argv[])
{
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		int k, c, s;
		cin >> k >> c >> s;
		cout << "Case #" << i+1 << ": ";

		long *arr = new long[k];
		// initialize to {0, 1, 2...}
		for (int j = 0; j < k; j++) {
			arr[j] = j;
		}
		// for each level of complexity
		// complexity 1 = no expansion
		for (int x = 1; x < c; x++) {
			for (int j = 0; j < k; j++) {
				arr[j] = (arr[j] * k) + j;
			}
		}

		for (int j = 0; j < k; j++) {
			cout << arr[j] + 1 << " ";
		}

		cout << "\n";
		delete[] arr;
	}
	return 0;
}