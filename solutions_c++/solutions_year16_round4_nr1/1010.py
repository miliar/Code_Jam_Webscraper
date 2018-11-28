#define _CRT_SECURE_NO_WARNINGS
#include <ios>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <vector>
#include <stack>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <cmath>
#include <chrono>
#include <cstdlib>
#include <future>
#include <numeric>
#include <functional>
#include <iterator>

using namespace std;

struct Input
{
	int n, p, r, s;

	friend istream& operator >> (istream& lhs, Input& rhs)
	{
		return lhs >> rhs.n >> rhs.r >> rhs.p >> rhs.s;
	}
};

struct Output
{
	string s;

	friend ostream& operator << (ostream& lhs, const Output& rhs)
	{
		static int case_number = 0;
		return lhs << "Case #" << ++case_number << ": " << rhs.s << endl;
	}
};

vector<vector<string>> answers;

Output solve(Input input)
{
	for (string str : answers[input.n])
	{
		int p = 0, r = 0, s = 0;
		for (char c : str)
		{
			if (c == 'P')
			{
				++p;
			}
			else if (c == 'R')
			{
				++r;
			}
			else
			{
				++s;
			}
		}
		if (p == input.p && r == input.r && s == input.s)
		{
			return{ str };
		}
	}
	return{ "IMPOSSIBLE" };
}

string minimize(string s)
{
	if (s.size() == 1)
	{
		return s;
	}
	string s1, s2;
	for (size_t i = 0; i < s.size(); ++i)
	{
		if (i < s.size() / 2)
		{
			s1 += s[i];
		}
		else
		{
			s2 += s[i];
		}
	}
	s1 = minimize(s1);
	s2 = minimize(s2);
	if (s1 < s2)
	{
		return s1 + s2;
	}
	return s2 + s1;
}

void generate()
{
	answers.emplace_back();
	answers[0].push_back("P");
	answers[0].push_back("R");
	answers[0].push_back("S");
	for (int i = 1; i < 13; ++i)
	{
		answers.emplace_back();
		for (int j = 0; j < 3; ++j)
		{
			string s;
			for (char c : answers[i - 1][j])
			{
				if (c == 'P')
				{
					s += "PR";
				}
				else if (c == 'R')
				{
					s += "RS";
				}
				else
				{
					s += "PS";
				}
			}
			answers[i].push_back(minimize(s));
		}
	}
}

int main(int argc, char* argv[])
{
	generate();
	auto start = chrono::system_clock::now();
	ios_base::sync_with_stdio(false);
	ifstream fin(argv[1]);
	ofstream fout(argv[2]);
	int t;
	fin >> t;
	int ready = 0;
	vector<future<Output>> tasks;
	mutex cout_mutex;
	for (int i = 0; i < t; ++i)
	{
		Input input;
		fin >> input;
		tasks.push_back(async([&ready, &t, &cout_mutex](Input input)
		{
			auto ans = solve(input);
			cout_mutex.lock();
			system("cls");
			cout << ++ready << "/" << t << endl;
			cout_mutex.unlock();
			return ans;
		}, input));
	}
	for (auto& task : tasks)
	{
		fout << task.get();
	}
	auto finish = chrono::system_clock::now();
	auto elapsed = chrono::duration_cast<chrono::duration<float, std::ratio<1, 1>>>(finish - start);
	cout << "Done!" << endl;
	cout << "Time elapsed: " << elapsed.count() << " s" << endl;
	string s;
	getline(cin, s);
	return 0;
}