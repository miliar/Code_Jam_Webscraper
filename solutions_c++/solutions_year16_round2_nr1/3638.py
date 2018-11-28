#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <map>

using namespace std;

//A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
//0 1 2 3 4 5 6 7 8 9 10111213141516171819202122232425

map<vector<int>, vector<int> > m;

vector<int> next(vector<int> l) {
	bool isZero = true;
	for (int i = 0; i < l.size(); ++i) {
		if (l[i] != 0)
			isZero = false;
	}
	if (isZero) {
		vector<int> emp(1);
		emp[0] = -1;
		return emp;
	}
	vector<int> org = l;
	vector<int> ret(1);
	bool finish = false;
	if (l[25] > 0 && l[4] > 0 && l[17] > 0 && l[14] > 0) {
		--l[25];
		--l[4];
		--l[17];
		--l[14];
		ret = next(l);
		if (ret[0] == -1) {
			ret.push_back(0);
			finish = true;
		}
	}
	l = org;
	if (!finish && l[14] > 0 && l[13] > 0 && l[4] > 0) {
		--l[14];
		--l[13];
		--l[4];
		ret = next(l);
		if (ret[0] == -1) {
			ret.push_back(1);
			finish = true;
		}
	}
	l = org;
	if (!finish && l[19] > 0 && l[22] > 0 && l[14] > 0) {
		--l[19];
		--l[22];
		--l[14];
		ret = next(l);
		if (ret[0] == -1) {
			ret.push_back(2);
			finish = true;
		}
	}
	l = org;
	if (!finish && l[19] > 0 && l[7] > 0 && l[17] > 0 && l[4] > 1) {
		--l[19];
		--l[7];
		--l[17];
		--l[4];
		--l[4];
		ret = next(l);
		if (ret[0] == -1) {
			ret.push_back(3);
			finish = true;
		}
	}
	l = org;
	if (!finish && l[5] > 0 && l[14] > 0 && l[20] > 0 && l[17] > 0) {
		--l[5];
		--l[14];
		--l[20];
		--l[17];
		ret = next(l);
		if (ret[0] == -1) {
			ret.push_back(4);
			finish = true;
		}
	}
	l = org;
	if (!finish && l[5] > 0 && l[8] > 0 && l[21] > 0 && l[4] > 0) {
		--l[5];
		--l[8];
		--l[21];
		--l[4];
		ret = next(l);
		if (ret[0] == -1) {
			ret.push_back(5);
			finish = true;
		}
	}
	l = org;
	if (!finish && l[18] > 0 && l[8] > 0 && l[23] > 0) {
		--l[18];
		--l[8];
		--l[23];
		ret = next(l);
		if (ret[0] == -1) {
			ret.push_back(6);
			finish = true;
		}
	}
	l = org;
	if (!finish && l[18] > 0 && l[4] > 1 && l[21] > 0 && l[13] > 0) {
		--l[18];
		--l[4];
		--l[4];
		--l[21];
		--l[13];
		ret = next(l);
		if (ret[0] == -1) {
			ret.push_back(7);
			finish = true;
		}
	}
	l = org;
	if (!finish && l[4] > 0 && l[8] > 0 && l[6] > 0 && l[7] > 0 && l[19] > 0) {
		--l[4];
		--l[8];
		--l[6];
		--l[7];
		--l[19];
		ret = next(l);
		if (ret[0] == -1) {
			ret.push_back(8);
			finish = true;
		}
	}
	l = org;
	if (!finish && l[13] > 1 && l[8] > 0 && l[4] > 0) {
		--l[13];
		--l[13];
		--l[8];
		--l[4];
		ret = next(l);
		if (ret[0] == -1) {
			ret.push_back(9);
			finish = true;
		}
	}
	//m[org] = ret;
	return ret;
}

int main() {
	int t;
	ifstream input("input.in");
	input >> t;
	ofstream output;
	output.open("output.txt");
	string s;
	for (int i = 0; i < t; ++i) {
		input >> s;
		vector<int> l(26);
		for (int j = 0; j < s.length(); ++j) {
			++l[s[j] - 65];
		}
		vector<int> ans = next(l);
		sort(ans.begin(), ans.end());
		output << "Case #" << i + 1 << ": ";
		for (int j = 1; j < ans.size(); ++j) {
			output << ans[j];
		}
		output << "\n";
		/*for (int j = 0; j < l.size(); ++j) {
		 cout << l[j] << " ";
		 }*/
	}
}
