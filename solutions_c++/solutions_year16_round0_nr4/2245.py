#include <algorithm>
#include <tuple>
#include <vector>
#include <string>
#include <iostream>
#include <fstream>
using namespace std;
using ll = unsigned long long;

int table[(1 << 10)+1];
int ssize;
int nmm = numeric_limits<int>::max() / 2048;
int ans;
ofstream file;

void work(ll testCase)
{
	int k, c, s;
	cin >> k >> c >> s;

	file << "Case #" << testCase << ": ";
	if (c == 1)
	{
		if ((k - 1 + 1) > s) {
			file << "IMPOSSIBLE" << endl;
			return;
		}

		for (int i = 1; i <= k; ++i)
			file << i << ' ';
		file << endl;
	}
	else
	{
		for (int i = 0; i < (k+1)/2; ++i)
			file << (k*i) + (k - i) << ' ';
		file << endl;
	}

}
int main()
{
	file.open("p2.txt");

	int n = 1;
	cin >> n;
	for (int i = 1; i <= n;++i)
	{
		work(i);
	}
}