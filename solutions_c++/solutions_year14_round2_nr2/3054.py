#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#define MAX_N 150

using namespace std;

int a, b, k, t;

int main() {
	ifstream fin ("B-small-attempt0.in");
	//ifstream fin ("A-large.in");
	ofstream fout ("lottery.out");
	fin >> t;
	for (int i = 1; i <= t; i++) {
		fin >> a >> b >> k;
		int ans = 0;
		for (int j = 0; j < a; j++) {
			for (int l = 0; l < b; l++) {
				int bit = j & l;
				if (bit < k)
					ans++;
			}
		}
		fout << "Case #" << i << ": " << ans << endl;
	}
}
