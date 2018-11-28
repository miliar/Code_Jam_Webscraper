#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <queue>
#include <fstream>

using namespace std;

set<int> d;

void separate(int n) {
	int a = n;
	while (a > 0) {
		d.insert(a % 10);
		a /= 10;
	}
}

int main() {
	ifstream fin("A-large.in");
	ofstream fout("A.txt");
	int t;
	fin >> t;
	for (int i = 1; i <= t; ++i) {
		d.clear();
		int n, ans;
		fin >> n;
		if (n == 0) fout << "Case #" << i << ": INSOMNIA\n";
		else {
			ans = n;
			separate(ans);
			while (d.size() < 10) {
				ans += n;
				separate(ans);
			}
			fout << "Case #" << i << ": " << ans << endl;
		}
	}
	//cin.get(); cin.get();
	return 0;
}