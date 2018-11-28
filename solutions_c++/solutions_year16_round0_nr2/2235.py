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
		string seq; fin >> seq;
		int target = 1, idx = seq.size() - 1;
		int ans = 0;
		while (idx >= 0) {
			if (target) {
				while (seq[idx] == '+' && idx >= 0) idx --;
				if (idx < 0) break;
				target = 0; ans ++;
			} else {
				while (seq[idx] == '-' && idx >= 0) idx --;
				if (idx < 0) break;
				target = 1; ans ++;
			}
		}
		fout << "Case #" << rk << ": " << ans << endl;
	}
	return 0;
} 
