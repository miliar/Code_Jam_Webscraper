#include <iostream>
#include <fstream>
#include <vector>

using namespace::std;

ifstream fin("A-large.in");
ofstream fout("A-large.out");
int n, t, sum, ans, cur;
char ch;

int main() {
	fin >> t;
	for (int i = 0; i < t; i++) {
		fin >> n;
		sum = 0;
		ans = 0;
		for (int j = 0; j <= n; j++) {
			fin >> ch;
			cur = ch - '0';
			if (sum < j) {
				ans += (j - sum);
				sum += (j - sum);
			}
			sum += cur;
		}
		fout << "Case #" << i + 1 << ": " << ans << endl;
	}
}