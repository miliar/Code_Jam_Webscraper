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

bool myfunction(int i, int j)
{
	return (i>j);
}

int pancake(vector<int>& v)
{
	sort(v.begin(), v.end(), myfunction);
	if (v[0]<=3) return v[0];

	int ans = v[0];
	for (int i = 2; i <= v[0]/2; ++i)
	{
		vector<int> v1(v);
		v1[0] = i;
		v1.push_back(v[0]-i);
		ans = min(ans, 1+pancake(v1));
	}

	return ans;
}

int main(int argc, char* argv[])
{
	ifstream in("B-small-attempt1.in");
	ofstream out("result.txt");
	int T, D;
	in >> T;
	for (int i = 0; i < T; ++i)
	{
		in >> D;
		vector<int> v(D, 0);
		for (int j = 0; j < D; ++j)
		{
			in >> v[j];
		}
		out << "Case #" << i+1 << ": " << pancake(v) << endl;
	}

	in.close();
	out.close();
	return 0;
}