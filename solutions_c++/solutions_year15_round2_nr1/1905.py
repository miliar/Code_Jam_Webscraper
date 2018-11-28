#include <iostream>
#include <fstream>
#include <sstream>
using namespace std;

int a[15];
int p[10];

int solve(string n) {
		int m = n.length();
		if (m == 1) {
			stringstream ss(n);
			int ans;
			ss >> ans;
			return ans;
		}
		int secondhalf = 0;
		for (int i = m/2; i < m; i++) secondhalf = secondhalf * 10 + n[i] - '0';
		if (secondhalf == 0) {
			stringstream ss(n);
			int tmp;
			ss >> tmp;
			tmp--;
			stringstream ss2;
			ss2 << tmp;
			string tmps;
			ss2 >> tmps;
			return solve(tmps)+1;
		}
		
		int ans = 0;
		ans += a[n.length()-1];
		if (m % 2 == 0) {
			bool b0 = false;
			bool b1 = true;
			if (n[0] == '1') b0 = true;
			for (int i = 1; i < m/2; i++) if (n[i] != '0') b1 = false;
			if (b0 && b1) {
				ans += secondhalf;
			} else {
				int add = 0;
				for (int i = m/2-1; i >= 0; i--) add = add * 10 + n[i] - '0';
				ans += secondhalf + add;
			}
		} else {
			bool b0 = false;
			bool b1 = true;
			if (n[0] == '1') b0 = true;
			for (int i = 1; i < m/2; i++) if (n[i] != '0') b1 = false;
			if (b0 && b1) {
				ans += secondhalf;
			} else {
				int add = 0;
				for (int i = m/2-1; i >= 0; i--) add = add * 10 + n[i] - '0';
				ans += secondhalf + add;
			}
		}
		return ans;
}

int main() {
	ifstream fin("in");
	ofstream fout("out");
	int T = 0;
	fin >> T;
	
	a[0] = 1;
	a[1] = a[0] + 9;
	a[2] = a[1] + 9 + 1 + 9;
	a[3] = a[2] + 9 + 1 + 99;
	a[4] = a[3] + 99 + 1 + 99;
	a[5] = a[4] + 99 + 1 + 999;
	a[6] = a[5] + 999 + 1 + 999;
	a[7] = a[6] + 999 + 1 + 9999;
	a[8] = a[7] + 9999 + 1 + 9999;
	a[9] = a[8] + 9999 + 1 + 99999;
	a[10]= a[9] + 99999 + 1 + 99999;
	a[11]= a[10]+ 99999 + 1 + 999999;
	a[12]= a[11]+ 999999 + 1 + 999999;
	a[13]= a[12]+ 999999 + 1 + 9999999;
	a[14]= a[13]+ 9999999 + 1 + 9999999;
	
	p[1] = 9;
	p[2] = 99;
	p[3] = 999;
	p[4] = 9999;
	p[5] = 99999;
	p[6] = 999999;
	p[7] = 9999999;
	
	for (int TT = 0; TT < T; TT++) {
		string n;
		fin >> n;
		int ans = solve(n);
		fout << "Case #" << TT+1 << ": " << ans << endl;
	}
	return 0;
}
