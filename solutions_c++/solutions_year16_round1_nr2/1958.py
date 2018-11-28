#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

void entry() {
	int N;
	cin >> N;
	vector< vector<long> > l(2 * N - 1, vector<long>(N));
	for (int n = 0; n < 2 * N - 1; ++n) {
		for (int i = 0; i < N; ++i) {
			cin >> l[n][i];
		}
	}
	int s = 0;
	vector<long> result(N, 0);
	int i;
	for (i = 0; i < N; ++i) {
		long sum = 0;
		long min_val = 2501;
		for (int n = s; n < 2 * N - 1; ++n) {
			sum += l[n][i];
			if (l[n][i] < min_val) {
				min_val = l[n][i];
			}
		}
		// find least 2 list with min_val
		long list_sum = 0;
		int num_found = 0;
		for (int n = s; n < 2 * N - 1; ++n) {
			if (l[n][i] == min_val) {
				++num_found;
				for (int ii = i; ii < N; ++ii) {
					list_sum += l[n][ii];
				}
				iter_swap(l.begin() + s, l.begin() + n);
				++s;
			}
		}
		if (num_found == 2) {
			result[i] = list_sum - sum;
		}
		else {
			result[i] = min_val;
			break;
		}
	}
	int t = i;
	s = 2 * N - 2;
	for (i = N - 1; i > t; --i) {
		long sum = 0;
		long max_val = 0;
		for (int n = s; n >= 0; --n) {
			sum += l[n][i];
			if (l[n][i] > max_val) {
				max_val = l[n][i];
			}
		}
		// find least 2 list with min_val
		long list_sum = 0;
		int num_found = 0;
		for (int n = s; n >= 0; --n) {
			if (l[n][i] == max_val) {
				++num_found;
				for (int ii = i; ii >= 0; --ii) {
					list_sum += l[n][ii];
				}
				iter_swap(l.begin() + s, l.begin() + n);
				--s;
			}
		}
		if (num_found == 2) {
			result[i] = list_sum - sum;
		}
		else {
			break;
		}
	}
	for (i = 0; i < N; ++i) {
		cout << " " << result[i];
	}
}

int main() {
	int T;
	cin >> T;
	for (int i = 0; i < T; ++i) {
		cout << "Case #" << (i + 1) << ":";
		entry();
		cout << "\n";
	}
	return 0;
}
