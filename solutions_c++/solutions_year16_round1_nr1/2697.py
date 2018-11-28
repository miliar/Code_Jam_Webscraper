#include <iostream>
#include <string>
#include <vector>
#include <fstream>
using namespace std;
ifstream fin("1.in");
ofstream fout("1.out");

int main() {
	int T; fin >> T;
	for (int rk = 1; rk <= T; rk ++) {
		string s; fin >> s;
		int len = s.size();
		string ans = "";
		for (int i = 0; i < len; i ++) {
			if (ans == "") ans = s[i];
			else if (s[i] >= ans[0]) ans = s[i] + ans;
			else ans += s[i];
		}
		fout << "Case #" << rk << ": " << ans << endl;
	}
	return 0;
}
 
