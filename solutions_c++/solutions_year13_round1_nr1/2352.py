/*
https://code.google.com/codejam/contest/351101/dashboard#s=p1

 *
 */
#include <iostream>
#include <fstream>
#include <algorithm>
#include <stack>

using namespace std;

int main()
{


	ifstream inf;
	ofstream outf;
	inf.open("A-small-attempt0.in", ios::in);
	outf.open("output.txt");

	double t;
	double r;
	double T;
	char c;
	string str, str2 = "";
	stack<string> q;
	char* arr[200];

	inf >> T;
	cout << T << endl;

	//getline(inf,str);

	for(int i = 0; i < T; i++) {
		//getline(inf,str);

		inf >> r;
		inf >> t;


		unsigned long long rings = 0;
		cout << r << "," << t << "," << i << endl;

		double x = ((r+1) * (r+1)  - (r * r) );

		while(t > 0) {
			t = t - x;
			rings++;
			x += 4;
		}
		if(t < 0)	--rings;

		//rings = (t-x) / (4*x);
		outf << "Case #" << (i+1) << ": " << rings << endl;

	}

	inf.close();
	outf.close();
	return 0;
}
