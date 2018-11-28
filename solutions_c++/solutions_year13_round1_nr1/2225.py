#include <iostream>
#include <fstream>
using namespace std;

ifstream fin("file.in");
ofstream fout("file.out");

int main()
{
	int n;
	fin >> n;

	int r, t;
	int result;
	int sum;
	int first;
	for (int i = 0; i < n; i++)
	{
		fin >> r >> t;

		first = r + r + 1;
		sum = first;
		result = 1;
		while (sum <= t)
		{
			sum += first + 4*result;
			result++;
		}
		result --;

		fout << "Case #" << i+1 << ": " << result << endl; 

	}

	return 0;

}