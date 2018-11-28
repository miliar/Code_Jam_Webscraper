#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>


using namespace std;

void main()

{
	fstream file;
	fstream out;
	string temp;

	long float C, X, F;
	int cases = 1;

	file.open("B-large.in");
	out.open("out.txt");

	while (getline(file, temp))
	{
		file >> C >> F >> X;
		//cout << setprecision(10) << C << " " << setprecision(10) << X << " " << setprecision(10) << F << endl;

		long float winnertime, nexttime;
		long float currentfarmtime, newfarmtime, currentrate, newrate;
		int farms = 1, ct=1;

		
		winnertime = X / 2;
		nexttime = 0;

		currentfarmtime = 0;


		again:
		currentrate = 2 + ((farms - 1) * F);
		currentfarmtime = currentfarmtime + (C / currentrate);
		newrate = 2 + (farms*F);
		nexttime = currentfarmtime + (X / newrate);

		if (winnertime > nexttime)
			{
				winnertime = nexttime;
				farms++;
				goto again;
			}
		

		out << fixed;
		out << "Case #" << cases << ": "<< setprecision(8) << winnertime << endl;
		cases++;

		winnertime = 0;
		nexttime = 0;
		currentfarmtime = 0;
		newfarmtime = 0;
		currentrate = 0;
		newrate = 0;


	}
	cin.get();
}