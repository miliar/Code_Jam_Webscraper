#ifdef _MSC_VER
//#define _CRTDBG_MAP_ALLOC
#include <stdlib.h>
#include <crtdbg.h>
#endif

#include "..\Source\Jams.h"
#include "..\Source\CodeJam.h"
#include <set>

class Jam1 : public CodeJam {
protected:	

	void solve(int task) override {
		long long p, q;
		string s;
		readln(s);
		stringstream ss(s);
		char c;
		ss >> p >> c >> q;

		// normalize
		int gens = 1;

		while (p * 2 < q) {
			if (q % 2 == 0)
				q /= 2;
			else {
				writeResult("impossible");
				return;
			}				
			gens++;
		}

		while (q > 1) {
			if (q % 2 == 0)
				q /= 2;
			else {
				writeResult("impossible");
				return;
			}			
		}

		writeResult(gens);		
	}
};


int main()
{	
	Jam1 m;
	m.solveJam("c");
	return 0;
}

