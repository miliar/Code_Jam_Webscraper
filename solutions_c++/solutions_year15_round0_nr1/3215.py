#include <iostream>
#include <algorithm>
#include <cstdio>
#include <string>
#include <fstream>
using namespace std;
ifstream fin("1.in");
ofstream fout("1.out");

void solve() {
	int n; fin >> n;
	for (int i = 0; i < n; i ++) {
		int s, sum, ans = 0; string seq;
		fin >> s >> seq;
		sum = seq[0] - '0';
		for (int j=1; j<seq.size(); j++) {
			if (sum < j) { 
				ans += j-sum; sum = j; 
			}
			sum += seq[j] - '0';
		}
		fout << "Case #" << i+1 << ": " << ans << endl;
	}
}

int main() {
	solve(); return 0;
}
