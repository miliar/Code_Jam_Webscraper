
#define PROBLEM_NAME "A"
#define PROBLEM_SMALL_INPUT "-small-attempt0"
#define PROBLEM_LARGE_INPUT "-large"

#include <set>

int main(int argc, char* argv[])
{
//	set_fio(PROBLEM_NAME ".txt");
//	set_fio(PROBLEM_NAME PROBLEM_SMALL_INPUT ".in");
//	set_fio(PROBLEM_NAME PROBLEM_SMALL_INPUT ".in", PROBLEM_NAME PROBLEM_SMALL_INPUT ".out.txt");
//	set_fio(PROBLEM_NAME PROBLEM_LARGE_INPUT ".in");
	set_fio(PROBLEM_NAME PROBLEM_LARGE_INPUT ".in", PROBLEM_NAME PROBLEM_LARGE_INPUT ".out.txt");

	int T;
	fin >> T;
	for (int cases=1; cases<=T; ++cases)
	{
		int Smax;
		fin >> Smax;

		std::string str;
		fin >> str;

		int addition = 0;

		int sum = str[0] - '0';
		for (size_t i=1; i<str.length(); ++i)
		{
			int curr_audience = str[i] - '0';
			if (curr_audience > 0)
			{
				if (sum >= i)
				{
					sum += curr_audience;
				}
				else
				{
					int a = i - sum;// + curr_audience;
					addition += a;
					sum += a + curr_audience;
				}
			}
		}

		fout << "Case #" << cases << ": " << addition << endl;
	}

	return 0;
}
