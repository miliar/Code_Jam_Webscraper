#define _CRT_SECURE_NO_WARNINGS

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define PROBLEM "C"
#define INPUT "small"
#define ATTEMPT "0"
#define VERIFY 0
const string PATH("C:\\Users\\stan\\Documents\\visual studio 2013\\Projects\\ConsoleApplication1\\ConsoleApplication1\\GCJ2015_R2");


class solver
{
	map<string, int> Dictionary;
	map<string, int> Other;

	vector<int> Words;
	
	vector<vector<int>> Lines;
	int n;

public:
	solver()
	{
		cin >> n;
		n--;
		n--;

		string T;
		int count = 0;
		getline(cin, T);
		getline(cin, T);

		stringstream A(T);

		while (!A.eof())
		{
			string W;
			A >> W;
			if (Dictionary.count(W) == 0)
			{
				Dictionary[W] = count++;
				Words.push_back(0);
			}
			Words[Dictionary[W]] |= 1;
		}

		getline(cin, T);

		A = stringstream(T);

		while (!A.eof())
		{
			string W;
			A >> W;
			if (Dictionary.count(W) == 0)
			{
				Dictionary[W] = count++;
				Words.push_back(0);
			}
			Words[Dictionary[W]] |= 2;
		}

		while (n--)
		{
			getline(cin, T);

			Lines.push_back(vector<int>());

			stringstream A(T);

			while (!A.eof())
			{
				string W;
				A >> W;

				if (Dictionary.count(W) == 0)
				{
					Dictionary[W] = count++;
					Words.push_back(0);
				}

				Lines.back().push_back( Dictionary[W]);
			}
		}

	};

	void solve(stringstream &S)
	{
		int bestcount = Dictionary.size();
		for (int i = 0; i < 1 << Lines.size(); i++)
		{
			int c = i;
			vector<int> Words2 = Words;
			for (int j = 0; j < Lines.size(); j++)
			{
				int bit = c & 1;
				c >>= 1;
				for (int k = 0; k < Lines[j].size(); k++)
					Words2[Lines[j][k]] |= 1 << bit;
			}
			int count = 0;
			for (int j = 0; j < Words2.size(); j++)
				if (Words2[j] == 3) count++;

			bestcount = min(count, bestcount);
		}

		S << bestcount;
	};
};



int main()
{
	clock_t start = clock();

	string Name = PATH + '\\' + PROBLEM + "-" + INPUT;
	if (INPUT == "small") Name = Name + "-attempt" + ATTEMPT;
	string InName = Name + ".in";
	string OutName = Name + ".out";

	freopen(InName.c_str(), "r", stdin);
	ofstream output;
	ifstream input;
	string before = "";
	vector<string> Before;
	if (VERIFY)
	{
		input.open(OutName.c_str());
		string T;
		while (getline(input, T)) before += T + "\n";

		int i = 1;
		int j = 0;
		for (;;)
		{
			string search = "Case #" + to_string((long long)i) + ":";
			int j2 = before.find(search);
			if (j2 == string::npos) break;
			if (j != 0) Before.push_back(before.substr(j + 1, j2 - 2 - j));
			j = j2 + search.length();
			i++;
		}
		Before.push_back(before.substr(j + 1, before.length() - 2 - j));
	}
	else  output.open(OutName.c_str());

	int T;
	cin >> T;

	vector<solver> A(T);
	vector<string> Answers(T);



	for (size_t i = 0; i < A.size(); i++)
	{
		stringstream S;
		A[i].solve(S);
		Answers[i] = S.str();
		cout << "Case #" << (i + 1) << ": " << Answers[i] << "\n";
	}

	bool errors = false;

	for (size_t i = 0; i < A.size(); i++)
	{
		cout << "Case #" << (i + 1) << ": " << Answers[i] << "\n";
		if (VERIFY)
		{
			if (Before[i] != Answers[i])
			{
				cout << "ERROR - PREVIOUSLY: " << Before[i] << "\n";
				errors = true;
			};

		}
		else output << "Case #" << (i + 1) << ": " << Answers[i] << "\n";
	}

	if (errors) cout << "ERRORS WERE FOUND IN SOLUTION" << "\n";

	clock_t end = clock();
	cout << "Time: " << (double)(end - start) / CLOCKS_PER_SEC << " seconds" << "\n";

};