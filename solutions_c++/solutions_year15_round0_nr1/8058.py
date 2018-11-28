#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
	ifstream fin;
	fin.open("A-large.in");
	ofstream fout;
	fout.open("A-large.out");

	int t;
	int n;
	string s;

	int i, j;
	int sum;
	int res;

	fin >> t;
	for (j = 1; j <= t; j++)
	{
		fin >> n >> s;
		sum = int(s[0] - '0');
		res = 0;
		for (i = 1; i <= n; i++)
		{
			if (sum < i)
			{
				res++;
				sum++;
			}
			sum += int(s[i] - '0');
		}
		fout << "Case #" << j << ": " << res << endl;
	}
	return 0;
}