#include <fstream>
#include <iomanip>

using namespace std;

ifstream fin("D:\\Input.txt");
ofstream fout("D:\\Output.txt");

int T;

int main(int argc, const char* argv[])
{
	fin >> T;
	for(int i = 0; i < T; i++)
	{
		double C = 0, F = 0, X = 0, answer = 0;

		fin >> C >> F >> X;
		double rate = 2;
		answer = 0;
		while(X / rate > C / rate + X / (rate + F))
			answer += C / rate, rate += F;
		answer += X / rate;

		fout << fixed << setprecision(9) << "Case #" << i + 1 << ": " << answer << "\n";
	}
	return 0;
}