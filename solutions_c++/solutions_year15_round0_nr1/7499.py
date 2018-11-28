#include <iostream>
#include <fstream>
using namespace std;

int solve(int * arr, int n) {
	int result = 0;
	int* dp = new int[n];
	dp[0] = 0;
	for (int i = 1; i < n; i++) {
		dp[i] = arr[i - 1] + dp[i - 1];
		if (dp[i] <= i) {
			int lack = i - dp[i];
			result += lack;
			dp[i] += lack;
		}
	}
	return result;
}

int main() {
	ifstream fin("d:/A-large.in");
	ofstream fout("d:/ouput.txt");
	int n = 0;
	fin >> n;
	for (int i = 0; i < n; i++) {
		int m = 0;
		fin >> m;
		int* arr = new int[m + 1];
		for (int j = 0; j <= m + 1; j++) {
			char chr;
			if (fin.get(chr) != 0) {
				if (j > 0) {
					arr[j - 1] = chr - '0';
				}
			}
		}
		fout << "Case #" << i + 1 << ": " << solve(arr, m + 1) << endl;
		delete [] arr;
	}
	fin.close();
	system("pause");
}

