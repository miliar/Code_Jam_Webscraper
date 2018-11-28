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
	int k, n;
	vector<double> p;

	friend istream& operator >> (istream& lhs, Input& rhs)
	{
		lhs >> rhs.n >> rhs.k;
		for (int i = 0; i < rhs.n; ++i)
		{
			double p;
			lhs >> p;
			rhs.p.push_back(p);
		}
		return lhs;
	}
};

struct Output
{
	double ans;

	friend ostream& operator << (ostream& lhs, const Output& rhs)
	{
		static int case_number = 0;
		lhs.precision(10);
		return lhs << "Case #" << ++case_number << ": " << rhs.ans << endl;
	}
};

Output solve(Input input)
{
	double best = -1;
	for (int i = 0; i < (1 << input.n); ++i)
	{
		vector<double> sel;
		for (int j = 0; j < input.n; ++j)
		{
			if (i & (1 << j))
			{
				sel.push_back(input.p[j]);
			}
		}
		if ((int)sel.size() != input.k)
		{
			continue;
		}
		vector<double> p(input.k + 1, 0);
		p[0] = 1;
		for (double c : sel)
		{
			for (int j = (int)p.size() - 1; j > -1; --j)
			{
				p[j] = p[j] * (1 - c) + p[j - 1] * c;
			}
		}
		best = max(best, p[input.k / 2]);
	}
	return{ best };
}

int main(int argc, char* argv[])
{
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