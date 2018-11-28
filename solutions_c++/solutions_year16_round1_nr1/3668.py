
#define PROBLEM_NAME "A"
#define PROBLEM_SMALL_INPUT "-small-attempt0"
#define PROBLEM_LARGE_INPUT "-large"

#include <list>

using namespace std;

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

		list<char> l;
		for (size_t i=0; i<S.length(); ++i)
		{
			char ch = S[i];
			if (l.empty())
				l.push_back(ch);
			else
			{
				if (l.front() <= ch)
					l.push_front(ch);
				else
					l.push_back(ch);
			}
		}


		fout << "Case #" << cases << ": ";

		for (list<char>::iterator it = l.begin(); it != l.end(); ++it)
		{
			fout << (*it);
		}
		fout << endl;
	}

	return 0;
}
