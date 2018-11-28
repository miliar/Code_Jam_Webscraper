#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void allPerms(string s, vector<string>& perms) {
	string start_str(1, s[0]);
	perms.push_back(start_str);
	for (int i = 1; i < s.size(); ++i) {
		int permSize = perms.size();
		for (int j = 0; j < permSize; ++j) {
			string s1 = perms[j] + s[i];
			string s2 = s[i] + perms[j];
			if (s1.compare(s2) > 0) {
				perms.push_back(s1);
			} else {
				perms.push_back(s2);
			}
		}

		while (perms[0].size() <= i) {
			//perms.erase(remove(perms.begin(), perms.end(), 0), perms.end());
			perms.erase(perms.begin(), perms.begin() + 1);
		}
	}
}

int main() {
	int numCases;
	cin >> numCases;
	for (int caseNum = 1; caseNum <= numCases; ++caseNum) {
		string inword;
		cin >> inword;
		vector<string> perms;
		allPerms(inword, perms);
		sort(perms.begin(), perms.end());
		cout << "Case #" << caseNum << ": " << perms.back() << endl;
		//for (int i = 0; i < perms.size(); ++i) {
		//	cout << perms[i] << endl;
		//}
	}
	return 0;
}
