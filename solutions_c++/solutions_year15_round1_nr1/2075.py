//NTheo 2015

#include <algorithm>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

int main(int, char**)
{

	std::string inname;
	std::string outname;
	std::cout << "input file?" << std::endl;
	std::cin >> inname;
	std::cout << "output file?" << std::endl;
	std::cin >> outname;
	if (outname.empty())
		outname = inname.substr(0, inname.length() - 3) +
		std::string(".out");
	std::ifstream input(inname);
	std::ofstream output(outname);
	int T;
	input >> T;
	for (int t = 0; t < T; t++)
	{
		int N;
		input >> N;
		std::vector<long long> m;
		m.reserve(N);
		for (int n = 0; n < N; n++)
		{
			long long mn;
			input >> mn;
			m.push_back(mn);
		}
		std::vector<long long> diffs;
		diffs.reserve(N - 1);
		for (int n = 0; n < N - 1; n++)
			diffs.push_back(m[n] - m[n + 1]);
		long long w1 = 0;
		for (int n = 0; n < N - 1; n++)
			w1 += (diffs[n]>0) ? diffs[n] : 0;
		long long maxdiff = *std::max_element(diffs.begin(), diffs.end());
		long long w2 = 0;
		for (int n = 0; n < N - 1; n++)
			w2 += std::min(maxdiff, m[n]);
		output << "Case #" << (t + 1) << ": " << w1 << " " << w2 << std::endl;
	}
	std::cout << "done" << std::endl;
	return 0;
}