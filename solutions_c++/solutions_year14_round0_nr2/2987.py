//#include <iostream>
#include <vector>
#include <fstream>
#include <iomanip>
using namespace std;

int main()
{
	ifstream in("in.txt");
	ofstream out("out.txt");
	int T;
	in >> T;
	out << setprecision(7) << std::fixed;
	for (int t=0; t < T; t++) {
		double c, f, x;
		in >> c >> f >> x;
		int N = x/c - 1 - 2/f + 0.9999999; //ceiling N=num farms
		double time=0;
		for (int i = 1; i <= N; i++) {
			time += c/(2+f*i-f);
		}
		if (N < 1) N = 0;
		time += x/(2+f*N);
		out << "Case #" << t+1 << ": " << time << endl;
	}//case
}