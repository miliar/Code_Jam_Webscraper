#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>

using namespace std;

int main() {
	int t;
	cin >> t;

	int x = 1;
	ofstream ofs("Senate Evacuation.txt");

	while (x <= t) {
		ofs << "Case #" << x << ": ";
		int n;
		cin >> n;

		int count = 0;
		vector<pair<int, int>> senate(n);
		for (int i = 0; i < n; ++i) {
			senate[i].second = i;
			cin >> senate[i].first;
			count += senate[i].first;
		}

		sort(senate.rbegin(), senate.rend());
		
		int m = n;
		while (count) {
			ofs << char(senate[0].second + 'A');
			senate[0].first--;
			if (senate[0].first == 0) m--;
			count--;

			if ((/*m != 2 &&*/ count != 2) && senate[1].first > 0)
			{
				ofs << char(senate[1].second + 'A');
				senate[1].first--;
				if (senate[1].first == 0) m--;
				count--;
			}
						
			ofs << " ";

			sort(senate.rbegin(), senate.rend());			
		}
		ofs << endl;
		x++;
	}
}