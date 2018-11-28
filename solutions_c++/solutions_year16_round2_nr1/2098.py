#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;
int main() {
	int t, test, i;
	cin >> t;
	for (test=1;test<=t;test++) {
		vector<int> res;
		map<char, int> count;

		string s;
		cin >> s;
		int n=s.size();
		for (i=0;i<n;i++)
			count[s[i]]++;

		if (count['Z'] > 0) {
			int m = count['Z'];
			for (int j=0;j<m;j++){
				res.push_back(0);
				count['Z']--;
				count['E']--;
				count['R']--;
				count['O']--;
			}
		}

		if (count['W'] > 0) {
			int m = count['W'];
			for (int j=0;j<m;j++){
				res.push_back(2);
				count['T']--;
				count['W']--;
				count['O']--;
			}
		}

		if (count['U'] > 0) {
			int m = count['U'];
			for (int j=0;j<m;j++){
				res.push_back(4);
				count['F']--;
				count['O']--;
				count['U']--;
				count['R']--;
			}
		}

		if (count['F'] > 0) {
			int m = count['F'];
			for (int j=0;j<m;j++){
				res.push_back(5);
				count['F']--;
				count['I']--;
				count['V']--;
				count['E']--;
			}
		}

		if (count['X'] > 0) {
			int m = count['X'];
			for (int j=0;j<m;j++){
				res.push_back(6);
				count['S']--;
				count['I']--;
				count['X']--;
			}
		}

		if (count['G'] > 0) {
			int m = count['G'];
			for (int j=0;j<m;j++){
				res.push_back(8);
				count['E']--;
				count['I']--;
				count['G']--;
				count['H']--;
				count['T']--;
			}
		}

		if (count['H'] > 0) {
			int m = count['H'];
			for (int j=0;j<m;j++){
				res.push_back(3);
				count['T']--;
				count['H']--;
				count['R']--;
				count['E']--;
				count['E']--;
			}
		}

		if (count['V'] > 0) {
			int m = count['V'];
			for (int j=0;j<m;j++){
				res.push_back(7);
				count['S']--;
				count['E']--;
				count['V']--;
				count['E']--;
				count['N']--;
			}
		}

		if (count['I'] > 0) {
			int m = count['I'];
			for (int j=0;j<m;j++){
				res.push_back(9);
				count['N']--;
				count['I']--;
				count['N']--;
				count['E']--;
			}
		}

		if (count['O'] > 0) {
			int m = count['O'];
			for (int j=0;j<m;j++){
				res.push_back(1);
				count['O']--;
				count['N']--;
				count['E']--;
			}
		}

		sort(res.begin(), res.end());
		cout << "Case #" << test << ": ";
		for (i=0;i<res.size();i++)
			cout << res[i];
		cout << endl;
	}
	return 0;
}