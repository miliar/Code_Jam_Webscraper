#include <iostream>
#include <cstdio>
#include <fstream>
#include <set>

using namespace std;

void digit_to_set(const int num, set<int>& digit_set)
{
	int value = num;
	while (value> 0)
	{
		digit_set.insert(value % 10);
		value /= 10;
	}
}

void solve()
{
	ifstream in("input.txt");
	ofstream out("output.txt");

	int T;
	in >> T;
	for (int t = 1; t <= T; t++)
	{
		int seed;
		in >> seed;

		int cur_num = seed;
		int last_cur_num = cur_num;
		set<int> digit_set;
		while (true)
		{
			digit_to_set(cur_num, digit_set);
			if (digit_set.size() == 10) break;
			
			cur_num += seed;
			if (last_cur_num == cur_num) break;
			last_cur_num = cur_num;
		}
		if (digit_set.size() < 10)
			out << "Case #" << t << ": " << "INSOMNIA" << endl;
		else
			out << "Case #" << t << ": " << cur_num << endl;
	}
}


int main(int argc, char** argv)
{
	solve();
	return 0;
}