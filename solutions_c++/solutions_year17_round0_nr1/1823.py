#include<iostream>
#include<fstream>
#include<stdio.h>
#include<string>
#include<vector>
#include<map>
#include<math.h>
#include<algorithm>
#include<iomanip>


using namespace std;

int main() {
	int n;
	ofstream ofs("out.txt");
	ifstream ifs("in.in");
	
	ifs >> n;
	for (int i = 0; i < n; i++) {
		vector<int> p;
		int k, ans = 0;
		string s;
		ifs >> s >> k;
		p.resize(s.size());
		for (int j = 0; j < s.size(); j++)
			p[j] = s[j] == '+' ? 0 : 1;
		for (int j = 0; j < s.size() - k + 1; j++) {
			if (p[j] == 1) {
				ans++;
				for (int h = 0; h < k; h++) {
					p[j + h] = p[j + h] == 1 ? 0 : 1;
				}
			}
		}
		bool b = true;
		for (int j = 0; j < s.size(); j++) {
			if (p[j] == 1) {
				b = false;
			}
		}
		ofs << "CASE #" << (i + 1) << ": ";
		if (b) {
			ofs << ans << endl;
		}
		else {
			ofs << "IMPOSSIBLE" << endl;
		}
	}

	return 0;
}