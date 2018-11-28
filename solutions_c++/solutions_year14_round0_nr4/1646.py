#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

const string input = "d.in",
			 output = "d.out";

int main()
{
	int T;
	ifstream fin(input.c_str());
	ofstream fout(output.c_str());
	
	fin >> T;
	for (int time = 0; time < T; ++time) {
		int n;
		fin >> n;
		vector<double> a(n, 0), b(n, 0);
		for (int i = 0; i < n; ++i)
			fin >> a[i];
		for (int i = 0; i < n; ++i)
			fin >> b[i];
		sort(a.begin(), a.end());
		sort(b.begin(), b.end());
		int ans1 = 0, ans2 = 0;
		int j = 0;
		for (int i = 0; i < n; ++i) {
			while (j < n && a[j] < b[i]) ++j;
			if (j < n) {
				++ans1;
				++j;
			}
		}
		j = n - 1;
		for (int i = n - 1; i >= 0; --i) {
			while (j >= 0 && a[j] > b[i]) --j;
			if (j >= 0) {
				++ans2;
				--j;
			}
		}
		fout << "Case #" << time + 1 << ": " << ans1 << " " << n - ans2 << endl;
	}
	return 0;
}