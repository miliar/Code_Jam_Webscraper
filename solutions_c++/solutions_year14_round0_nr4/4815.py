#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>

using namespace std;

int MyComparer(double a, double b)
{
	return a > b;
}

int GetSol_W(vector<double> nVector, vector<double> kVector)
{
	int MAX_POINTS = nVector.size();
	int ken_points = 0;

	sort(nVector.begin(), nVector.end());
	sort(kVector.begin(), kVector.end());

	while (1)
	{
		double NLarge = *(nVector.end() - 1);
		double KLarge = *(kVector.end() - 1);
		cout << endl;

		if (NLarge > KLarge)
		{
			nVector.erase(nVector.end() - 1);
			kVector.erase(kVector.begin());
		}
		else
		{
			nVector.erase(nVector.end() - 1);
			kVector.erase(kVector.end() - 1);
			++ken_points;
		}

		if (nVector.size() == 0)
			break;
	}
	int naomi_points = MAX_POINTS - ken_points;
	return naomi_points;
}

int GetSol_DW(vector<double> nVector, vector<double> kVector)
{
	int MAX_POINTS = nVector.size();
	int naomi_points = 0;

	sort(nVector.begin(), nVector.end());
	sort(kVector.begin(), kVector.end());

	while (1)
	{
		double NLarge = *(nVector.end() - 1);
		double KLarge = *(kVector.end() - 1);

		if (KLarge > NLarge)
		{
			kVector.erase(kVector.end() - 1);
			nVector.erase(nVector.begin());
		}
		else
		{
			nVector.erase(nVector.end() - 1);
			kVector.erase(kVector.end() - 1);
			++naomi_points;
		}

		if (nVector.size() == 0)
			break;
	}
	
	return naomi_points;
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
		cout << "Solving " << _case << " of " << nTests << " ANSWER: ";

		char szNum[10] = { 0 };
		fin.getline(szNum, 10, '\n');
		int nElements = atoi(szNum);

		char szLine[30000] = { 0 };
		fin.getline(szLine, 30000, '\n');
		vector<double> naomiVector = StringToVectorDouble(szLine);
		
		fin.getline(szLine, 30000, '\n');
		vector<double> kenVector = StringToVectorDouble(szLine);

		int DWResult = GetSol_DW(naomiVector, kenVector);
		int WResult = GetSol_W(naomiVector, kenVector);

		cout << DWResult << " " << WResult << endl;
		fout << "Case #" << _case << ": " << DWResult << " " << WResult << endl;
	}

	fin.close();
	fout.close();
	system("PAUSE");
	return 0;
}