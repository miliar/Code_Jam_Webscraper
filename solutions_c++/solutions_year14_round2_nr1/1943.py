#include <iostream>
#include <sstream>
#include <vector>
#include <math.h>
#include <algorithm>
#include <functional>

using namespace std;

int solve( vector<string>& sa )
{
	if (sa.size() != 2)
		return -1;

	int num = 0;

	string s1 = sa[0];
	string s2 = sa[1];

	int i = 0, j = 0;
	while (i < s1.length() && j < s2.length())
	{
		if (s1[i] == s2[j])
		{
			++i; ++j;
		}
		else if (i > 0 && s1[i] == s1[i-1])
		{
			char c = s1[i];
			for (; i < s1.length() && s1[i] == c; ++i, ++num);
		}
		else if (j > 0 && s2[j] == s2[j-1])
		{
			char c = s2[j];
			for (; j < s2.length() && s2[j] == c; ++j, ++num);
		}
		else {
			num = -1;
			break;
		}
	}

	if (num >= 0 && i < s1.length() && j >= s2.length())
	{
		if (i > 0 && s1[i] == s1[i-1])
		{
			char c = s1[i];
			for (; i < s1.length() && s1[i] == c; ++i, ++num);
		}
	}
	else if (num >= 0 && j > 0 && s2[j] == s2[j-1])
	{
		char c = s2[j];
		for (; j < s2.length() && s2[j] == c; ++j, ++num);
	}

	if (num >= 0 && i < s1.length() || j < s2.length())
		num = -1;

	return num;
}


int main()
{
	int nc = 0;
	cin >> nc;

	for (int c = 0; c < nc; ++c)
	{
		int N;
		cin >> N ;

		vector<string> sa(N);
		for (int i = 0; i < N; ++i)
			cin >> sa[i];
		
		
		cout << "Case #" << c + 1 << ": ";
		int num = solve(sa);
		if (num >= 0)
			cout << num << endl;
		else
			cout << "Fegla Won" << endl;
	}

	return 0;
}
