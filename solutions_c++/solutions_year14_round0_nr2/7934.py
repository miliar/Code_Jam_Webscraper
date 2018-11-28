#include<iostream>
#include<fstream>
#include<sstream>
#include<conio.h>
#include<cstring>

using namespace std;
typedef unsigned int uint;

int main()
{
	uint testcases = 0;
	double c = 0, f = 0, x = 0;
	ifstream in("E:\\B-large.in", ios::in);
	ofstream out("E:\\testout.in", ios::out);

	string line;

	getline(in, line);
	stringstream ss(line);
	ss >> testcases;

	for (uint i = 1; i <= testcases; i++)
	{
		double rate = 2;
		getline(in, line);
		stringstream ss1(line);
		ss1 >> c >> f >> x;

		double prevTime = UINT_MAX;
		double byTime = 0;
		double currTime = x / 2;
		double prevRate = 0;
		
		while (currTime<prevTime)
		{
			prevRate = rate;
			rate += f;
			prevTime = currTime;
			byTime = byTime + (c / prevRate);
			currTime = byTime + x / rate;
			if (currTime>prevTime)
			{
				currTime = prevTime;
				break;
			}
		}
		out.precision(12);
		out << "Case #" << i << ": " << currTime << endl;
	}
	_getch();
}