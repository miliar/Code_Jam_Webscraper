#include <iostream>
#include <string>
#include <fstream>
#include <vector>
using std::cout;
using std::cin;
using std::endl;
using std::vector;
double tillFarm(double tillRate, double tillC)
{
	return tillC / tillRate;
}
double afterFarm(double Rate, double afterF, double afterX)
{
	return (afterX) / (Rate + afterF);
}
double noFarm(double Rate, double noX)
{
	return (noX) / (Rate);
}
double getTime(double rate, double c, double x, double f)
{
	//cout << "Gettin Time" << endl;
	double time = 0;
	double afterF = 0;
	double afterX = 0;
	double tillF = 0;
	while (true)
	{
		//cout << "OldTime = " << time << endl;
		afterF = afterFarm(rate, c, x);
		//cout << "afterF =" << afterF << endl;
		afterX = noFarm(rate, x);
		//cout << "afterX = " << afterX << endl;
		tillF = tillFarm(rate, c);
		if ((tillF + noFarm(rate + f, x)) < afterX)
		{
			time += tillF;
			//cout << "newTime = " << time << endl;
			rate += f;
			//system("PAUSE");

		}
		else
		{
			time += afterX;
			//cout << "newTime = " << time << endl;
			//system("PAUSE");

			break;
		}
	}
	//system("PAUSE");
	return time;
}

void main()
{
	std::ifstream inFile;
	std::ofstream outFile;
	double T;
	double temp;
	inFile.open("C:/Users/Brendan/Dropbox/Compsci/big2.in");
	cout << "File opened" << endl;
	inFile >> T;
	vector<double> C;
	vector<double> F;
	vector<double> X;
	vector<double> times;
	double cps;
	for (int i = 0; i < T;i++)
	{
		inFile >> temp;
		C.push_back(temp);
		//cout << C.back() << endl;
		inFile >> temp;
		F.push_back(temp);
		//cout << F.back() << endl;
		inFile >> temp;
		X.push_back(temp);
		//cout << X.back() << endl;
	}

	double tempTime;
	for (int i = 0; i < T; i++)
	{
		cps = 2;
		tempTime = getTime(cps, C[i], X[i], F[i]);
		times.push_back(tempTime);
		//cout << tempTime << endl;
	}
	outFile.open("C:/Users/Brendan/Dropbox/Compsci/jam2b.txt");
	{
		outFile.precision(7);
		outFile.setf(std::ios::fixed);
		outFile.setf(std::ios::showpoint);
		for (int i = 0; i < times.size(); i++)
		{
			outFile << "Case #";
			outFile << i + 1;
			outFile << ": ";
			outFile << times[i];
			outFile << "\n";
		}
	}
	system("PAUSE");
}