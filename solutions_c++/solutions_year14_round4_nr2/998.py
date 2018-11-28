#include<iostream>
#include<algorithm>
#include<map>

using namespace std;

int main() {
	int kases;
	cin >> kases;
	for (int kase = 1; kase <= kases; kase++) {
		cout << "Case #" << kase << ": ";
		//cerr << kase << ":" << endl;

		int N;
		cin >> N;
		vector<int> as(N);
		int largest = 0;
		for (int i = 0; i < N; i++){
			cin >> as[i];
			largest = max(largest, as[i]);
		}

		int last = -1;
		int left = 0;
		int right = N-1;
		int cost = 0;

		while (last < largest) {
			int pos = -1;
			int smallest = largest + 1;
			for (int i = 0; i < N; i++) {
				if  (as[i] > last && as[i] < smallest) {
					smallest = as[i];
					pos = i;
				}
			}
			last = smallest;

			// shift it left or right, depending on which is closer
			if (pos - left < right - pos) {
				for (int i = pos; i > left; i--) {
					int t = as[i];
					as[i] = as[i-1];
					as[i-1] = t;
					cost++;
					//cerr << "swap left " << i << endl;
				}
				left++;
			} else {
				for (int i = pos; i < right; i++) {
					int t = as[i];
					as[i] = as[i+1];
					as[i+1] = t;
					cost++;
					//cerr << "swap right " << i << endl;
				}
				right--;
			}
		}

		//for (int i = 0; i < N; i++) cerr << as[i] << " ";
		//cerr << endl;

		cout << cost << endl;
	}
	return 0;
}
