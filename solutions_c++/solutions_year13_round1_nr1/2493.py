#include <fstream>
#include <cmath>
using namespace std;


int main()
{
	ifstream fin("input.txt");
	ofstream fout("output.txt");

	int n;
	fin >> n;
	for (int i = 0; i < n; ++i) {
		long long r, t;
		fin >> r >> t;

		long long paint = 
			(0.25 + sqrt((0.5*r-0.25)*(0.5*r-0.25) + 0.5*t) - 0.5*r);

		fout << "Case #" << i + 1 << ": " << paint << endl;
	}
}