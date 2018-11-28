#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <fstream>

using namespace std;

void del(map<char, int> &m, string &num, int count)
{
	for (int i = 0; i < num.length(); i++)
	{
		m[num[i]] -= count;
	}
}

int main()
{
	//ifstream cin("in.in");
	//ofstream cout("out.txt");
	int tests;
	cin >> tests;
	for (int i = 1; i <= tests; i++)
	{
		string s;
		cin >> s;

		//int sz = s.length();
		vector<int> v(10);
		map<char, int> m;
		for (int j = 0; j < s.length(); j++)
		{
			m[s[j]]++;
		}

		
		vector<string> nums(10);
		nums[0] = "ZERO";
		nums[1] = "ONE";
		nums[2] = "TWO";
		nums[3] = "THREE";
		nums[4] = "FOUR";
		nums[5] = "FIVE";
		nums[6] = "SIX";
		nums[7] = "SEVEN";
		nums[8] = "EIGHT";
		nums[9] = "NINE";

		v[0] = m['Z'];
		del(m, nums[0], m['Z']);

		v[8] = m['G'];

		del(m, nums[8], m['G']);

		v[6] = m['X'];

		del(m, nums[6], m['X']);

		v[2] = m['W'];

		del(m, nums[2], m['W']);

		v[3] = m['H'];

		del(m, nums[3], m['H']);

		v[4] = m['R'];

		del(m, nums[4], m['R']);

		v[1] = m['O'];

		del(m, nums[1], m['O']);

		v[5] = m['F'];

		del(m, nums[5], m['F']);

		v[9] = m['I'];

		del(m, nums[9], m['I']);

		v[7] = m['V'];

		del(m, nums[7], m['V']);

		cout << "Case #" << i << ": ";

		for (int j = 0; j < 10; j++)
		{
			while (v[j] > 0)
			{
				cout << j;
				v[j]--;
			}
		}
		cout << endl;
		
	}
	return 0;
}

