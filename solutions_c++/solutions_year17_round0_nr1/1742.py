#include <fstream>
#include <iostream>
#include <string>

using namespace std;

//#define SMALL_INPUT
#define LARGE_INPUT

#if defined(SMALL_INPUT)
std::ifstream fin("D:\\develop\\GCJ\\data\\small.in");
std::ofstream fout("D:\\develop\\GCJ\\data\\small.out");
#define gin fin
#define gout fout
#elif defined(LARGE_INPUT)
std::ifstream fin("D:\\develop\\GCJ\\data\\large.in");
std::ofstream fout("D:\\develop\\GCJ\\data\\large.out");
#define gin fin
#define gout fout
#else
#define gin cin
#define gout cout
#endif

class Solver
{
public:
	int	Solve(string s, int k)
	{
		int ret = 0;
		for (size_t i = 0; i <= s.length()-k; ++i)
		{
			if (s[i] == '+') continue;

			for (size_t j = i; j < i + k; ++j)
			{
				if (s[j] == '-') s[j] = '+';
				else s[j] = '-';
			}

			++ret;
		}

		for (size_t i = 0; i < s.length(); ++i)
		{
			if (s[i] == '-')
			{
				ret = -1;
				break;
			}
		}

		return ret;
	}
};

int main()
{
	int t;
	gin >> t;

	for (int i = 1; i <= t; ++i)
	{
		string s;
		int k;
		gin >> s >> k;

		Solver sovler;
		int ret = sovler.Solve(s, k);

		gout << "Case #" << i << ": ";
		if (ret >= 0) gout << ret << "\n";
		else gout << "IMPOSSIBLE\n";
	}

	return 0;
}