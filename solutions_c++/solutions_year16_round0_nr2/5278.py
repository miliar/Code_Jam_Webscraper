
#define PROBLEM_NAME "B"
#define PROBLEM_SMALL_INPUT "-small-attempt0"
#define PROBLEM_LARGE_INPUT "-large"

#include <set>
#include <vector>

using namespace std;

#define HAPPY	1	// '+'
#define BLANK	0	// '-'

// opt. count of n '+'
// = min(

int opt_happy(int* arr, int n);

int opt_blank(int* arr, int n)
{
	if (n == 0)
	{
		return 0;
	}

	if (arr[n-1] == BLANK)
	{
		return opt_blank(arr, n-1);
	}
	else
	{
		return opt_happy(arr, n-1) + 1;
	}
}

int opt_happy(int* arr, int n)
{
	if (n == 0)
	{
		return 0;
	}

	if (arr[n-1] == HAPPY)
	{
		return opt_happy(arr, n-1);
	}
	else
	{
		return opt_blank(arr, n-1) + 1;
	}
}



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
		string S;
		fin >> S;

		vector<int> arr;
		for (size_t i=0; i<S.size(); ++i)
		{
			if (S[i] == '-')
				arr.push_back(BLANK);
			else
				arr.push_back(HAPPY);
		}

		int opt = opt_happy(&arr[0], (int) S.size());

		fout << "Case #" << cases << ": " << opt << endl;
	}

	return 0;
}
