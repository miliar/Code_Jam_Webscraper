#include <iostream>
#include <fstream>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

int min_shuffle(vector<int>& v)
{
	int total = 0;
	for(int i = 0; i < v.size(); i++)
	{
		int left, right;
		left = 0;
		right = 0;
		for(int j = i - 1; j >= 0; j--)
		{
			if(v[j] > v[i]) left++;
		}
		for(int j = i + 1; j < v.size(); j++)
		{
			if(v[j] > v[i]) right++;
		}

		if(left < right) total += left;
		else total += right;
	}
	return total;
}

int main(int argc, char** argv)
{
	int T;
	cin >> T;

	for(int i = 1; i <= T; i++)
	{
		int N;
		vector<int> v;
		cin >> N;

		v.resize(N);
		for(int j = 0; j < N; j++)
		{
			cin >> v[j];
		}

		int sol = min_shuffle(v);
		cout << "Case #" << i << ": " << sol << endl;
	}
	return 0;
}

