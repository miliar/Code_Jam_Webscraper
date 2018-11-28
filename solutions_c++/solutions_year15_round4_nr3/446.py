#include <iostream>
#include <algorithm>
#include <set>
#include <vector>
#include <limits>
#include <future>
#include <sstream>
#include <functional>
#include <climits>
using namespace std;

struct TestCase
{
	int n;
	vector<string> lines;
	vector<vector<int>> sents;
	vector<string> db;

	void input()
	{
		string line;
		getline(cin, line);
		stringstream tmp;
		tmp << line;
		tmp >> n;
		for (int i = 0; i < n; i++)
		{
			getline(cin, line);
			lines.push_back(line);
		}
		answer = INT_MAX;
	}
	int answer = 0;
	set<int> endb, frdb, checked;
	set<int> enCache, frCache, ckCache;
	void clear()
	{
		endb = enCache;
		frdb = frCache;
		checked = ckCache;
	}
	
	void adden(int a)
	{
		if (checked.count(a))
		{
			return;
		}
		endb.insert(a);
		if (frdb.count(a))
		{
			checked.insert(a);
		}
	}
	
	void addfr(int a)
	{
		if (checked.count(a))
		{
			return;
		}
		frdb.insert(a);
		if (endb.count(a))
		{
			checked.insert(a);
		}
	}

	void makeDb(string a)
	{
		stringstream ss(a);
		while (!ss.eof())
		{
			string k;
			ss >> k;
			db.push_back(k);
		}
	}

	void retDb(string a, int i)
	{
		sents.push_back(vector<int>());
		stringstream ss(a);
		while (!ss.eof())
		{
			string k;
			ss >> k;
			int j = distance(db.begin(), lower_bound(db.begin(), db.end(), k));
			sents[i].push_back(j);
		}
	}

	void addSentEn(const vector<int> &a)
	{
		for (auto &k : a)
		{
			adden(k);
		}
	}

	void addSentFr(const vector<int> &a)
	{
		for (auto &k : a)
		{
			addfr(k);
		}
	}

	void check()
	{
		answer = min(answer, (int)checked.size());
	}

	void process()
	{
		for (int i = 0; i < n; i++)
		{
			makeDb(lines[i]);
		}
		sort(db.begin(), db.end());
		db.erase(unique(db.begin(), db.end()), db.end());
		for (int i = 0; i < n; i++)
		{
			retDb(lines[i], i);
		}

		auto en = sents[0];
		auto fr = sents[1];
		if (n == 2)
		{
			clear();
			addSentEn(en);
			addSentFr(fr);
			check();
			return;
		}
		clear();
		
		addSentEn(en);
		addSentFr(fr);
		for (auto &ccc : checked)
		{
			endb.erase(ccc);
			frdb.erase(ccc);
		}
		enCache = endb;
		frCache = frdb;
		ckCache = checked;

		sents.erase(sents.begin());
		sents.erase(sents.begin());
		int mm = 1 << sents.size();
		for (int h = 0; h < mm; h++)
		{
			clear();
			for (int p = 0; p < sents.size(); p++)
			{
				int hand = 1 << p;
				bool isEn = h & hand;
				if (isEn)
				{
					addSentEn(sents[p]);
				}
				else
				{
					addSentFr(sents[p]);
				}
				if (answer < checked.size())
				{
					break;
				}
			}
			check();
		}
	}
	void output()
	{
		cout << answer;
	}
};

int main()
{
	int t;
	string line;
	getline(cin, line);
	stringstream tmp;
	tmp << line;
	tmp >> t;
	vector<TestCase> testCases(t);
	vector<future<void>> futures;
	for (int i = 0; i < t; i++)
	{
		testCases[i].input();
	}
	for (int i = 0; i < t; i++)
	{
		futures.push_back(async(launch::async, [&](int p){ testCases[p].process(); }, i));
	}
	for (int i = 0; i < t; i++)
	{
	}
	for (int i = 0; i < t; i++)
	{
		futures[i].wait();
		cout << "Case #" << i + 1 << ": ";
		testCases[i].output();
		cout << endl;
	}
	return 0;
}
