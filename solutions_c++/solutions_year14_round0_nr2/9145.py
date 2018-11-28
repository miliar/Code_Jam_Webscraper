#include <fstream>
#include <iomanip>
#include <iostream>
using namespace std;

int main(int argc, char* args[])
{
	ifstream fin(args[1]);
	ofstream fout(args[2]);	
	
	int n;
	fin >> n;
	for (int t = 1; t <= n; ++t)  {
		cout << "Test " << t << endl;
		double C, F, X;
		fin >> C >> F >> X;
		double sum  = 0;
		double r = 2.;
		double prev = X/r;
		double cur = prev;
		//max (X*F)/C - 2;	
		do {
			prev = cur;
			sum += C/r;
			r += F;
			cur = sum + X/r;					
		} while (cur < prev);
	
	  fout << "Case #" << t << ": " << fixed << setprecision(7) << prev << endl;
	}	
	
	fin.close();
	fout.close();
	return 0;
}
