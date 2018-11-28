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
const string PATH("C:\\Users\\stan\\Documents\\visual studio 2013\\Projects\\ConsoleApplication1\\ConsoleApplication1\\GCJ2016_R2");


class solver
{
	int N, R, P, S;

public:
	solver()
	{
		cin >> N >> R >> P >> S;

	};

	char wins(char A, char B)
	{
		if (A == 'F' || B == 'F') return 'F';
		if (A == B) return 'F';
		if (A == 'R' && B == 'S') return 'R';
		if (A == 'S' && B == 'P') return 'S';
		if (A == 'R' && B == 'P') return 'P';
		if (A == 'S' && B == 'R') return 'R';
		if (A == 'P' && B == 'S') return 'S';
		if (A == 'P' && B == 'R') return 'P';
	}
	
	char check(string A, int s, int e)
	{
		if (e == s) return A[e];

		char L = check(A, s, (e - s) / 2 + s);
		char R = check(A,  (e - s) / 2 + s + 1, e);

		return wins(L, R);
	}

	void solve(stringstream &cout)
	{
		string A((1 << N), ' ');
		vector<pair<int, string>> Q;
		Q.push_back({ 0, "P"});
		Q.push_back({ 0, "R"});
		Q.push_back({ 0, "S"});
		int n = 1 << N;

		for (int k = 0; k < P; k++) Q[0].first++;
		for (int j = P; j < P+R; j++) Q[1].first++;
		for (int t = P+R; t < P+R+S; t++) Q[2].first++;

		while (n > 1)
		{
			map<string, int> Next;
			for (int i = 0; 2 * i < n; i++)
			{
				sort(Q.rbegin(), Q.rend());
				if (Q.size() < 2 || Q[1].first == 0)
				{
					cout << "IMPOSSIBLE";
					return;
				}
				if (Q[0].second < Q[1].second) Next[Q[0].second + Q[1].second]++;
				else  Next[Q[1].second + Q[0].second]++;
				Q[0].first--;
				Q[1].first--;
			}
			Q.clear();
			for (auto a : Next)
				Q.push_back({ a.second, a.first });
			n = n / 2;
		}
		cout << Q[0].second;
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