#include<iostream>
#include<fstream>
#include<string>
#include<vector>
#include<iomanip>
using namespace std;

int main(int argc, char *argv[])
{
    if (argc!=3) 
    {
	cout << "Missing arguments." << endl;
	return -1;
    }
    ifstream fin(argv[1]);
    ofstream fout(argv[2]);

    int T;
    fin >> T;

    

    

    for (int t = 0; t < T; ++t)
    {
	double C, F, X;

	fin >> C;
	fin >> F;
	fin >> X;

	int n = (F*X-2*C)/(F*C);
	if (n < 0) n = 0;

	cout << n << endl;
	double time = 0;
	for (int i = 0; i < n; ++i)
	    time += C/(2.0+static_cast<double>(i) * F);

	time += X/(2.0+static_cast<double>(n) * F);
	
	fout << "Case #" << t+1 << ": ";
	fout << fixed << setprecision(7) << time << endl;
	
    }
    return 0;
}
