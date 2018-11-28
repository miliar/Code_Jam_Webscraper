#include <fstream>
#include <utility>
#include <algorithm>

#define MAX_N 100000

using namespace std;

ifstream fin("D:\\Input.txt");
ofstream fout("D:\\Output.txt");

int T, N, values[MAX_N];
pair<int, int> answer;

int main(int argc, const char* argv[])
{
	fin >> T;
	for(int i = 0; i < T; i++)
	{
		fin >> N;
		answer = pair<int, int>();
		for(int j = 0; j < N; j++)
			fin >> values[j];
		for(int j = 1; j < N; j++)
			answer.first += -min(0, values[j] - values[j - 1]);
		int rate = 0;
		for(int j = 1; j < N; j++)
			if(values[j] - values[j - 1] < 0)
				rate = max(rate, values[j - 1] - values[j]);
		for(int j = 1; j < N; j++)
			answer.second += min(rate, values[j - 1]);
		fout << "Case #" << i + 1 << ": " << answer.first << " " << answer.second << "\n";
	}
	return 0;
}