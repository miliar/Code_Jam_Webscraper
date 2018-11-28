#ifdef _MSC_VER
//#define _CRTDBG_MAP_ALLOC
#include <stdlib.h>
#include <crtdbg.h>
#endif

#include "..\Source\Jams.h"
#include "..\Source\CodeJam.h"
#include <set>

typedef std::set<double> dvec;
typedef std::vector<double> dvector;

class War : public CodeJam {
protected:	

	int playWar(dvec naomi, dvec ken) {
		int naomiPoints = 0;
		for (auto i : naomi) {
			auto kenbl = ken.upper_bound(i);
			if (kenbl == ken.end()) {
				++naomiPoints;
				ken.erase(ken.begin());
			}
			else
				ken.erase(kenbl);
		}
		return naomiPoints;
	}

	int playDecWar(dvec naomi, dvec ken) {		
		int naomiPoints = 0;

		auto nbeg = naomi.begin();
		auto nend = naomi.end();
		auto kbeg = ken.begin();
		auto kend = ken.end();
		for (; nbeg != nend; )
			if (*nbeg > *kbeg) {
				++nbeg; ++kbeg;
				++naomiPoints;
			}
			else {
				++nbeg; --kend;
			}

		return naomiPoints;
	}

	void solve(int task) override {
		int NBlocks;
		readln(NBlocks);
		auto NaomiBl = readDoubles();
		auto KenBl = readDoubles();

		int warPoints = playWar(dvec(NaomiBl.begin(), NaomiBl.end()), 
			dvec(KenBl.begin(), KenBl.end()));
		int dwarPoints = playDecWar(dvec(NaomiBl.begin(), NaomiBl.end()),
			dvec(KenBl.begin(), KenBl.end()));

		stringstream s;		
		s << dwarPoints << ' ' << warPoints;
		writeResult(s.str());
	}
};


int main()
{	
	War m;
	m.solveJam("w");
	return 0;
}

