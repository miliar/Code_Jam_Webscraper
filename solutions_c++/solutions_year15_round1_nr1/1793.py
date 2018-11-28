#include "stdafx.h"
#include <string>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <fstream>
#include <sstream>
#include <iomanip>

using namespace std;

int firstMethod(vector<int>& m)
{
	int ans = 0;
	int N = m.size();
	for (int i = 1;i < N; ++i)
	{
		ans += max(m[i-1]-m[i], 0);
	}
	return ans;
}

int secondMethod(vector<int>& m)
{
	int N = m.size();
	int delta = 0, ans = 0;
	for (int i = 1; i < N; ++i)
	{
		delta = max(delta, m[i-1]-m[i]);
	}
	for (int i = 0; i < N-1; ++i)
	{
		ans += min(m[i], delta);
	}
	return ans;
}

int main(int argc, char* argv[])
{
	ifstream in("A-large.in");
	ofstream out("result.txt");
	int T, N;
	in >> T;
	for (int i = 0; i < T; ++i)
	{
		in >> N;
		vector<int> m(N, 0);
		for (int j = 0; j < N; ++j) in >> m[j];
		out << "Case #" << i+1 << ": " << firstMethod(m) << " " << secondMethod(m) << endl;
	}

	in.close();
	out.close();
	return 0;
}