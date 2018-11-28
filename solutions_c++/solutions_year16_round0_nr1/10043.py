#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

ifstream fin("A-small-attempt1.in");
ofstream fout("A-small-attempt1.out");

long long int solve(long long int N)
{
	if (N * 2 == N * 3) return -1;

	vector<char> Int(10, false);
	long long int answer = N;
	long long int i = 0, j = 1;
	while (1)
	{
		answer = N * j;
		while (answer > 0)
		{
			if (!Int[answer % 10])
			{
				Int[answer % 10] = true;
				i++;
			}
			answer /= 10;
		}
		if (i != 10)
			j++;
		else
			break;
	}
	return N * j;
}

int main()
{
	int n = 0;
	fin >> n;
	for (int i = 0; i < n; ++i) {
		long long int N = 0;
		fin >> N;
		long long int answer = solve(N);
		if (answer >= 0)
			fout << "Case #" << i + 1 << ": " << answer << '\n';
		else
			fout << "Case #" << i + 1 << ": " << "INSOMNIA" << '\n';
	}
	return 0;
}