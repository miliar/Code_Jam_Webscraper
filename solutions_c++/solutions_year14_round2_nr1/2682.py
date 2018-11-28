#include <iostream>
#include <set>
#include <algorithm>
#include <vector>
#include <iterator>
#include <fstream>
#include <math.h>
#include <map>
#include <utility>
#include <string>
#include <list>
#include <time.h>
#include <queue>


void solveonecase(int caseN, std::istream& in, std::ostream& out)
{
	int N;
	in >> N;

	std::vector<std::string> originals(N);
	for(int i = 0; i < N; ++i)
		in >> originals[i];

	std::string shortstr;
	std::unique_copy(originals[0].begin(), originals[0].end(), std::back_inserter(shortstr));

	//check
	for(int i = 1; i < N; ++i)
	{
		std::string temp;
		std::unique_copy(originals[i].begin(), originals[i].end(), std::back_inserter(temp));

		if(temp != shortstr)
		{
			out << "Case #" << caseN << ": Fegla Won\n";
			return;
		}
	}
	int num = shortstr.length();
	std::vector<std::vector<int> > mmm(N, std::vector<int>(num));

	for(int i = 0; i < N; ++i)
	{
		mmm[i][0] = originals[i].find_first_not_of(shortstr[0]);

		int last = mmm[i][0];
		int prevlast = last;
		for(int j = 1; j < num - 1; ++j)
		{
			last = originals[i].find_first_not_of(shortstr[j], last + 1);
			mmm[i][j] = last - prevlast;
			prevlast = last;
		}
		mmm[i][num - 1] = originals[i].length() - last;
	}

	int result = 0;

	for(int i = 0; i < num; ++i)
	{
		int sum = 0;
		for(int j = 0; j < N; ++j)
			sum += mmm[j][i];

		double M = (double) sum;
		M /= N;
		
		int median = M + 0.5;

		for(int j = 0; j < N; ++j)
			result += std::abs(mmm[j][i] - median);
	}

	out << "Case #" << caseN << ": " << result << "\n";

}




int main(void)
{
	int T;

	std::ifstream in("A-small-attempt1.in");
	std::ofstream out("A-small-attempt1.out");
	
	in >> T;

	for (int i = 1; i <= T; ++i)
		solveonecase(i, in, out);

	return 0;
}