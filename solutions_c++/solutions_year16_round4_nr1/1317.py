#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <functional>      // For greater<int>()
#include <stdio.h>
#include <cstdlib>
#include <cmath>
#include <map>
#include <set>
#include <queue>
#include <sstream>
using namespace std;

void GetNumVec(vector<int> &v, int N)
{
	v.resize(3);
	v[0] = 1;
	for (int i = 0; i < N; ++i)
	{
		int r = v[0] + v[1];
		int p = v[1] + v[2];
		int s = v[0] + v[2];
		v[0] = r;
		v[1] = p;
		v[2] = s;
	}
}

void Shift(vector<int> &v)
{
	int r = v[0];
	int p = v[1];
	int s = v[2];
	v[0] = p;
	v[1] = s;
	v[2] = r;
}

int Check(vector<int> &v0, vector<int> &v)
{
	if (v0 == v)
		return 0;
	Shift(v0);
	if (v0 == v)
		return 1;
	Shift(v0);
	if (v0 == v)
		return 2;
	return -1;
}

string Double(string &str)
{
	string ret(str.length() * 2, ' ');
	for (int i = 0; i < str.length(); ++i)
	{
		if (str[i] == 'R')
		{
			ret[i * 2] = 'R';
			ret[i * 2 + 1] = 'S';
		}
		else if (str[i] == 'P')
		{
			ret[i * 2] = 'P';
			ret[i * 2 + 1] = 'R';
		}
		else if (str[i] == 'S')
		{
			ret[i * 2] = 'P';
			ret[i * 2 + 1] = 'S';
		}
	}
	return ret;
}

// i=0 ‚È‚ç 1ŒÂ‚¸‚ÂA
// i=1 ‚È‚ç2ŒÂ‚¸‚Â
// i=2 ‚È‚ç4ŒÂ‚¸‚Â
// Ž«‘Ž®‚É‚È‚é‚æ‚¤“ü‚ê‘Ö‚¦‚éB
void Permute(string &s, int i)
{
	int blockSize = (int)pow(2, i);
	int pairSize = blockSize * 2;
	int numPairs = s.length() / pairSize;
	for (int i = 0; i < numPairs; ++i)
	{
		string a = s.substr(i * pairSize, blockSize);
		string b = s.substr(i * pairSize + blockSize, blockSize);
		if (a > b)
		{
			a.copy(&s[i * pairSize + blockSize], blockSize);
			b.copy(&s[i * pairSize], blockSize);
		}
	}
}

static void HandleCase(const int cse)
{
	int N, R, P, S;
	cin >> N >> R >> P >> S;

	vector<int> v0;
	v0.push_back(R);
	v0.push_back(P);
	v0.push_back(S);

	vector<int> v;
	GetNumVec(v, N);

	int shift = Check(v0, v);

	char *seed[3] = {"R", "P", "S"};
	if (shift >= 0)
	{
		string s(seed[shift]);
		for (int i = 0; i < N; ++i)
			s = Double(s);
		for (int i = 0; i < N; ++i)
			Permute(s, i);
		cout << "Case #" << cse << ": " << s << endl;
	}
	else
		cout << "Case #" << cse << ": IMPOSSIBLE" << endl;
}


int main()
{
	//freopen("test.in", "r", stdin);
	//freopen("test.out", "w", stdout);

	//freopen("A-small-attempt0.in", "r", stdin);
//	freopen("A-small-attempt0.out", "w", stdout);

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int T;
	cin >> T;

	for (int i = 0; i < T; ++i)
		HandleCase(i + 1);

	return 0;
}


