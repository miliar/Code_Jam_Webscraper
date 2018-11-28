#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <iomanip>

using namespace std;

ifstream in("b1.in");
ofstream out("b1.out");

int yndhanurQanak, chistBarer, maximumBarer;

int solve(const string& a, const string& b)
{
	int k = -1, answer = -1;
	do
	{
		k++;
		answer++;
		k = a.find(b, k);
	} while (k != string::npos);
	return answer;
}

void rec(const string& tarer, int qanak, const string & s, const string& bar)
{
	if (qanak == 0)
	{
		yndhanurQanak++;
		int t = solve(s, bar);
		chistBarer += t;
		maximumBarer = max(maximumBarer, t);
		return;
	}

	for (int i = 0; i < tarer.size(); ++ i)
		rec(tarer, qanak - 1, s + tarer[i], bar);
}

int main()
{
	int test;
	in >> test;
	for (int t = 1; t <= test; ++t)
	{
		string tarer, bar;
		int k, L, s;
		double answer;
		in >> k >> L >> s;
		in >> tarer >> bar;

		yndhanurQanak = 0;
		chistBarer = 0;
		maximumBarer = 0;
		rec(tarer, s, "", bar);

		//cout << yndhanurQanak << " " << chistBarer << " " << maximumBarer << endl;

		answer = (double)maximumBarer - (double)chistBarer / yndhanurQanak;

		out << "Case #" << t << ": " << fixed << setprecision(8) << answer << endl;
	}
}