#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
	
	int size;

	cin >> size;

	for (int i = 0; i < size; i++) {
		int ins;
		cin >> ins;
		vector<double> vec = vector<double>();
		vector<double> vec2 = vector<double>();

		for (int j = 0; j < ins; j++) {
			double x;
			cin >> x;
			vec.push_back(x);
		}

		for (int j = 0; j < ins; j++) {
			double x;
			cin >> x;
			vec2.push_back(x);
		}

		sort(vec.begin(), vec.end());
		sort(vec2.begin(), vec2.end());

		vector<double> vec3 = vec;
		vector<double> vec4 = vec2;

		int dec = 0;
		int itr = ins;
		int trickWin = 0;
		for (int ii = itr-1; ii >= 0; ii--) {
			double value = vec2[ii];
			bool found = false;
			for (int k = 0; k < vec.size(); k++) {
				if (vec[k] > value) {
					found = true;
					vec.erase(vec.begin()+k);
					break;
				}
			}
			if (found) {
				trickWin++;
			} else {
				vec.erase(vec.begin());
			}
		}
		int wins = ins;
		for (int p = 0; p < ins; p++) {
			for (int k = 0; k < vec4.size(); k++) {
				if (vec4[k] > vec3[p]) {
					wins--;
					vec4.erase(vec4.begin()+k);
					break;
				}
			}
		}
		cout << "Case #" << i+1 << ": " << trickWin << " " << wins << endl;
	}
	return 0;
}