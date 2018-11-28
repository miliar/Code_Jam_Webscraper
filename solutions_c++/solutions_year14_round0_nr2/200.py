#ifdef _MSC_VER
//#define _CRTDBG_MAP_ALLOC
#include <stdlib.h>
#include <crtdbg.h>
#endif

#include "..\Source\Jams.h"
#include "..\Source\CodeJam.h"

class Cookie : public CodeJam {
protected:
	void solve(int task) override {
		double C, F, X;
		readln(C, F, X);
		double speed = 2.0;
		double eps = 1e-9;
		double time = 0.0;

		while (X > eps) {
			double planeTime = X / speed;
			double farmTime = C / speed + X / (speed + F);
			if (planeTime <= farmTime) {
				time += planeTime;
				X = 0;
			}
			else {
				time += C / speed;
				speed += F;
			}
		}
		output.precision(10);
		cout.precision(10);
		cout << time << endl;
		writeResult(time);
	}
};


int main()
{	
	Cookie m;
	m.solveJam("c");
	return 0;
}

