#include <iostream>
#include <fstream>
#include <stdio.h>
#include <vector>
#include <math.h>

#define i64 long long int

using namespace std;

const int N = 16;
const int J = 50;
i64 seq[N-2];
i64 divs[11];
i64 nums[11];
ofstream fout("out1.txt");
i64 seq_count = 0;

bool next_seq()
{
	++seq_count;
	int i = 0;
	while(i < N - 2 && seq[i] == 1)
	{
		seq[i] = 0;
		++i;
	}
	if (i == N - 2)
	{
		return false;
	}
	else
	{
		seq[i] = 1;
		return true;
	}
}

i64 get_num(i64 base)
{
	i64 pow = base;
	i64 ans = 1;
	for (int i = 0; i < N - 2; ++i)
	{
		ans += seq[i] * pow;
		pow *= base;
	}
	ans += pow;
	return ans;
}

i64 find_div(i64 num)
{
	for (i64 i = 2; i <= sqrt(num) + 1; ++i)
	{
		if (num % i == 0)
		{
			return i;
		}
	}
	return 0;
}

bool is_jamcoin()
{
	for (int i = 2; i <= 10; ++i)
	{
		i64 num = get_num(i);
		i64 div = find_div(num);
		if (!div)
		{
			return false;
		}
		else
		{
			divs[i] = div;
			nums[i] = num;
		}
	}
	return true;
}

void print_ans()
{
	fout << "1";
	for(int i = N-3; i >= 0; --i)
	{
		fout << seq[i];
	}
	fout << "1 ";
	for (int i = 2; i <= 10; ++ i)
	{
		fout << divs[i] << " ";
	}
	fout << endl;
}


int main()
{
	fout << "Case #1:" << endl;
	int count_ans = 0;
	if (is_jamcoin())
	{
		print_ans();
		++count_ans;
	}
	while (next_seq())
	{
//		cout << seq_count << " " << count_ans << endl;
		if (is_jamcoin())
		{
			print_ans();
			++count_ans;
		}
		if (count_ans == J)
		{
			break;
		}
	}
	return 0;
}

