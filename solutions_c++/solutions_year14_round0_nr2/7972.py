#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

int main () {
	ifstream fin ("B-large.in");
	if (!fin)  // validation
		return 1;
	ofstream fout ("B-large.out");
	if (!fout)  // validation
		return 1;

	int num;
	fin >> num;
	if (num < 1 || num > 100)
		return 1;

	int i = 0;
	while (i < num) {
		long double C, R = 2, F, X;

		fin >> C;
		if (C < 1 || C > 10000)
			return 1;
		
		fin >> F;
		if (F < 1 || F > 100)
			return 1;
		
		fin >> X;
		if (X < 1 || X > 100000)
			return 1;
		
		long double timeElapsed = C / R;
		long double c = C;
			
		while (c != X) {
            if ((X / (R + F)) < ((X - C) / R)) {		
				R = R + F;
                timeElapsed = timeElapsed + C / R;
                c = C;
            }
            else {
				timeElapsed = timeElapsed + (X - C) / R;
                c = X;
            }
        }

		fout << "Case #" << i + 1 << ": " << setprecision (7) << showpoint << fixed << timeElapsed << endl;
		i++;
	}

	fout.close ();
	fin.close ();
	return 0;
}