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

#define PROBLEM "D"
#define INPUT "small"
#define ATTEMPT "1"
#define VERIFY 0
const string PATH("C:\\Users\\stan\\Documents\\visual studio 2013\\Projects\\ConsoleApplication1\\ConsoleApplication1\\GCJ2015_R2");

vector<vector<int>> Answers = { { 2, 1, 1, 3 }, { 2, 3, 2, 2 }, { 3, 1, 1, 5 }, { 3, 3, 1, 5 }, { 6, 4, 2, 19 } };

class solver
{
	int r, c;

public:
	solver()
	{
		cin >> r >> c;
	};

	void solve(stringstream &S)
	{
		S << Answers[r - 2][c - 3];
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


/* PYTHON CODE TO GENERATE ANSWERS:

from math import factorial

for Y in range(2, 7) :
print "{",
for X in range(3, 7) :

A = [[0 for _ in range(X)] for _ in range(Y)];
Answers = set()

direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]

def consistency_check(A) :
#   print A
for y in range(Y) :
for x in range(X) :
if A[y][x] == 0 :
continue
count = 0
zeros = 0
for d in range(4) :
y1 = y + direction[d][0]
	if y1 >= Y or y1 < 0 :
		continue
		x1 = (x + direction[d][1]) % X
	if (A[y1][x1] == A[y][x]) :
		count += 1
	if (A[y1][x1] == 0) :
		zeros += 1

	if count > A[y][x]:
	return False

	if count + zeros < A[y][x] :
		return False

		return True


		def dive(x, y) :
	for n in range(1, 5) :
		A[y][x] = n
	if consistency_check(A) :
		x1 = x + 1
		y1 = y
	if x1 == X :
		y1 += 1
		x1 = 0
	if y1 == Y :
		R = []
		for y2 in range(Y) :
			R.append("".join(str(i) for i in A[y2]))
			Answers.add(tuple(R))
			break
			dive(x1, y1)
			A[y][x] = 0


			dive(0, 0)

			Clean = set()

		for a in Answers :
		success = True;
		b = list(a)
		for j in range(X) :
		if (tuple(b) in Clean) :
			success = False
			break
		for i in range(Y) :
			b[i] = b[i][1:] + b[i][0]
			if success :
				Clean.add(a)

				print len(Clean), ",",
				print "},",











*/