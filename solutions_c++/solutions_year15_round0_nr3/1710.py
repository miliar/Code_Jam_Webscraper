#define _CRT_SECURE_NO_WARNINGS 1

#include <vector>
#include <list>
#include <map>
#include <unordered_set>
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

#define PROBLEM "C"
#define INPUT "small"
#define ATTEMPT "1"
#define VERIFY 0
const string PATH("C:\\Stas\\Code Jam\\IO\\QR");

map<string, pair<int, string>> M = {
							{ "11", make_pair(1, "1")},
							{ "1i", make_pair(1, "i") },
							{ "1j", make_pair(1, "j") },
							{ "1k", make_pair(1, "k") },

							{ "i1", make_pair(1, "i") },
							{ "ii", make_pair(-1, "1") },
							{ "ij", make_pair(1, "k") },
							{ "ik", make_pair(-1, "j") },

							{ "j1", make_pair(1, "j") },
							{ "ji", make_pair(-1, "k") },
							{ "jj", make_pair(-1, "1") },
							{ "jk", make_pair(1, "i") },

							{ "k1", make_pair(1, "k") },
							{ "ki", make_pair(1, "j") },
							{ "kj", make_pair(-1, "i") },
							{ "kk", make_pair(-1, "1") }
};


class solver
{
	int L, X;
	int s;
	string T;
	string LS;

public:
	solver()
	{
		cin >> L >> X;
		cin >> T;

		assert(T.size() == L);

		for (int i = 0; i < X; i++)
		for (int j = 0; j < T.size(); j++)
			LS.push_back(T[j]);
	};

	void solve(stringstream &S)
	{
		vector<int> startcand;
		unordered_set<int> endcand;

		/*if (LS.size() < 3)
		{
			S << "NO";
			return;
		}*/
		
		string C = "1";
		int sgn = 1;

		for (int i = 0; i < LS.size() - 2; i++)
		{
			auto o = M[C + LS[i]];
			C = o.second;
			sgn *= o.first;
			if (C == "i" && sgn == 1) startcand.push_back(i + 1);
		}

		C = "1";
		sgn = 1;
		for (int i = LS.size() - 1; i > 1; i--)
		{
			auto o = M[LS[i] + C];
			C = o.second;
			sgn *= o.first;

			if (C == "k" && sgn == 1) endcand.insert(i - 1);
		}

		for (auto c = startcand.begin(); c != startcand.end(); c++)
		{
			C = "1";
			sgn = 1;
			for (int i = *c; i < LS.size() - 1; i++)
			{
				auto o = M[C + LS[i]];
				C = o.second;
				sgn *= o.first;
				if (C == "j" && sgn == 1 && endcand.count(i))
				{
					S << "YES";
					return;
				}
			}
		}
		S << "NO";
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