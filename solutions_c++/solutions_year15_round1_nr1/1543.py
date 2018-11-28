#include <iostream>
#include <vector>
#include <map>

using namespace std;

int main () {

	int n;
	cin >> n;

	vector<int> num_mushrooms(n);
	vector<vector<int> > mushrooms(n);
	for (int i=0; i<n; ++i) {
		cin >> num_mushrooms[i];
		for (int j=0; j<num_mushrooms[i]; ++j) {
			int k;
			cin >> k;
			mushrooms[i].push_back(k);
		}
	}

	for (int i=0; i<n; ++i) {
		int ans1 = 0;
		int ans2 = 0;
		int num_mushroom = num_mushrooms[i];
		vector<int>& mushroom = mushrooms[i];

		int biggest_decrease = 0;
		for (int j=0; j<num_mushroom-1; ++j) {
			int decrease = mushroom[j] - mushroom[j+1];
			if (decrease > biggest_decrease)
				biggest_decrease = decrease;
			if (mushroom[j] > mushroom[j+1]) {
				ans1 += mushroom[j] - mushroom[j+1];
			}
		}
		for (int j=0; j<num_mushroom-1; ++j) {
			if (mushroom[j] < biggest_decrease)
				ans2 += mushroom[j];
			else
				ans2 += biggest_decrease;
		}




		cout << "Case #" << (i+1) << ": " << ans1 << " " << ans2 << endl;
	}


	return 0;
}