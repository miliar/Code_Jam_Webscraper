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
#define INPUT "large"
#define ATTEMPT "0"
#define VERIFY 0
const string PATH("C:\\Users\\stan\\Documents\\visual studio 2013\\Projects\\ConsoleApplication1\\ConsoleApplication1\\GCJ2015_R2");

const vector<pair<int, int>> Dir = { { -1, 0 }, { 0, 1 }, { 1, 0 }, { 0, -1 } };

class solver
{
	int r, c;
	vector<string> Map;
	vector<int> Graph;
	vector<vector<int>> Directions;
	vector<int> outsiders;

public:
	solver()
	{
		cin >> r >> c;
		Map = vector<string>(r);
		for (int i = 0; i < r; i++)
			cin >> Map[i];

	};

	void solve(stringstream &S)
	{
		Graph = vector<int>(r * c);
		Directions = vector<vector<int>>(r * c, vector<int>(4));

		for (int i = 0; i < r; i++)
		{
			for (int j = 0; j < c; j++)
			{
				if (Map[i][j] == '.') continue;
				for (int d = 0; d < 4; d++)
				{
					int i1 = i + Dir[d].first;
					int j1 = j + Dir[d].second;
					while (i1 >= 0 && i1 < r && j1 >= 0 && j1 < c)
					{
						if (Map[i1][j1] != '.')
						{
							Directions[i * c + j][d] = i1 * c + j1;
							break;
						}
						i1 += Dir[d].first;
						j1 += Dir[d].second;
					}
					if (!(i1 >= 0 && i1 < r && j1 >= 0 && j1 < c)) 	Directions[i * c + j][d] = -1;
				}
				switch (Map[i][j])
				{
				case '^':
					Graph[i*c + j] = Directions[i*c + j][0];
					break;
				case '>':
					Graph[i*c + j] = Directions[i*c + j][1];
					break;
				case 'v':
					Graph[i*c + j] = Directions[i*c + j][2];
					break;
				case '<':
					Graph[i*c + j] = Directions[i*c + j][3];
					break;
				}
				if (Graph[i*c + j] == -1)  outsiders.push_back(i*c + j);
			}
		}

		bool success = true;
		int count = 0;

		while (outsiders.size() > 0 && success)
		{
			int i = outsiders.back();
			int j;
			for (j = 0; j < 4; j++)
			{
				if (Directions[i][j] != -1)
				{
					Graph[i] = Directions[i][j];
					count++;
					break;
				}
			}
			if (j == 4) success = false;
			else outsiders.pop_back();
		}

		if (!success) S << "IMPOSSIBLE";
		else S << count;

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