
#define PROBLEM_NAME "A"
#define PROBLEM_SMALL_INPUT "-small-attempt0"
#define PROBLEM_LARGE_INPUT "-large"

#include <map>

struct Disc
{
	int totalSize;
	std::vector<int> S;
};

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
		int N, X;
		fin >> N >> X;
		std::vector<int> S;
		S.reserve(N);
		for (int i=0; i<N; ++i)
		{
			int s;
			fin >> s;
			S.push_back(s);
		}
		std::sort(S.begin(), S.end());

		std::multimap<int, Disc*, std::greater<int> > discs;
		std::multimap<int, Disc*, std::greater<int> > fulldiscs;

		for (int i=0; i<N; ++i)
		{
			int size = S.back();
			S.pop_back();

			bool disc_found = false;
			for (std::multimap<int, Disc*, std::greater<int> >::iterator it = discs.begin(); it != discs.end(); ++it)
			{
				Disc* pDisc = (*it).second;
				if (pDisc->totalSize + size <= X)
				{
					discs.erase(it);
					pDisc->totalSize += size;
					pDisc->S.push_back(i);
					disc_found = true;
					if (pDisc->S.size() >= 2)
					{
						fulldiscs.insert(std::make_pair(pDisc->totalSize, pDisc));
					}
					else
					{
						discs.insert(std::make_pair(pDisc->totalSize, pDisc));
					}
					break;
				}
			}

			if (disc_found)
				continue;

			Disc* pDisc = new Disc;
			pDisc->totalSize = size;
			pDisc->S.push_back(i);
			discs.insert(std::make_pair(pDisc->totalSize, pDisc));
		}

		fout << "Case #" << cases << ": " << (discs.size() + fulldiscs.size()) << endl;

		for (std::multimap<int, Disc*, std::greater<int> >::iterator it = discs.begin(); it != discs.end(); ++it)
		{
			Disc* pDisc = (*it).second;
			delete pDisc;
		}
	}

	return 0;
}
