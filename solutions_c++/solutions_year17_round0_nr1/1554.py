#define WIN32_LEAN_AND_MEAN
#define VC_EXTRALEAN
#define _CRT_SECURE_NO_WARNINGS

#include <windows.h>

#include <iostream>
#include <string>

#include <array>
#include <vector>
#include <map>
#include <unordered_map>
#include <set>
#include <unordered_set>
#include <queue>

#define FILE_NAME "A-large"

static constexpr auto in_file = R"(c:\users\shachar\downloads\)" FILE_NAME ".in";
static constexpr auto out_file = R"(c:\users\shachar\downloads\)" FILE_NAME ".out";

using namespace std;

string solve(string pancakes, int K)
{
	int flips = 0;

	size_t cur = 0;
	while (true)
	{
		auto idx = pancakes.find_first_of('-', cur);
		if (idx == pancakes.npos)
		{
			break;
		}

		++flips;
		for (auto i = idx; i < idx + K; ++i)
		{
			if (i >= pancakes.size())
			{
				return "IMPOSSIBLE";
			}

			if (pancakes[i] == '-') {
				pancakes[i] = '+';
				continue;
			}

			if (pancakes[i] == '+') {
				pancakes[i] = '-';
				continue;
			}
		}
	}
	return to_string(flips);
}

int main(int argc, char* argv[])
{
	UNREFERENCED_PARAMETER(argc);
	UNREFERENCED_PARAMETER(argv);

	freopen(in_file, "r", stdin);
	freopen(out_file, "w", stdout);

	int tests;

	cin >> tests;

	for (auto test_case = 0; test_case < tests; ++test_case)
	{
		string pancakes;
		int K;
		cin >> pancakes >> K;
		const string solution = solve(pancakes, K);
		cout << "Case #" << test_case + 1 << ": " << solution.c_str() << "\n";
	}
}
