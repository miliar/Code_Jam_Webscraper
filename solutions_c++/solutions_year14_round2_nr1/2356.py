#include <string>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <fstream>
#include <sstream>
#include <iomanip>

using namespace std;

string squeezing(string s)
{
	string res(1, s[0]);
	for (int i = 1; i < s.length(); ++i)
	{
		if (s[i] != s[i-1])
		{
			res += s[i];
		}
	}
	return res;
}

int repeater(vector<string>& S)
{
	string s = squeezing(S[0]);
	for (int i = 1; i < S.size(); ++i)
	{
		string tmp = squeezing(S[i]);
		if (tmp != s)
			return -1;
	}

	int m = S.size();
	int n = s.length();
	int c[100][100];
	memset(c, 0, 10000*sizeof(int));
	for (int k = 0; k < m; ++k)
	{
		string v = S[k];
		int i = 0;
		for (int j = 0; j < n; ++j)
		{
			while (i < v.length() && s[j] == v[i])
			{
				++i;
				++c[k][j];
			}
		}
	}

	int res = 0;
	for (int j = 0; j < n; ++j)
	{
		int mean = 0;
		for (int i = 0; i < m; ++i)
			mean += c[i][j];
		mean /= m;
		int sum = 0;
		for (int i = 0; i < m; ++i)
			sum += abs(c[i][j]-mean);
		res += sum;
	}
	return res;
}

int main(int argc, char* argv[])
{
	ifstream in("A-small-attempt0.in");
	ofstream out("result.txt");
	int T, N;
	in >> T;
	for (int i = 0; i < T; ++i)
	{
		in >> N;
		vector<string> S(N, "");
		for (int j = 0; j < N; ++j)
			in >> S[j];
		int res = repeater(S);
		if (res != -1)
			out << "Case #" << i+1 << ": " << res << endl;
		else
			out << "Case #" << i+1 << ": Fegla Won" << endl;
	}

	in.close();
	out.close();
	return 0;
}