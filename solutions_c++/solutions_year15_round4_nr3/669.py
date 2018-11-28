#include <iostream>
#include <fstream>
#include <sstream>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <vector>
#include <iomanip>
#include <cmath>
#include <algorithm>
#include <numeric>
#include <iterator>

using namespace std;

ifstream in("C1.in");
ofstream out("C1.out");

int n;
int answer;
vector < vector <int> > h;

int hash1(const string& s)
{
	int hash = 0;
	for (int i = 0; i < s.size(); ++i)
		hash = hash * 26 + s[i] - 'a' + 1;
	return hash;
}

void dzzel(vector<int>& v)
{
	sort(v.begin(), v.end());
	v.erase(unique(v.begin(), v.end()), v.end());
}

void rec( vector <int>& en,  vector <int>& fr, int k)
{
	if (k == n - 2)
	{
		vector <int> en1 = en;
		vector <int> fr1 = fr;
		dzzel(en1);
		dzzel(fr1);

		vector <int> sp;
		set_intersection(en1.begin(), en1.end(), fr1.begin(), fr1.end(), back_inserter(sp));
		if (sp.size() < answer || answer == -1)
			answer = sp.size();

		return;
	}

	for (int j = 0; j < h[k + 2].size(); ++j)
	{
		en.push_back(h[k + 2][j]);
	}
	rec(en, fr, k + 1);
	for (int j = 0; j < h[k + 2].size(); ++j)
		en.pop_back();

	for (int j = 0; j < h[k + 2].size(); ++j)
	{
		fr.push_back(h[k + 2][j]);
	}
	rec(en, fr, k + 1);

	for (int j = 0; j < h[k + 2].size(); ++j)
		fr.pop_back();
}

int main()
{
	char temp[10000];
	int test;
	in >> test;
	for (int t = 1; t <= test; ++t)
	{
		in >> n;
		vector < vector <string> > s(n);
		h.clear();
		h.resize(n);
		in.getline(temp, 10000);
		for (int i = 0; i < n; ++i)
		{
			string str, st;
			getline(in, str);
			istringstream read(str);
			while (read >> st)
			{
				s[i].push_back(st);
				h[i].push_back(hash1(st));
			}
		}

		vector <int> english;
		vector <int> french;
		for (int i = 0; i < s[0].size(); ++i)
			english.push_back(h[0][i]);
		for (int i = 0; i < s[1].size(); ++i)
			french.push_back(h[1][i]);

		dzzel(english);
		dzzel(french);


		//vector <int> sg;

		//set_intersection(english.begin(), english.end(), french.begin(), french.end(), back_inserter(sg));

		answer = -1;

		//if (n == 2)
		//	answer = sg.size();

		rec(english, french, 0);
		
		out << "Case #" << t << ": " << answer << endl;
	}
	return 0;
}