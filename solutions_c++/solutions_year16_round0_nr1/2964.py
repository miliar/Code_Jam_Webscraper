// ProblemA.cpp : Defines the entry point for the console application.
//

#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctime>
#include <string>
#include <fstream>

using namespace std;

#define vi vector<int>
#define MAX_BOUND 123456789

string counting_sheep(vi start_num)
{
	vi flag(10, 0);
	vi s(32, 0);
	int start_len = start_num.size();
	int s_len = 32;
	for (int i = 1; i <= start_len; i++)
		s[s_len - i] = start_num[start_len - i];

	do
	{
		int top_index = 0;
		while (top_index < s_len && s[top_index] == 0)
			top_index++;

		for (int i = top_index; i < s_len; i++)
			flag[s[i]]++;

		bool stop = true;
		for (int i = 0; i < 10; i++)
			if (flag[i] == 0)
				stop = false;

		if (stop)
		{
			string result;
			for (int j = top_index; j < s_len; j++)
				result += '0' + s[j];
			return result;
		}

		int carry = 0;
		for (int i = 1; i <= start_len; i++)
		{
			int sum = (s[s_len - i] + start_num[start_len - i] + carry);
			carry = sum / 10;
			s[s_len - i] = sum % 10;
		}

		int k = s_len - start_len - 1;
		while (carry && k >= 0)
		{
			int sum = (s[k] + carry);
			carry = sum / 10;
			s[k] = sum % 10;
			k--;
		}

		if (carry)
			return "INSOMNIA";

	} while (true);

	return "INSOMNIA";
}

int main()
{
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");

	int item_count = 0;
	fin >> item_count;

	for (int i = 0; i < item_count; i++)
	{
		int num;
		fin >> num;

		if (num == 0)
		{
			fout << "Case #" << i + 1 << ": INSOMNIA" << endl;
			continue;
		}

		vi start_num;
		while (num)
		{
			start_num.push_back(num % 10);
			num = num / 10;
		}

		reverse(start_num.begin(), start_num.end());


		fout << "Case #" << i + 1 << ": " << counting_sheep(start_num) << endl;
	}

	return 0;
    return 0;
}

