#include <iostream>
#include <string>
#include <fstream>
#include <sstream>

using namespace std;

int main()
{
	int T = 0;

	ifstream inf;
	ofstream oufile;
	inf.open("A-small-attempt0.in");
	oufile.open("out.txt");
	string oup;
	inf >> T;
	for( int  c = 0; c < T; c++ )
	{
		unsigned long long t = 0;
		unsigned long long r = 0;
		inf >> r >> t;

		unsigned long long count = 0;
		unsigned long long dax = 2 * r + 4 * count + 1;	
		while( dax <= t )
		{
			t -= dax;
			count++;
			dax = 2 * r + 4 * count + 1;
		}

		//cout << count << endl;
		string oup = "";
		stringstream out;
		out << c + 1;
		stringstream ccoutd;
		ccoutd << count;
		oup = "Case #" + out.str() + ": " + ccoutd.str() + "\n"; 
		oufile << oup;
	}

	oufile.close();
	inf.close();

	system("pause");
	return 0;
}