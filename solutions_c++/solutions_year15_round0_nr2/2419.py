#include <fstream>
#include <algorithm>
#include <cmath>

#define MAX_N 1000
#define INFINITY 10000000000

using namespace std;

ifstream fin("D:\\Input.txt");
ofstream fout("D:\\Output.txt");

int T, N, answer, values[MAX_N];

int main(int argc, const char* argv[])
{
	fin >> T;
	for(int i = 0; i < T; i++)
	{
		answer = INFINITY;
		fin >> N;
		int max_value = 0;
		for(int j = 0; j < N; j++)
			fin >> values[j], max_value = max(max_value, values[j]);
		for(int j = 1; j <= max_value; j++)
		{
			int temp = 0;
			for(int k = 0; k < N; k++)
				temp += (ceil((double)values[k] / (double)j) - 1);
			answer = min(answer, temp + j);
		}
		fout << "Case #" << i + 1 << ": " << answer << "\n";
	}
	return 0;
}