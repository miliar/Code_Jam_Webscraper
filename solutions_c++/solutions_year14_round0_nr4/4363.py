#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
	int t = 0;
	cin >> t;
	vector <double> v1;
	vector <double> v2;
	for (int cur = 0; cur < t; cur++) {
		int num = 0;
		cin >> num;
		v1.resize(num);
		v2.resize(num);
		for (int i=0; i < num; i++) {
			cin >> v1[i];
		}
		for (int i=0; i < num; i++) {
			cin >> v2[i];
		}
		sort(v1.begin(), v1.end());
		sort(v2.begin(), v2.end());
		int dec = 0, war = 0;
		for (int i = 0, j = 0; i < num;) {
			if (v1[i] > v2[j]) {
				dec++;
				j++;
			}
			i++;
		}
		for (int i = 0, j = 0; j < num;) {
			if (v1[i] < v2[j]) {
				i++;
			} else {
				war++;
			}
			j++;
		}
		
		cout << "Case #" << cur + 1 << ": " << dec << ' ' << war << endl;
	}
	return 0;
}
