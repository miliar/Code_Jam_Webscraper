#include <iostream>
#include <iomanip>
#include <fstream>
using namespace std;

int p;
double c, f, x, time, best, now;

int main() {
	ifstream fin("B-small-attempt0.in");
	ofstream fout("output.txt");
	
	fin >> p;
	for (int test=1; test<=p; test++){ 
		fin >> c >> f >> x;
		double speed = 2.0;
		time = best = x/speed;
		now = 0;
		
		while (1) {
			now = now+c/speed;
			speed = speed+f;
			time = now+x/speed;
			if (time > best) break;
			else best = time;
		}
		fout << "Case #" << test << ": " << fixed << setprecision(7) << best <<endl;
	}

	fin.close();
	fout.close();
}
