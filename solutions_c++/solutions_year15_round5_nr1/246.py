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

#define PROBLEM "A"
#define INPUT "small"
#define ATTEMPT "0"
#define VERIFY 0
const string PATH("C:\\Users\\stan\\Documents\\visual studio 2013\\Projects\\ConsoleApplication1\\ConsoleApplication1\\GCJ2015_R3");

const vector<pair<int, int>> Dir = { { -1, 0 }, { 0, 1 }, { 1, 0 }, { 0, -1 } };

class solver
{
	vector<int> S;
	vector<int> Sum;
	vector<vector<int>> E;
	int n, d;


public:
	solver()
	{
		cin >> n >> d;
		S = vector<int>(n);
		Sum = vector<int>(n, -1);
		E = vector<vector<int>>(n);

		long long s, a, c, r;
		cin >> s >> a >> c >> r;
		for (int i = 0; i < n; i++)
		{
			S[i] = s;
			s = (s * a + c) % r;
		}

		long long m;
		cin >> m >> a >> c >> r;
		for (int i = 1; i < n; i++)
		{
			m = (m * a + c) % r;
			E[m%i].push_back(i);
		}


	};

	int count(int e)
	{
		if (E[e].size() == 0)
			return 1;
		if (Sum[e] == -1)
		{

			int counter = 1;
			for (int i = 0; i < E[e].size(); i++)
				counter += count(E[e][i]);
			Sum[e] = counter;
		}
		
		return Sum[e];
	}

	int dive(int e, int s)
	{
		if (S[e] < s || S[e] > s + d)
			return count(e);

		int count = 0;
		for (int i = 0; i < E[e].size(); i++)
			count += dive(E[e][i], s);

		return count;

	}

	void solve(stringstream &T)
	{
		int best = n;
		int start = max(S[0] - d, 0);
		int end = min(1001, S[0]);

		for (int s = start; s <= end; s++)
		{
			best = min(best, dive(0, s));
		}

		T << n - best << "\n";

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