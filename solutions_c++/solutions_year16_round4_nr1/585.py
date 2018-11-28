#include <iostream>
#include <fstream>
#include <istream>
#include <ostream>
#include <vector>
#include <set>
#include <string>
#include <algorithm>
#include <map>
#include <queue>
using namespace std;




void solve(ifstream& fin, ofstream& fout) {
	int x, y, z,n;
	fin >> n;
	int N = 1 << n;
	fin >> y >> x >> z;
	int xx, yy, zz;
	xx = x; yy = y; zz = z;
	int flag = 1;
	for (int i = 0; i < n; i++) {
		int m = (x + y + z) / 2;
		int a, b, c;
		a = m - z;
		b = m - x;
		c = m - y;
		if (a < 0 || b < 0 || c < 0) {
			flag = 0;
			break;
		}
		x = a; y = b; z = c;
	}
	if (!flag) {
		fout << "IMPOSSIBLE" << endl;
	}
	else {
		int x, y, z;
		x = xx; y = yy; z = zz;
		deque<string> as, bs, cs;
		deque<string> at, bt, ct;
		for (int i = 0; i < xx; i++) as.push_back("P");
		for (int i = 0; i < yy; i++) bs.push_back("R");
		for (int i = 0; i < zz; i++) cs.push_back("S");
		for (int i = 0; i < n; i++) {
			sort(as.begin(), as.end());
			sort(bs.begin(), bs.end());
			sort(cs.begin(), cs.end());
			int m = (x + y + z) / 2;
			at.clear(); bt.clear(); ct.clear();
			int a, b, c;
			a = m - z;
			b = m - x;
			c = m - y;
			for (int j = 0; j < a; j++) {
				string s1 = as.front();
				string s2 = bs.front();
				as.pop_front(); bs.pop_front();
				string ans = s1 < s2 ? s1 + s2 : s2 + s1;
				at.push_back(ans);
			}

			for (int j = 0; j < c; j++) {
				string s1 = as.front();
				string s2 = cs.front();
				as.pop_front(); cs.pop_front();
				string ans = s1 < s2 ? s1 + s2 : s2 + s1;

				ct.push_back(ans);
			}

			for (int j = 0; j < b; j++) {
				string s1 = bs.front();
				string s2 = cs.front();
				bs.pop_front(); cs.pop_front();
				string ans = s1 < s2 ? s1 + s2 : s2 + s1;
				bt.push_back(ans);
			}

			x = a; y = b; z = c;
			as = at; bs = bt; cs = ct;
		}
		if (as.size()) fout << as[0] << endl;
		if (bs.size()) fout << bs[0] << endl;
		if (cs.size()) fout << cs[0] << endl; 
		if (as.size() + bs.size() + cs.size() != 1) cerr << "error" << endl;
	}
}

int main(int argc, char *argv[])
{
	std::ios::sync_with_stdio(false);
	const char* inn;
	if (argc < 2) {
		inn = "c.in";
	}
	else {
		inn = argv[1];
	}
	string in = inn;
	string out = in.replace(in.find(".in"), in.length(), ".out");
	ifstream fin(inn);
	ofstream fout(out);

	int t;
	fin >> t;

	for (int cs = 1; cs <= t; cs++) {
		fout << "Case #" << cs << ": ";
		solve(fin, fout);
	}
	fout.close();

	return 0;
}
