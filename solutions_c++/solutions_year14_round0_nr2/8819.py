// list::sort
#include <list>
#include <string>
#include <cctype>
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <sstream>
#include <iomanip> 
using namespace std;

void main()
{
	double x;// = 2000;
	double c;// = 500;
	double f;// = 4.0;
	int t;

	ifstream filein;
	filein.open("B-large.in");
	if (!filein.is_open()) return;

	ofstream fileout;
	fileout.open("Bout.txt");
	if (!fileout.is_open()) return;

	fileout.precision(7);

	filein >> t;

	for (int i = 1; i <= t; i++)
	{
		ostringstream strst;
		strst << i;
		string st = strst.str();
		string returns = "Case #" + st + ": ";
		fileout<<returns;
		filein >> c;
		filein >> f;
		filein >> x;

		double startf = 2.0;
		double startcook = 0;

		double secs = 0.0;
		double secspast = 0.0;

	while(startcook == 0)
	{
		secs = c/startf;
		secspast = secspast + secs;
		while((x/startf)>((c/startf)+(x/(startf+f))))
		{
					startf = startf + f;
					secs = c/startf;
					secspast = secspast + secs;
					startcook = 0;
		}
		secspast = secspast - secs;
		secspast = secspast + (x/startf);
		startcook = x;
	
	}

	fileout<<fixed<<secspast<<"\n";
	}
	fileout.close();
	filein.close();
	return;
}