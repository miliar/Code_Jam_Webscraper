#include <fstream>

#define MAX_N 1000

using namespace std;

ifstream fin("D:\\Input.txt");
ofstream fout("D:\\Output.txt");

int T, N, answer, values[MAX_N + 1];

int main(int argc, const char* argv[])
{
	fin >> T;
	for(int i = 0; i < T; i++)
	{
		answer = 0;
		fin >> N;
		char a;
		for(int j = 0; j < N + 1; j++)
			fin >> a, values[j] = a - '0';
		int running_total = 0;
		for(int j = 0; j < N + 1; j++)
		{
			if(running_total >= j)
				running_total += values[j];
			else
			{
				int delta = j - running_total;
				answer += delta, running_total += delta + values[j];
			}
		}
		fout << "Case #" << i + 1 << ": " << answer << "\n";
	}
	return 0;
}