#include <iostream>
#include <string>
#include <vector>
#include <stdlib.h>

using namespace std;

void solve(int a, string& b, int i);

int main()
{
	int n;
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		int a;
		string b;
		cin >> a >> b;
		//if (i == 2)
		solve(a, b, i);
	}

	return 0;
}

int solve2(vector<int>& vec)
{
	int total = 0;
	int nfriends = 0;
	for (int i = 0; i < vec.size(); i++)
	{
		int threshold = i;
		int want = 0;
		if (total >= threshold || vec[i] == 0)
		{
		}
		else
		{
			want = threshold - total;
		}
		nfriends += want;
		total += vec[i] + want;
	//	cout << i << " " << vec[i] << " " << total << " " << threshold << endl;
	}

	return nfriends;
}

void solve(int a, string& b, int i)
{
	vector<int> vec;
	for (int i = 0; i < b.size(); i++)
	{
		const char c = b[i];
		//cout << atoi(&c) << " ";
		vec.push_back(atoi(&c));
	}

	cout << "Case #" << i+1 << ": " << solve2(vec) << endl;
}
