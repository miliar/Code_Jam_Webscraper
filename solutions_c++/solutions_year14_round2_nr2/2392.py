#include <fstream>
using namespace std;
int main()
{
	int t, i, a, b, k, result, j, l;
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	fin >> t;
	for (i = 1; i <= t; i++)
	{
		fin >> a >> b >> k;
		result = 0;
		for (j = 0; j < a; j++)
		for (l = 0; l < b; l++)
		if ((j & l) < k)
			result++;
		fout << "Case #" << i << ": " << result << endl;
	}
	return 0;
}