#include <fstream>
#include <iostream>
#include <cmath>
#include <string>
#include <vector>
using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

long long result[11];

long long base(long long n, int b) {
	if (b == 10)
		return n;
	//long long ans = 0;
	vector<int> ans;
	while (n) {
		ans.push_back(n%b);
		n /= b;
	}
	long long rans = 0;
	for(int i = ans.size()-1; i>=0; --i) {
		rans = rans * 10 + ans[i];
	}
	return rans;
}

long long inter_base(long long n, long long b) {
	long long ans = 0;
	long long p = 1;
	while (n) {
		ans += (n % 10) * p;
		n /= 10;
		p *= b;
	}
	return ans;
}

long long findDiv(long long k) {
	long long i;
	for (i = 2; i <= sqrt(k); ++i) {
		if (k%i == 0)
			return i;
	}
	return -1;
}

bool check(long long num) {
	int i;
	long long k = base(num, 2);
	for (i = 2; i <= 10; ++i)
	{
		long long m = inter_base(k, i);
		long long l = findDiv(m);
		if (l == -1)
			return false;
		result[i] = l;
	}
	return true;
}

void print(long long m) {
	fout << base(m, 2);
	for (int i = 2; i <= 10; ++i)
		fout << ' ' << result[i];
	fout << endl;
}

void printSol(int n, int j) {
	long long num = pow(2, n - 1) + 1;
	while (j) {
		if (check(num))
		{
			cout << "Found " << num << "   J=" << j << endl;
			--j;
			print(num);
		}
		num += 2;
	}
	return;
}

int main()
{
	int t, n, j;
	fin >> t >> n >> j;
	fout << "Case #1:" << endl;
	printSol(n, j);
	return 0;
}

