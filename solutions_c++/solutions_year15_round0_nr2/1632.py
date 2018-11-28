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
#include <cassert>

using namespace std;

#define PROBLEM "B"
#define INPUT "large"
#define ATTEMPT "2"
#define VERIFY 0
const string PATH("C:\\Stas\\Programming\\Competitive_CPP\\CPP\\IO\\2015\\QR");

map<vector<long long>, int> Answers;

class solver
{
	int n;
	int maxp = 0;
	vector<int> People;

public:
	solver()
	{
		cin >> n;
		People = vector<int>(n, 0);
		for (int i = 0; i < n; i++)
		{
			cin >> People[i];
			maxp = max(maxp, People[i]);
		}

	}

	void solve(stringstream &S)
	{
		vector<long long> splits(maxp + 1, 0);

		for (int i = 0; i < People.size(); i++)
		{
			for (int j = 1; j < People[i]; j++)
				splits[j] += (People[i] - 1) / j;
		}
		
		long long bestcount = maxp;

		for (int i = 1; i < maxp; i++)
			bestcount = min(bestcount, i + splits[i]);

		S << bestcount;

	};
};



int main()
{
	clock_t start = clock(); 

	string Name = PATH + '\\' + PROBLEM + "-" + INPUT;
	if (INPUT == string("small")) Name = Name + "-attempt" + ATTEMPT;
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
		while (true)
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