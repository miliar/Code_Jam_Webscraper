#include <iostream>
#include <fstream>
#include <vector>

using namespace::std;

ifstream fin("B-large.in");
ofstream fout("B-large.out");
vector<int> pancakes;
int n, t, ans, cur;

int main() {
	fin >> t;
	for (int i = 0; i < t; i++) {
		fin >> n;
		pancakes.clear();
		for (int j = 0; j < n; j++) {
			fin >> cur;
			pancakes.push_back(cur);
		}
		ans = INT_MAX;
		for (int j = 1; j <= 1000; j++) {
			cur = j;
			for (int k = 0; k < n; k++)
				cur += (pancakes[k] - 1) / j;
			ans = (ans > cur) ? cur : ans;
		}
		fout << "Case #" << i + 1 << ": " << ans << endl;
	}
}