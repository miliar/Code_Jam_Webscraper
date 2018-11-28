#include <iostream>
#include <cstdio>
#include <algorithm>
#include <fstream>
#include <map>
#include <queue>
using namespace std;
ifstream fin("1.in");
ofstream fout("1.out");

void solve() {
	int n; fin >> n;
	for (int i = 0; i < n; i ++) {
		int d, M = 0, p[1010]; fin >> d;
		for (int j = 0; j < d; j ++) {
			fin >> p[j]; M = max(M, p[j]);
		}
		
		int ans = M;
		for (int j = 1; j <= M; j ++) {
			int tmp = j;
			for (int k = 0; k < d; k ++)
				if (p[k] % j == 0) tmp += p[k]/j - 1;
				else tmp += p[k]/j;
			ans = min(ans, tmp);
		}
		fout << "Case #" << i+1 << ": " << ans << endl;
	}
}

int main() {
	solve(); return 0;
}
