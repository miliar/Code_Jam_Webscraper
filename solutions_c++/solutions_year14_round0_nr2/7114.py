#include <iostream>
#include <fstream>

using namespace std;

int main(){
	ifstream fin("in.txt");
	ofstream fout("out.txt");
	fout.setf(fout.fixed);
	fout.precision(7);

	int t;
	fin >> t;
	for(int i = 0; i < t; i++){
		double c, f, x, cps = 2.0, time = 0.0;
		fin >> c >> f >> x;

		while(c/cps+x/(cps+f) < x/cps){
			time += c/cps;
			cps += f;
		}
		time += x/cps;
		fout << "Case #" << (i+1) << ": " << time << "\n";
	}
	return 0;
}
