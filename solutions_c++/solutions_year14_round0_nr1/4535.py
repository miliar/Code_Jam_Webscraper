#include <iostream>
#include <set>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	int a[4][4];
	
	int T;
	cin >> T;

	for(int t = 1; t <= T; ++t) {
		set<int> s1, s2;
		vector<int> v;

		int c1, c2;
		cin >> c1;

		for(int i = 0; i < 4; ++i) {
			for(int j = 0; j < 4; ++j) {
				cin >> a[i][j];
			}
		}
		
		for(int i = 0; i < 4; ++i) {
			s1.insert(a[c1-1][i]);
		}

		cin >> c2;

		for(int i = 0; i < 4; ++i) {
			for(int j = 0; j < 4; ++j) {
				cin >> a[i][j];
			}
		}

		for(int i = 0; i < 4; ++i) {
			s2.insert(a[c2-1][i]);
		}

		set_intersection(s1.begin(), s1.end(), s2.begin(), s2.end(), back_inserter(v));
		
		cout << "Case #" << t << ": ";

		if(v.size() == 1) {
			cout << v[0] << endl;
		} else if(v.size() == 0) {
			cout << "Volunteer cheated!" << endl;
		} else {
			cout << "Bad magician!" << endl;
		}
	}

}
