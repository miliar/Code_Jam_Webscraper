#include <iostream>
#include <fstream>

using namespace std;

#define NMAX 50

int N, J;
int data[NMAX];
int answer[1000];

void get_input()
{
	N = 16;	J = 50;
	//N = 6;	J = 7;
}

void increment_one()
{
	int itor;

	++data[N - 2];

	for (itor = N - 1; itor > 0; --itor)
	{
		if (data[itor] == 2)
		{
			++data[itor - 1];
			data[itor] = 0;
		}
	}
}

__int64 trans_base(int base)
{
	int itor;
	__int64 result = 0;
	__int64 multiple = 1;

	for (itor = N - 1; itor >= 0; --itor)
	{
		result += (data[itor] * multiple);
		multiple *= base;
	}

	return result;
}

int find_divider(__int64 number)
{
	int itor;
	int search = sqrt((double)number) + 1;

	for (itor = 2; itor < search; ++itor)
	{
		if (number % itor == 0)
		{
			if ((itor % 2) == 0 && ((number / itor)) % 2 == 0)
				continue;

			return itor;
		}
	}
	return -1;
}

void find_next()
{
	int flag;
	int base;
	__int64 trans;

	while (1)
	{
		flag = 0;
		increment_one();
		for (base = 2; base <= 10; ++base)
		{
			trans = trans_base(base);
			answer[base - 2] = find_divider(trans);
			
			if (answer[base - 2] == -1)
			{
				flag = 1;
				break;
			}
		}

		
		int itor2;
		for (itor2 = 0; itor2 < N; ++itor2)
			cout << data[itor2];
		cout << endl;
		

		if (flag == 0)
			break;
	}
}

void print_answer()
{
	fstream fp;
	fp.open("output.out", ofstream::out | ofstream::trunc);

	fp << "Case #1:" << endl;

	memset(data, 0, sizeof(data));
	
	data[N - 1] = 1;
	data[N - 2] = -1;
	data[0] = 1;

	int itor, itor2;
	for (itor = 0; itor < J; ++itor)
	{
		find_next();
		for (itor2 = 0; itor2 < N; ++itor2)
			fp << data[itor2];

		fp << " ";

		for (itor2 = 2; itor2 <= 10; ++itor2)
		{
			fp << answer[itor2 - 2];
			if (itor2 != 10)
			{
				fp << " ";
			}
		}

		fp << endl;
	}

	fp.close();
}

int main()
{
	get_input();
	print_answer();
	return 0;
}
