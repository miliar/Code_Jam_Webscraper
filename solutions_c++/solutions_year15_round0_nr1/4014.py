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

int ovation(int N, string s)
{
	int ans = 0, sum = 0;
	int k = s[0]-'0';
	if (k==0)
	{
		++ans;
		sum = 1;
	}
	else
	{
		sum = k;
	}
	for (int i = 1; i <= N; ++i)
	{
		k = s[i]-'0';
		if (sum < i)
		{
			ans += i-sum;
			sum = i;
		}
		sum += k;
	}
	return ans;
}

int main(int argc, char* argv[])
{
	ifstream in("A-large.in");
	ofstream out("result.txt");
	int T, N;
	string s;
	in >> T;
	for (int i = 0; i < T; ++i)
	{
		in >> N >> s;
		out << "Case #" << i+1 << ": " << ovation(N, s) << endl;
	}

	in.close();
	out.close();
	return 0;
}