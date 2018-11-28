#define _CRT_SECURE_NO_WARNINGS 1

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

#define PROBLEM "D"
#define INPUT "large"
#define ATTEMPT "0"
#define VERIFY 0
const string PATH("C:\\Stas\\Code Jam\\IO\\QR");


class solver
{
	long long k, c, s;


public:
	solver()
	{
		cin >> k >> c >> s;
	};

	void solve(stringstream &cout)
	{
		int n_checks = (k - 1) / c + 1;
		if (n_checks > s)
		{
			cout << "IMPOSSIBLE";
			return;
		}

		vector<long long> results;

		for (int i = 0; i < n_checks; i++)
		{
			long long counter = i * c + 1;
			long long result = i * c;

			for (int j = 1; j < c; j++)
				result = result * k + min(k-1, counter++);

			results.push_back(result + 1);
		};

		sort(results.begin(), results.end());

		for (long long r : results) cout << r << " ";

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