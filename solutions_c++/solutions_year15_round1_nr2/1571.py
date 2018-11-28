#include <iostream>
#include <vector>
#include <map>
#include <limits.h>

using namespace std;

int main () {

	int T;
	cin >> T;

	vector<int> B(T);
	vector<long long> N(T);
	vector<vector<long long> > Mk(T);
	for (int i=0; i<T; ++i) {
		cin >> B[i];
		cin >> N[i];
		for (int j=0; j<B[i]; ++j) {
			long long k;
			cin >> k;
			Mk[i].push_back(k);
		}
	}

	for (int i=0; i<T; ++i) {
		int b = B[i];
		long long n = N[i];
		vector<long long>& mk = Mk[i];

/*		cout << b << endl;
		cout << n << endl;
		for (const int& j : mk) {
			cout << j << " ";
		} cout << endl;
*/
		double inv_sum = 0.0;
		for (const int& j : mk) {
			inv_sum += 1/(double)j;
		}
//		cout << "inv sum: " << inv_sum << endl;
		long long target_time = (long long) ((n-10) / inv_sum);
		if (target_time < 0)
			target_time = 0;
//		cout << "target_time : " << target_time << endl;

		vector<long long> current_time(b);
		long long processed = 0;
		for (int j=0; j<b; ++j) {
			long long my_processed = target_time/mk[j];
			processed += my_processed;
			current_time[j] = my_processed * mk[j];
		}
//		cout << processed << " (processed) " << endl;

		while (true) {
			long long smallest = LLONG_MAX;
			int smallest_index = -1;
			for (int j=0; j<b; ++j) {
				if (current_time[j] < smallest) {
					smallest = current_time[j];
					smallest_index = j;
				}
			}
			current_time[smallest_index] += mk[smallest_index];
			++processed;
			if (processed == n) {
				cout << "Case #" << (i+1) << ": " << smallest_index + 1 << endl;
				break;
			}
			if (processed > n) {
				cout << "wrong.." << endl;
				break;
			}
		}
	}


	return 0;
}