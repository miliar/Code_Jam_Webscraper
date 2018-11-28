#include <iostream>
#include <fstream>
#include <iomanip>
#include <string>
#include <vector>
#include <map>
#include <cstdio>
#include <cstring>
#include <deque>
#include <queue>

using namespace std;

#if defined WIN32
#define scanf scanf_s
#endif

double solve(double c, double f, double x)
{
	double cur = 2;
	double total = 0;
	while (x / cur > c / cur + x / (cur + f)) {
		total += c / cur;
		cur = cur + f;
	}

	return total + x / cur;
}

double dfs(double c, double cur, double f, double x)
{
	
	if (x / cur < c / cur + x / (cur + f))
		return x / cur;
	else
		return (c / cur + dfs(c, cur + f, f, x));
}

int main()
{
	ifstream fin("large.txt");
	ofstream fout("result.txt");
	int t;
	double c, f, x;
	fin >> t;
	int index = 0;
	while (t--) {
		fin >> c >> f >> x;
		fout << setiosflags(ios::fixed) << setprecision(7)  << "Case #" << ++index << ": " << solve(c, f, x) << endl;
	}
	return 0;
}