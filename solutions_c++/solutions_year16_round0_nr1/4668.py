#include <iostream>
#include <fstream>
#include <cstring>
using namespace std;

bool used[10];

bool check(int num) {
	while (num != 0) {
		used[num % 10] = true;
		num /= 10;
	}
	for (int i = 0; i < 10; ++i)
		if (!used[i]) return false;
	return true;
}

int solve(int n) {
	if (n == 0) return -1;
	memset(used, 0, sizeof(used));
	int k = 1;
	while (true) {
		if (check(k * n)) break;
		++k;
	}
	return n * k;
}

int main() {
	ifstream fin("input.txt");
	ofstream fout("output.txt");

	int c;
	fin >> c;
	for (int tc = 1; tc <= c; ++tc) {
		int n;
		fin >> n;
		int ret = solve(n);
		fout << "Case #" << tc << ": ";
		if (ret == -1) fout << "INSOMNIA" << endl;
		else fout << ret << endl;
	}
}