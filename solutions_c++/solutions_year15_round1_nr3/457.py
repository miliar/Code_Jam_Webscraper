#define _CRT_SECURE_NO_WARNINGS

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
#define ATTEMPT "0"
#define VERIFY 0
const string PATH("C:\\Users\\stan\\Documents\\visual studio 2013\\Projects\\ConsoleApplication1\\ConsoleApplication1\\GCJ2015_R1A");


class solver
{
	int n;
	vector<pair<long long, long long>> T;
	map<pair<long long, long long>, int> M;

public:
	solver()
	{
		cin >> n;

		T = vector<pair<long long, long long>>(n);
		M = map<pair<long long, long long>, int>();

		for (int i = 0; i < n; i++)
		{
			cin >> T[i].first >> T[i].second;
			M[T[i]] = i;
		}

	};
	
	bool cw(pair<long long, long long> a, pair<long long, long long> b, pair<long long, long long> c) {
		return a.first*(b.second - c.second) + b.first*(c.second - a.second) + c.first*(a.second - b.second) <= 0;
	}

	bool ccw(pair<long long, long long> a, pair<long long, long long> b, pair<long long, long long> c) {
		return a.first*(b.second - c.second) + b.first*(c.second - a.second) + c.first*(a.second - b.second) >= 0;
	}
	
	
	void convex_hull(vector<pair<long long, long long> > & a) {
		if (a.size() == 1)  return;
		sort(a.begin(), a.end());
		pair<long long, long long> p1 = a[0], p2 = a.back();
		vector<pair<long long, long long> > up, down;
		up.push_back(p1);
		down.push_back(p1);
		for (size_t i = 1; i<a.size(); ++i) {
			if (i == a.size() - 1 || cw(p1, a[i], p2)) {
				while (up.size() >= 2 && !cw(up[up.size() - 2], up[up.size() - 1], a[i]))
					up.pop_back();
				up.push_back(a[i]);
			}
			if (i == a.size() - 1 || ccw(p1, a[i], p2)) {
				while (down.size() >= 2 && !ccw(down[down.size() - 2], down[down.size() - 1], a[i]))
					down.pop_back();
				down.push_back(a[i]);
			}
		}
		a.clear();
		for (size_t i = 0; i<up.size(); ++i)
			a.push_back(up[i]);
		for (size_t i = down.size() - 2; i>0; --i)
			a.push_back(down[i]);
	}

	void solve(stringstream &S)
	{
		int i = 0;
		vector<int> Ans(T.size(), 15);

		int maxcount = 15;

		int maxj = 1 << T.size();

		for (int j = 0; j < maxj; j++)
		{
			vector<pair<long long, long long>> B = T;
			int i = j;
			int count = 0;
			int tree = T.size() - 1;

			while (i > 0)
			{
				if (i % 2)
				{
					B.erase(B.begin() + tree);
					count += 1;
				}
				i /= 2;
				tree--;
			}

			if (count >= maxcount) continue;

			convex_hull(B);

			for (int i = 0; i < B.size(); i++)
				Ans[M[B[i]]] = min(Ans[M[B[i]]], count);

			maxcount = 0;
			for (int i = 0; i < Ans.size(); i++)
				maxcount = max(maxcount, Ans[i]);
		}
		
		for (int i = 0; i < Ans.size(); i++)
			S << "\n" << Ans[i];
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