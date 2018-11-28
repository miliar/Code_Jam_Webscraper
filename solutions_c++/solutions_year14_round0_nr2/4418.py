#include <iostream>
#include <vector>
#include <limits>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <iomanip> 
#include <fstream>

using namespace std;

void disp(string s, int r, int c, ofstream& ops)
{
	for(int i = 0; i < r; i++)
	{
		for(int h = 0; h < c; h++)
		{
			ops << s[i * c + h];
		}
		ops << endl;
	}
}

int main()
{
	ifstream ins("C:\\Users\\Mike\\Downloads\\A-small-attempt1 (1).in");
	ofstream ops("C:\\Users\\Mike\\Downloads\\output.txt");
	//istream& ins = cin;
	int t;
	ins >> t;

	for(int g = 0; g < t; g++)
	{
		ops << "Case #" << (g + 1) << ": ";
		double c, f, x;
		ins >> c >> f >> x;
		double r = 2;
		double t = x / r;
		double b = 0;
		while(b + c / r + x / (r + f) < t)
		{
			t = b + c / r + x / (r + f);
			b += c / r;
			r += f;
		}
		ops << setprecision(20) << t << endl;
	}
	ops.close();
	//cin.get();cin.get();
	return 0;
}