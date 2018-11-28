#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int total(vector<double> Naomi, vector<double> Ken, int N) {
		int deceit=0, nodec=0, j=0, k=N-1, l=N-1;
		while (j<=k) {
			if (Naomi[k] > Ken[l]) {
				deceit++;
				k--;
				l--;
			} else {
				l--;
				j++;
			}
		}
		return deceit;
}

int main() {
	int T;
	cin >> T;
	for (int i=0; i<T; ++i) {
		int N;
		cin >> N;
		vector<double> Naomi(N), Ken(N);
		copy_n(istream_iterator<double>(cin), N, Naomi.begin() );
		copy_n(istream_iterator<double>(cin), N, Ken.begin() );
		sort(Naomi.begin(), Naomi.end());
		sort(Ken.begin(), Ken.end());
		cout << "Case #" << i+1 << ": " << total(Naomi, Ken, N) << " " << N-total(Ken, Naomi, N) << endl;
	}
	return 0;
} 
