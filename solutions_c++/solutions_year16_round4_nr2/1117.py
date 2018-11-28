#define _CRT_SECURE_NO_WARNINGS

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#define INPUT "small"
#define ATTEMPT "1"
#define VERIFY 0
const string PATH("C:\\Users\\stan\\Documents\\visual studio 2013\\Projects\\ConsoleApplication1\\ConsoleApplication1\\GCJ2016_R2");

class solver
{
	int n, k;
	vector<double> P;


public:
	solver()
	{
		cin >> n >> k;
		P = vector<double>(n);

		for (int i = 0; i < n; i++)
			cin >> P[i];


	}

	double probability(vector<double> C)
	{
		double A = 0.0;
		for (int i = 0; i < 1 << k; i++)
		{
			int count = 0;
			double Pr = 0.0;
			int j = i;
			int index = 0;
			while (index < k)
			{
				if (j & 1) Pr += log(C[index]), count++;
				else Pr += log(1.0 - C[index]);
				j >>= 1;
				index += 1;
			}
			if (count == k / 2) A += exp(Pr);
		}
		return A;
	}

	void solve(stringstream &cout)
	{
		sort(P.begin(), P.end());
		vector<double> C(k);
		for (int i = 0; i < k / 2; i++)
			C[i] = P[i];
		for (int i = 0; i < k / 2; i++)
			C[i + k / 2] = P[P.size() - 1 - i];

		double best = 0.0;

		for (int i = 0; i < 1 << n; i++)
		{
			vector<double> C1;
			int count = 0;
			double Pr = 0.0;
			int j = i;
			int index = 0;
			while (index < n)
			{
				if (j & 1) C1.push_back(P[index]), count++;
				j >>= 1;
				index += 1;
			}
			if (count == k)  best = max(best, probability(C1));
		}

		cout << fixed << setprecision(7) << best;

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