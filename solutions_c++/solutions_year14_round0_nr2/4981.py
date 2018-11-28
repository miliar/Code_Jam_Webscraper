#include <iostream>
#include <fstream>
#include <cstdio>
#include <vector>

using namespace std;


double CalculateForN(double C, double F, double X, double n)
{
	double term2 = X / (n * F + 2);

	double term1 = 0.0;
	for (int x = 0; x < n; x++)
	{
		double t = C * (1 / (x * F + 2));
		term1 += t;

		double totaltime = term1 + term2;
		//cout << totaltime << endl;
	}

	return term1 + term2;
}
double GetAnswer(double C, double F, double X)
{
	double answer = -7749;
	double vel = 2;
	if (C >= X)
	{
		answer = X / vel;
	}

	double prevAns = X / 2;
	int MAX_N = INT_MAX;

	for (int n = 0; n < MAX_N; n++)
	{
		double curAns = CalculateForN(C, F, X, n);

		if (curAns > prevAns)
			return prevAns;
		else
			prevAns = curAns;

		//cout << answer << endl;
	}

	return answer;
}

vector<double> StringToVectorDouble(string input)
{
	string temp = "";
	vector<double> t;
	for (int i = 0; i < input.size(); i++)
	{
		if (input.at(i) == ' ')
		{
			t.push_back(atof(temp.c_str()));
			temp = "";
		}
		else
		{
			temp += input.at(i);
		}
	}
	t.push_back(atof(temp.c_str()));

	return t;
}

int main()
{
	ifstream fin("input.txt", ios::in);
	ofstream fout("output.txt", ios::out);

	char szTests[5] = { 0 };
	fin.getline(szTests, 5, '\n');
	int nTests = atoi(szTests);

	for (int _case = 1; _case <= nTests; ++_case)
	{
		cout << "Solving " << _case << " of " << nTests << " Answer: ";
		char buf[200] = { 0 };
		fin.getline(buf, 200, '\n');
		
		auto lineVector = StringToVectorDouble(buf);
		double result = GetAnswer(lineVector.at(0), lineVector.at(1), lineVector.at(2));
		fout.precision(7);
		fout << "Case " << "#" << _case << ": " << fixed << result << endl;
		cout << fixed << result << endl;
	}

	fin.close();
	fout.close();
	system("PAUSE");
	return 0;
}