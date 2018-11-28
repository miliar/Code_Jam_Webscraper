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

#define PROBLEM "B"
#define INPUT "small"
#define ATTEMPT "0"
#define VERIFY 0
const string PATH("C:\\Users\\stan\\Documents\\visual studio 2013\\Projects\\ConsoleApplication1\\ConsoleApplication1\\GCJ2015_R2");


class solver
{
	double  V, X;
	int n;
	vector<double> speed;
	vector<double> temp;

public:
	solver()
	{
		
		cin >> n >> V >> X;
		for (int i = 0; i < n; i++)
		{
			double t1, t2;
			cin >> t1 >> t2;
			speed.push_back(t1);
			temp.push_back(t2);
		}
	};

	void solve(stringstream &S)
	{
		if (speed.size() == 1)
		{
			if (temp[0] == X) S << fixed << setprecision(10) << V / speed[0];
			else S << "IMPOSSIBLE";
			return;
		}

		double s1 = speed[0];
		double s2 = speed[1];
		double t1 = temp[0];
		double t2 = temp[1];

		if (t1 < X && t2 < X)
		{
			S << "IMPOSSIBLE";
			return;
		}

		if (t1 > X && t2 > X)
		{
			S << "IMPOSSIBLE";
			return;
		}

		if (t1 == X && t2 == X)
		{
			S << fixed << setprecision(10) << V / (s1 + s2);
			return;
		}

		if (t1 == X && t2 != X)
		{
			S << fixed << setprecision(10) << V / s1;
			return;
		}

		if (t1 != X && t2 == X)
		{
			S << fixed << setprecision(10) << V / s2;
			return;
		}

		double time2 = (V * X - V * t1) / (s2*t2 - s2*t1);
		double time1 = (V * X - V * t2) / (s1*t1 - s1*t2);
		S << fixed << setprecision(10) << max(time1, time2);
		return;
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