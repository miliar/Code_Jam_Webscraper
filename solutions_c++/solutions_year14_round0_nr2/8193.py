#include <iostream>
#include <math.h>
#include <sstream>
#include <vector>
#include <fstream>
#include <string>
#include <cstdlib>
#include <iomanip>   

using namespace std;

int main() {

	ifstream fin; fin.open("testinput.in");
	ofstream fout; fout.open("output.txt");

	int cases;
	double farmcost, increase, target, targetwaqt, farmwaqt, ans, cookierate;
	int casenumber = 1;
	
	fin >> cases;
	while (!fin.eof()) {
		if(casenumber > cases) break;

		ans = 0;
		cookierate = 2;
		fout << "Case #" << casenumber++ << ": ";

		fin >> farmcost;
		fin >> increase;
		fin >> target;
	

		while(1) {

			targetwaqt = ans + target/cookierate;
			farmwaqt = ans + farmcost/cookierate + target/(cookierate+increase);

			if (farmwaqt < targetwaqt) {
				ans += farmcost/cookierate;
				cookierate += increase;
			} else break;

		}

		ans += target/cookierate;

		fout << setprecision(9) << ans << endl;

	}

	fin.close();
	fout.close();

	system ("pause");


}
