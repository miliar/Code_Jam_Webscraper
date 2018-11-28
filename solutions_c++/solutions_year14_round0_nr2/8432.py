#include <string>
#include <iostream>
#include <sstream>
#include <fstream>
#include <set>
#include <vector>
#include <iomanip>
using namespace std;

bool compareSteps(double c, double f, double x, int iter)
{
	double first = 0.0, second = 0.0;
	first = x / (2.0 + iter * f);
	second = c / (2.0 + iter * f) + x / (2.0 + (iter + 1.0) * f);
//	cout << iter << endl;
//	cout << "first: " << first << "second: " << second << endl;
//	cout << "-----------------------------" << endl;
	if (first < second)
		return true;
	else
		return false;
};

double countSec(double c, double f, double x, int iter)
{
	double res0 = x / 2.0;
	double res = c / 2.0;
	if (iter == 0) return res0;
	for (int i = 1; i < iter; i++)
	{
		res += c / (2.0 + i * f);
	}

	res += x / (2.0 + iter * f);

	return res;
}

int main()
{
	ifstream in;
	in.open("D:/B-large.in");
	ofstream outputFile;
	outputFile.open("D:/B-large.out");
	string str;
	getline(in, str);
	int tcNr;
	tcNr = stoi(str);
	double cee=0.0, fee=0.0, xee=0.0;
	for (int i = 0; i < tcNr; i++)
	{
		getline(in, str);
		
		istringstream iss(str);
		string sub;

		iss >> sub;
		cee = stold(sub);
		iss >> sub;
		fee = stold(sub);
		iss >> sub;
		xee = stold(sub);

//		cout << "C : " << cee << ", F: " << fee << ", X: " << xee << endl;

		bool stop = false;
		int j = 0;
		while (!stop){
			stop = compareSteps(cee, fee, xee, j);
			j++;
		}

		double result = 0.0;
		result = countSec(cee, fee, xee, j-1);
		
		outputFile.setf(ios::fixed, ios::floatfield);
		outputFile.precision(7);

		int nr = i + 1;
		string out = "Case #" + to_string(nr) + ": ";
		outputFile << out << result << endl;

	}

	outputFile.close();
	system("pause");

}